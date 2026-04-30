# SETUP E EXECUÇÃO - Guia Rápido

## Status Atual

✅ **Python:** 3.11.9  
✅ **venv:** Configurado em `.venv/`  
✅ **Dependências:** Todas instaladas  
✅ **Pipeline:** Testado e funcionando  

## Pacotes Instalados

| Pacote | Versão |
|--------|--------|
| pandas | 2.0.3 |
| matplotlib | 3.7.2 |
| seaborn | 0.12.2 |
| scipy | 1.15.3 |
| openpyxl | 3.1.5 |
| xlrd | 2.0.2 |

## Como Usar

### Opção 1: PowerShell (Recomendado)
```powershell
.\run_pipeline_venv.ps1
```

### Opção 2: Batch (Windows CMD)
```batch
run_pipeline_venv.bat
```

### Opção 3: Manual - Python direto
```bash
# Ativar venv
.venv\Scripts\activate.bat    # Windows CMD
# ou
.venv\Scripts\Activate.ps1    # PowerShell

# Rodar pipeline
python run_pipeline.py
```

### Opção 4: Passo a passo
```bash
cd 02_ETL
python etl_pnad_covid.py

cd ..\03_Analise_Exploratoria
python eda_pnad_covid.py

cd ..\04_Modelo_SEIR
python modelo_seir.py
```

## Verificar Instalação

```bash
python --version
pip list | findstr pandas scipy matplotlib
```

## Estrutura de Saídas

```
relatorios/
├── graficos/
│   ├── 01_sintomas_evolucao.png
│   ├── 02_taxa_internacao_sintomas.png
│   ├── 03_comportamento_evolucao.png
│   ├── 04_indice_transmissao_beta.png
│   ├── 05_seir_cenarios_completos.png
│   ├── 06_seir_comparacao_infectados.png
│   └── metricas_seir_cenarios.csv
│
└── metricas_seir_cenarios.csv

dados/processed/
├── pnad_covid_consolidado_maio_agosto_novembro_2020.csv
└── indicadores_agregados_por_mes.csv
```

## Troubleshooting

### Erro: "No module named 'pandas'"
```bash
pip install -r requirements.txt
```

### Erro: "venv not found"
```bash
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Erro: "Permission denied" em PowerShell
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\run_pipeline_venv.ps1
```

## Documentação Adicional

- [README.md](README.md) - Visão geral do projeto
- [CONCLUSAO.md](CONCLUSAO.md) - Mudanças realizadas
- [ESTRUTURA_PROJETO.md](ESTRUTURA_PROJETO.md) - Arquitetura técnica
- [00_LEIA_MUDANCAS.md](00_LEIA_MUDANCAS.md) - Guia de mudanças recentes
