<#
Build a standalone Windows executable for Zehef using PyInstaller.

Usage:
  .\build_exe.ps1           # builds using py -3 or python
  .\build_exe.ps1 -Clean   # clean previous build artifacts then build

This script will:
 - detect a Python 3 interpreter (py -3, python3, or python)
 - create a temporary virtualenv in .\build_venv
 - install/upgrade pip, setuptools, wheel, pyinstaller
 - run PyInstaller to create a single-file exe
 - copy the resulting exe to ./dist/Zehef.exe
#>

param(
    [switch]$Clean,
    [ValidateSet('cli','gui','backend')]
    [string]$Target = 'cli',
    [string]$Icon = '',
    [switch]$NoConsole
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $scriptDir

function Find-Python3 {
    if (Get-Command py -ErrorAction SilentlyContinue) {
        & py -3 -c "import sys; assert sys.version_info[0]==3" > $null 2>&1
        if ($LASTEXITCODE -eq 0) { return @{exe='py'; args='-3'} }
    }
    if (Get-Command python3 -ErrorAction SilentlyContinue) {
        & python3 -c "import sys; assert sys.version_info[0]==3" > $null 2>&1
        if ($LASTEXITCODE -eq 0) { return @{exe='python3'; args=''} }
    }
    if (Get-Command python -ErrorAction SilentlyContinue) {
        & python -c "import sys; assert sys.version_info[0]==3" > $null 2>&1
        if ($LASTEXITCODE -eq 0) { return @{exe='python'; args=''} }
    }
    return $null
}

$py = Find-Python3
if (-not $py) {
    Write-Error "No Python 3 interpreter found. Install Python 3 and ensure 'py', 'python3', or 'python' is in PATH."
    exit 1
}

$venvDir = Join-Path $scriptDir 'build_venv'
if ($Clean -and (Test-Path $venvDir)) {
    Write-Host "Cleaning previous build venv..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force $venvDir
}

if (-not (Test-Path $venvDir)) {
    Write-Host "Creating virtual environment in $venvDir" -ForegroundColor Cyan
    if ($py.exe -eq 'py') {
        & py -3 -m venv $venvDir
    } else {
        & $($py.exe) $($py.args) -m venv $venvDir
    }
}

$pip = Join-Path $venvDir 'Scripts\pip.exe'
$python = Join-Path $venvDir 'Scripts\python.exe'

if (-not (Test-Path $pip)) {
    Write-Error "Virtualenv creation failed or pip not found at $pip"
    exit 1
}

Write-Host "Upgrading pip and installing PyInstaller in venv..." -ForegroundColor Cyan
& $pip install --upgrade pip setuptools wheel
& $pip install pyinstaller

Write-Host "Building executable with PyInstaller (target: $Target) ..." -ForegroundColor Cyan

# Remove previous PyInstaller artifacts if present
if (Test-Path "$scriptDir\build") { Remove-Item -Recurse -Force "$scriptDir\build" }
if (Test-Path "$scriptDir\dist") { Remove-Item -Recurse -Force "$scriptDir\dist" }
if (Test-Path "$scriptDir\zehef.spec") { Remove-Item -Force "$scriptDir\zehef.spec" }

if ($Target -eq 'gui') {
    $entry = 'zehef_gui.py'
    $name = 'ZehefGUI'
    $windowed = '--noconsole'
} elseif ($Target -eq 'backend') {
    # Build a packaged backend executable that runs the FastAPI app
    $entry = 'web\backend\run_server.py'
    $name = 'ZehefBackend'
    # allow building backend without a console window when requested
    if ($NoConsole) { $windowed = '--noconsole' } else { $windowed = '' }
} else {
    $entry = 'zehef.py'
    $name = 'Zehef'
    $windowed = ''
}

$iconArg = ''
if ($Icon -ne '') {
    $fullIcon = if ([System.IO.Path]::IsPathRooted($Icon)) { $Icon } else { Join-Path $scriptDir $Icon }
    if (Test-Path $fullIcon) {
        $iconArg = "--icon `"$fullIcon`""
    } else {
        Write-Warning "Icon not found at $fullIcon; building without icon."
    }
}

$entryPath = Join-Path $scriptDir $entry
if (-not (Test-Path $entryPath)) {
    Write-Error "Entry script not found: $entryPath"
    exit 1
}

$pyinstallerArgs = @('--onefile', $windowed, '--name', $name)
if ($iconArg -ne '') { $pyinstallerArgs += $iconArg }
$pyinstallerArgs += $entry

& $python -m PyInstaller @pyinstallerArgs

if ($LASTEXITCODE -ne 0) {
    Write-Error "PyInstaller failed (exit code $LASTEXITCODE)"
    exit $LASTEXITCODE
}

$exePath = Join-Path $scriptDir ("dist\{0}.exe" -f $name)
if (Test-Path $exePath) {
    Write-Host "Build succeeded: $exePath" -ForegroundColor Green
    Write-Host "You can distribute the single file executable at: $exePath" -ForegroundColor Green
} else {
    Write-Error "Expected exe not found at $exePath"
    exit 1
}

Write-Host "Done." -ForegroundColor Cyan
