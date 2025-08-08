Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Redis Semantic Cache Web Demo" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Starting Flask web application..." -ForegroundColor Green
Write-Host "Open your browser to: http://localhost:5000" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Red
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

& "C:/Users/Souvik.Misra/OneDrive - ConnectWise, Inc/Desktop/mcp/redis-semantic-cache/redis-searchenv/Scripts/python.exe" app.py

Read-Host "Press Enter to continue..."
