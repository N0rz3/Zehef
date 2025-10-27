const { app, BrowserWindow } = require('electron')
const { spawn } = require('child_process')
const path = require('path')
const http = require('http')

// Choose python executable cross-platform
const python = process.platform === 'win32' ? 'py' : 'python3'
const backendPort = process.env.ZEHEF_PORT || 8000
let backendProc = null

function startBackend() {
  if (app.isPackaged) {
    // In packaged app, run the bundled backend executable included under resources/backend/
    const exePath = path.join(process.resourcesPath, 'backend', process.platform === 'win32' ? 'ZehefBackend.exe' : 'ZehefBackend')
    console.log('Starting bundled backend:', exePath)
    backendProc = spawn(exePath, [], { stdio: 'inherit' })
    backendProc.on('exit', (code) => {
      console.log('Bundled backend exited with code', code)
    })
    return
  }

  // Development mode: run uvicorn using the system Python
  const projectRoot = path.resolve(__dirname, '..', '..')
  const cmd = python
  const args = ['-3', '-m', 'uvicorn', 'web.backend.app:app', '--host', '127.0.0.1', '--port', String(backendPort)]

  console.log('Starting backend (dev):', cmd, args.join(' '))
  backendProc = spawn(cmd, args, { cwd: projectRoot, stdio: 'inherit' })

  backendProc.on('exit', (code) => {
    console.log('Backend exited with code', code)
  })
}

function waitForBackendAndOpen() {
  const url = `http://127.0.0.1:${backendPort}`
  const maxAttempts = 60
  let attempts = 0

  const tryOpen = () => {
    attempts++
    http.get(url, (res) => {
      createWindow(url)
    }).on('error', (err) => {
      if (attempts < maxAttempts) {
        setTimeout(tryOpen, 250)
      } else {
        console.error('Backend did not start, opening anyway')
        createWindow(url)
      }
    })
  }

  tryOpen()
}

function createWindow(url) {
  const win = new BrowserWindow({
    width: 1000,
    height: 700,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true
    }
  })

  win.loadURL(url)
}

app.on('ready', () => {
  startBackend()
  waitForBackendAndOpen()
})

app.on('window-all-closed', () => {
  if (backendProc) {
    try { backendProc.kill() } catch (e) {}
    backendProc = null
  }
  if (process.platform !== 'darwin') app.quit()
})

app.on('quit', () => {
  if (backendProc) {
    try { backendProc.kill() } catch (e) {}
  }
})
