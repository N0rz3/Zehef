import asyncio
import sys
import os
from pathlib import Path
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve the frontend static files
frontend_dir = Path(__file__).resolve().parents[1] / 'frontend'
if not frontend_dir.exists():
    raise RuntimeError(f"Frontend directory not found: {frontend_dir}")

app.mount('/', StaticFiles(directory=str(frontend_dir), html=True), name='static')


@app.websocket('/ws/search')
async def websocket_search(ws: WebSocket):
    await ws.accept()
    proc = None
    try:
        data = await ws.receive_json()
        email = data.get('email')
        if not email:
            await ws.send_json({'type': 'error', 'msg': 'Missing email'})
            await ws.close()
            return

        # Locate the project root and zehef.py
        project_root = Path(__file__).resolve().parents[2]
        script_path = project_root / 'zehef.py'
        if not script_path.exists():
            await ws.send_json({'type': 'error', 'msg': f'zehef.py not found at {script_path}'})
            await ws.close()
            return

        cmd = [sys.executable, str(script_path), email]
        # Start subprocess and stream stdout/stderr
        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,
        )

        # Read lines and forward to websocket
        while True:
            line = await proc.stdout.readline()
            if not line:
                break
            text = line.decode('utf-8', errors='replace')
            await ws.send_text(text)

        rc = await proc.wait()
        await ws.send_text(f"\nProcess exited with code {rc}\n")
        await ws.close()

    except WebSocketDisconnect:
        # client disconnected
        if proc and proc.returncode is None:
            try:
                proc.terminate()
                await proc.wait()
            except Exception:
                pass
    except Exception as e:
        # send error and close
        try:
            await ws.send_json({'type': 'error', 'msg': str(e)})
            await ws.close()
        except Exception:
            pass
