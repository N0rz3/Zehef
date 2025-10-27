Param(
    [string]$NodePath = 'node',
    [string]$NpmPath = 'npm'
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $scriptDir

Write-Host "Preparing to build Electron app..." -ForegroundColor Cyan

if (-not (Get-Command $NpmPath -ErrorAction SilentlyContinue)) {
    Write-Error "npm not found. Install Node.js (which includes npm) and re-run this script."
    exit 1
}

$electronDir = Join-Path $scriptDir 'web\electron'
if (-not (Test-Path $electronDir)) {
    Write-Error "Electron scaffold not found at $electronDir"
    exit 1
}

# Build the Python backend exe first so it can be bundled into the Electron app
Write-Host "Building backend executable (PyInstaller) without console..." -ForegroundColor Cyan
& "$scriptDir\build_exe.ps1" -Target backend -NoConsole
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to build backend exe. Aborting Electron build."
    exit $LASTEXITCODE
}

# Copy backend exe into electron resources so electron-builder can include it
$backendExe = Join-Path $scriptDir 'dist\ZehefBackend.exe'
if (-not (Test-Path $backendExe)) {
    Write-Error "Expected backend exe not found at $backendExe"
    exit 1
}

$destDir = Join-Path $electronDir 'backend'
if (-not (Test-Path $destDir)) { New-Item -ItemType Directory -Path $destDir | Out-Null }
Copy-Item -Path $backendExe -Destination (Join-Path $destDir 'ZehefBackend.exe') -Force


Write-Host "Running npm install in $electronDir" -ForegroundColor Cyan
Push-Location $electronDir
& $NpmPath install
if ($LASTEXITCODE -ne 0) { Write-Error "npm install failed"; Pop-Location; exit $LASTEXITCODE }

Write-Host "Building Electron distributable (this may take a while)..." -ForegroundColor Cyan
& $NpmPath run dist
$rc = $LASTEXITCODE
Pop-Location

if ($rc -ne 0) {
    Write-Error "Electron build failed (exit code $rc). Check the npm logs above for details."
    exit $rc
}

Write-Host "Electron build finished. Output directory: electron_dist" -ForegroundColor Green
