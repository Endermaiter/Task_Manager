Write-Host "🚀 Starting setup..." -ForegroundColor Cyan

$originalPath = Get-Location

$root = $PSScriptRoot
$backendPath = Join-Path $root "task_manager_api"
$frontendPath = Join-Path $root "task_manager_frontend"

Write-Host "🐍 Installing backend dependencies..." -ForegroundColor Green
poetry install --no-root --directory "$backendPath"
Write-Host "✅ Backend dependencies installed." -ForegroundColor Green

poetry show --directory "$backendPath"

Write-Host "🟢 Installing frontend dependencies..." -ForegroundColor Green
npm install
Write-Host "✅ Frontend dependencies installed." -ForegroundColor Green

Write-Host "🚀 Launching Django and Vue servers..." -ForegroundColor Cyan

Start-Process powershell -ArgumentList "-NoExit", "-Command", "poetry run python `"$backendPath\manage.py`" runserver"

Start-Process powershell -ArgumentList "-NoExit", "-Command", "npm --prefix `"$frontendPath`" run dev"

Write-Host "✅ Servers launched in separate windows. Check the consoles for logs." -ForegroundColor Green

Set-Location $originalPath