# Script para ativar venv e rodar o pipeline
# Uso: .\run_pipeline_venv.ps1

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  PNAD-COVID-19: Pipeline com venv" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Verificar se venv existe
if (-Not (Test-Path ".venv\Scripts\Activate.ps1")) {
    Write-Host "[ERRO] venv nao encontrado. Execute:" -ForegroundColor Red
    Write-Host "   python -m venv .venv" -ForegroundColor Yellow
    Write-Host "   .venv\Scripts\activate.bat" -ForegroundColor Yellow
    Write-Host "   pip install -r requirements.txt" -ForegroundColor Yellow
    exit 1
}

# Ativar venv
Write-Host "[INFO] Ativando venv..." -ForegroundColor Cyan
& .venv\Scripts\Activate.ps1

# Verificar Python
Write-Host "[OK] Python $(python --version)" -ForegroundColor Green

# Rodar pipeline
Write-Host "`n[INFO] Iniciando pipeline...`n" -ForegroundColor Cyan
python run_pipeline.py

Write-Host "`n========================================" -ForegroundColor Green
Write-Host "  Pipeline finalizado com sucesso!" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Green
