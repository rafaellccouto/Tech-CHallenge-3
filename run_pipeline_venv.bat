@echo off
REM Script para ativar venv e rodar o pipeline
REM Uso: run_pipeline_venv.bat

echo.
echo ========================================
echo  PNAD-COVID-19: Pipeline com venv
echo ========================================
echo.

REM Ativar venv
call .venv\Scripts\activate.bat

REM Rodar pipeline
echo.
echo Iniciando pipeline...
echo.
python run_pipeline.py

echo.
echo Pipeline finalizado!
echo.
pause
