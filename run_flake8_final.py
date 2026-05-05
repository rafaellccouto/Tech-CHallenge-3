#!/usr/bin/env python3
"""Script para gerar relatório final de flake8"""
import subprocess
import sys

files = [
    'run_pipeline.py',
    'summary.py',
    '02_ETL/etl_pnad_covid.py',
    '03_Analise_Exploratoria/eda_pnad_covid.py',
    '04_Modelo_SEIR/modelo_seir.py'
]

result = subprocess.run(
    [sys.executable, '-m', 'flake8'] + files,
    capture_output=True,
    text=True
)

with open('flake_report_final.txt', 'w') as f:
    f.write(result.stdout)

print(f"Relatório salvo em: flake_report_final.txt")
print(f"Total de problemas: {len(result.stdout.splitlines())}")
if result.stdout:
    print("\nPrimeiros 20 problemas:")
    for line in result.stdout.splitlines()[:20]:
        print(line)
else:
    print("\n✓ Nenhum problema encontrado!")
