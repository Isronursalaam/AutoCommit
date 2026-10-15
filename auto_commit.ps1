# PowerShell Auto Commit Script
# Menjalankan auto_commit.py dan melakukan push ke remote GitHub
param (
    [switch]$Push
)

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "   GitHub Daily Auto Commit Runner       " -ForegroundColor Yellow
Write-Host "=========================================" -ForegroundColor Cyan

$scriptPath = Join-Path $PSScriptRoot "auto_commit.py"

if ($Push) {
    python $scriptPath --push
} else {
    python $scriptPath
}
