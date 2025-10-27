Param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$Args
)

# Run from script directory so relative paths work
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $scriptDir

# Detect a Python 3 interpreter: try python3, then py -3, then python
$found = $null

if (Get-Command python3 -ErrorAction SilentlyContinue) {
    & python3 -c "import sys; assert sys.version_info[0]==3" > $null 2>&1
    if ($LASTEXITCODE -eq 0) { $found = "python3" }
}

if (-not $found -and (Get-Command py -ErrorAction SilentlyContinue)) {
    & py -3 -c "import sys; assert sys.version_info[0]==3" > $null 2>&1
    if ($LASTEXITCODE -eq 0) { $found = "py -3" }
}

if (-not $found -and (Get-Command python -ErrorAction SilentlyContinue)) {
    & python -c "import sys; assert sys.version_info[0]==3" > $null 2>&1
    if ($LASTEXITCODE -eq 0) { $found = "python" }
}

if (-not $found) {
    Write-Error "No Python 3 interpreter found. Install Python 3 and ensure 'python', 'python3', or the 'py' launcher is in PATH."
    exit 1
}

if ($found -eq "py -3") {
    $exe = "py"
    $exeArgs = @("-3","zehef.py") + $Args
} else {
    $exe = $found
    $exeArgs = @("zehef.py") + $Args
}

Write-Host "Running: $exe $($exeArgs -join ' ')" -ForegroundColor Cyan
& $exe @exeArgs
$exit = $LASTEXITCODE
exit $exit
