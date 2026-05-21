# 1. Run sync
uv sync --active

# 2. Build the full path to the src folder under the current script directory
$srcPath = Join-Path -Path $PSScriptRoot -ChildPath "src"

# 3. Check whether the path exists and is a directory (Container)
if (Test-Path -Path $srcPath -PathType Container) {
    Write-Host "Detected src folder, running pip install -e ." -ForegroundColor Green
    uv pip install -e .
}
else {
    Write-Host "src folder not detected; skipping install step." -ForegroundColor Yellow
}
