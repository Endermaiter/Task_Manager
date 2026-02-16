Write-Host "🚀 Starting setup..." -ForegroundColor Cyan

$originalPath = Get-Location

$root = $PSScriptRoot
$backendPath = Join-Path $root "task_manager_api"
$frontendPath = Join-Path $root "task_manager_frontend"

$currentPolicy = Get-ExecutionPolicy -Scope CurrentUser
if ($currentPolicy -ne "RemoteSigned" -and $currentPolicy -ne "Unrestricted") {
    Write-Host "⚠️ The execution policy does not allow running scripts. Please run this first:" -ForegroundColor Yellow
    Write-Host "Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned" -ForegroundColor Cyan
    exit 1
}
Write-Host "✅ Execution policy is correct. Continuing..." -ForegroundColor Green

Write-Host "🐍 Installing backend dependencies..." -ForegroundColor Green
poetry install --no-root --directory "$backendPath"
Write-Host "✅ Backend dependencies installed." -ForegroundColor Green

# Show installed packages
poetry show --directory "$backendPath"

Write-Host "🟢 Installing frontend dependencies..." -ForegroundColor Green
npm install
Write-Host "✅ Frontend dependencies installed." -ForegroundColor Green

Write-Host "🚀 Launching Django and Vue servers..." -ForegroundColor Cyan

Start-Process powershell -ArgumentList "-NoExit", "-Command", "poetry run python `"$backendPath\manage.py`" runserver"

Start-Process powershell -ArgumentList "-NoExit", "-Command", "npm --prefix `"$frontendPath`" run dev"

Write-Host "✅ Servers launched in separate windows. Check the consoles for logs." -ForegroundColor Green

Set-Location $originalPath