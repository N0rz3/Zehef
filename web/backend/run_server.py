"""
Launcher for the FastAPI backend used when packaging a standalone backend executable.
This runs Uvicorn programmatically so PyInstaller can bundle a single exe.
"""
import os
import sys
import uvicorn

def main():
    port = int(os.environ.get('ZEHEF_PORT', '8000'))
    host = os.environ.get('ZEHEF_HOST', '127.0.0.1')
    # Use the app path as module
    uvicorn.run('web.backend.app:app', host=host, port=port, log_level='info')

if __name__ == '__main__':
    main()
