# 🚀 GUIA PASSO A PASSO: EXECUÇÃO DO PROJETO

## Fase 1: Preparação (Semana 1)

### Passo 1.1: Clonar/Baixar o Projeto
```bash
# Criar diretório
mkdir -p ~/projetos/data_lake_covid
cd ~/projetos/data_lake_covid

# Se usando Git
git clone <repositorio> .
```

### Passo 1.2: Configurar Ambiente Python

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Passo 1.3: Instalar Dependências

```bash
# Atualizar pip
pip install --upgrade pip

# Instalar requirements
pip install -r requirements.txt

# Verificar instalação
python -c "import pandas, numpy, scipy; print('✓ Dependências OK')"
```

### Passo 1.4: Criar Estrutura de Diretórios

```bash
# Criar pastas de dados
mkdir -p dados/raw
mkdir -p dados/processed
mkdir -p dados/csv_meses
mkdir -p relatorios/graficos

echo "✓ Estrutura criada"
```

---

## Fase 2: Aquisição de Dados (Semana 1)

### Passo 2.1: Download Manual do IBGE

**Via Browser:**
1. Acesse: https://covid19.ibge.gov.br/pnad-covid/
2. Clique em cada mês desejado (Maio, Agosto, Novembro)
3. Download em formato CSV
4. Salve em `dados/raw/`

**Resultado esperado:**
```
dados/raw/
├── pnad_covid_05_2020.csv
├── pnad_covid_08_2020.csv
└── pnad_covid_11_2020.csv
```

### Passo 2.2: Verificar Integridade dos Dados

```bash
# Python script para validar
python -c "
import pandas as pd
import os

for arquivo in ['05', '08', '11']:
    caminho = f'dados/raw/pnad_covid_{arquivo}_2020.csv'
    if os.path.exists(caminho):
        df = pd.read_csv(caminho, sep=';', encoding='latin-1', nrows=10)
        print(f'✓ {arquivo}: {df.shape[0]} linhas, {df.shape[1]} colunas')
    else:
        print(f'✗ {arquivo}: Arquivo não encontrado!')
"
```

---

## Fase 3: ETL - Extração, Transformação e Carga (Semana 2)

### Passo 3.1: Executar Pipeline ETL

```bash
# Navegar até pasta do ETL
cd 02_ETL

# Executar script
python etl_pnad_covid.py

# Saída esperada:
# ✓ Dados carregados: (N, 20)
# ✓ Limpeza concluída
# ✓ Base consolidada salva: dados/processed/pnad_covid_consolidado...
```

### Passo 3.2: Validar Dados Processados

```bash
# Python script
python -c "
import pandas as pd

# Verificar base consolidada
df = pd.read_csv('../dados/processed/pnad_covid_consolidado_maio_agosto_novembro_2020.csv')

print(f'Dimensões finais: {df.shape}')
print(f'\nColunas:')
print(df.columns.tolist())
print(f'\nPrimeiras linhas:')
print(df.head())
print(f'\nDados faltantes:')
print(df.isnull().sum())
"
```

### Passo 3.3: Revisar Indicadores Agregados

```bash
# Visualizar arquivo CSV
python -c "
import pandas as pd

df_ind = pd.read_csv('../dados/processed/indicadores_agregados_por_mes.csv')
print(df_ind.to_string())
"
```

---

## Fase 4: Análise Exploratória (Semana 3)

### Passo 4.1: Executar EDA

```bash
# Navegar até pasta de análise
cd ../03_Analise_Exploratoria

# Executar análise
python eda_pnad_covid.py

# Saída:
# ⚕️  ANÁLISE DE SINTOMAS CLÍNICOS
# 👥 ANÁLISE DE COMPORTAMENTO POPULACIONAL
# 💰 ANÁLISE DE VULNERABILIDADE ECONÔMICA
```

### Passo 4.2: Verificar Gráficos Gerados

```bash
# Listar arquivos gerados
ls -lah ../relatorios/graficos/

# Saída esperada:
# 01_sintomas_evolucao.png
# 02_taxa_internacao_sintomas.png
# 03_comportamento_evolucao.png
# 04_indice_transmissao_beta.png
```

### Passo 4.3: Abrir Gráficos para Revisão

```bash
# Windows
start ../relatorios/graficos/

# Linux
xdg-open ../relatorios/graficos/

# Mac
open ../relatorios/graficos/
```

---

## Fase 5: Modelo SEIR (Semana 4)

### Passo 5.1: Executar Simulações SEIR

```bash
# Navegar até pasta SEIR
cd ../04_Modelo_SEIR

# Executar modelo
python modelo_seir.py

# Saída:
# 🦠 Modelo SEIR Inicializado
# 📊 CENÁRIO 1: BASELINE...
# 📊 CENÁRIO 2: PRESSÃO...
# 📊 CENÁRIO 3: ADAPTAÇÃO...
# 📊 CENÁRIO 4: NOVO SURTO...
```

### Passo 5.2: Verificar Gráficos SEIR

```bash
# Listar novos gráficos
ls -lah ../relatorios/graficos/ | grep "0[56]_"

# Saída esperada:
# 05_seir_cenarios_completos.png
# 06_seir_comparacao_infectados.png
```

### Passo 5.3: Revisar Tabela de Métricas

```bash
# Visualizar métricas
python -c "
import pandas as pd

df_metrics = pd.read_csv('../relatorios/metricas_seir_cenarios.csv')
print(df_metrics.to_string())
"
```

---

## Fase 6: Geração de Relatórios (Semana 4)

### Passo 6.1: Verificar Documentação

```bash
# Navegar para relatórios
cd ../05_Relatorios

# Listar arquivos
ls -la

# Arquivo crítico:
# RECOMENDACOES_HOSPITAL.md ← MAIS IMPORTANTE PARA TOMADOR DE DECISÃO
```

### Passo 6.2: Compilar Relatório Executivo

**Estrutura sugerida para apresentação:**

```
1. SUMÁRIO EXECUTIVO (2 páginas)
   ├─ Contexto da análise
   ├─ Principais achados
   └─ Recomendação nº1: Dimensionar 3.000 leitos

2. ANÁLISE EXPLORATÓRIA (5 páginas)
   ├─ Sintomas prevalentes
   ├─ Comportamento populacional
   ├─ Vulnerabilidade econômica
   └─ [4 Gráficos EDA]

3. MODELO SEIR (5 páginas)
   ├─ Metodologia
   ├─ 4 Cenários simulados
   ├─ [2 Gráficos SEIR]
   └─ Tabela de Métricas

4. RECOMENDAÇÕES ESTRATÉGICAS (10 páginas)
   ├─ Pilar 1: Leitos (dimensionamento + plano ativação)
   ├─ Pilar 2: Insumos (estoque + fornecedores)
   ├─ Pilar 3: Triagem por risco (4 protocolos)
   ├─ Pilar 4: Centros isolamento (500-800 leitos)
   ├─ Pilar 5: RRHH (8.000-10.000 profissionais)
   └─ Pilar 6: Comunicação (transparência)

5. PLANO DE AÇÃO (3 páginas)
   ├─ Cronograma de implementação
   ├─ Responsáveis
   ├─ Orçamento estimado
   └─ KPIs de monitoramento
```

### Passo 6.3: Preparar Apresentação

```bash
# Copiar todos os gráficos
cp -r ../relatorios/graficos ./graficos_apresentacao/

# Criar deck PowerPoint com:
# - 6 gráficos (4 EDA + 2 SEIR)
# - Tabelas comparativas
# - Recomendações estruturadas
```

---

## Fase 7: Validação e Testes (Semana 4)

### Passo 7.1: Checklist de Qualidade

```bash
# Criar arquivo de validação
python -c "
import os
import pandas as pd

checklist = {
    'Dados Raw': os.path.exists('../dados/raw/pnad_covid_05_2020.csv'),
    'Dados Processados': os.path.exists('../dados/processed/pnad_covid_consolidado_maio_agosto_novembro_2020.csv'),
    'Gráficos EDA': len(os.listdir('../relatorios/graficos/')) >= 4,
    'Gráficos SEIR': 'seir' in str(os.listdir('../relatorios/graficos/')),
    'Arquivo Recomendações': os.path.exists('./RECOMENDACOES_HOSPITAL.md'),
}

for item, status in checklist.items():
    print(f'{"✓" if status else "✗"} {item}')
"
```

### Passo 7.2: Teste de Reproduibilidade

```bash
# Executar todo pipeline novamente
bash
cd 02_ETL && python etl_pnad_covid.py
cd ../03_Analise_Exploratoria && python eda_pnad_covid.py
cd ../04_Modelo_SEIR && python modelo_seir.py

# Se tudo rodar sem erros: ✓ Reproduível
```

---

## Fase 8: Apresentação Executiva (Semana 4)

### Passo 8.1: Preparar Apresentação para Decisores

**Timeline:** 60 minutos

| Tempo | Tópico | Responsável |
|-------|--------|-------------|
| 5 min | Contexto COVID-19 (2020) | Analista |
| 10 min | Seleção 20 Variáveis PNAD | Analista |
| 15 min | EDA: Sintomas + Comportamento | Analista |
| 10 min | Índice β (Transmissão) | Cientista de Dados |
| 15 min | Cenários SEIR (4 modelos) | Epidemiologista |
| 15 min | **Recomendações Críticas** | **Head de Dados** |
| 10 min | Q&A + Decisão | Todos |

### Passo 8.2: Key Messages para Tomador de Decisão

```
1️⃣ "Agosto 2020 foi crítico: 1.2M infectados simultâneos"
2️⃣ "Precisamos de 3.000 leitos estruturados (não 500)"
3️⃣ "Oxigênio é gargalo nº1 (estocar 5 dias de consumo)"
4️⃣ "Com mitigação agressiva, reduzimos pico em 50%"
5️⃣ "Centros de isolamento comunitário economizam R$ 1B"
6️⃣ "Dashboard em tempo real permite resposta em <3 dias"
```

---

## 📊 Dashboard de Progresso

Copie este checklist e atualize conforme avança:

```
PROGRESSO DO PROJETO:

Semana 1 (Preparação):
  ✅ Ambiente Python configurado
  ✅ Dados baixados do IBGE
  ⏳ ETL iniciado

Semana 2 (ETL):
  ⏳ Limpeza de dados
  ⏳ Base consolidada
  ⏳ Indicadores agregados

Semana 3 (Análise):
  ⏳ EDA concluída
  ⏳ 4 gráficos gerados
  ⏳ Índice β calculado

Semana 4 (SEIR + Relatórios):
  ⏳ 4 cenários SEIR simulados
  ⏳ 2 gráficos SEIR gerados
  ⏳ Recomendações documentadas
  ⏳ Apresentação preparada
```

---

## 🆘 Troubleshooting

### Erro: "Arquivo não encontrado"
```bash
# Solução: Verificar caminho
ls -la dados/raw/
# Deve conter: pnad_covid_05_2020.csv, pnad_covid_08_2020.csv, pnad_covid_11_2020.csv
```

### Erro: "Module not found"
```bash
# Solução: Reinstalar dependências
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Erro: "Dados faltantes excessivos"
```bash
# Solução: Verificar encoding do arquivo
python -c "
import pandas as pd
try:
    df = pd.read_csv('dados/raw/pnad_covid_05_2020.csv', sep=';', encoding='utf-8')
except:
    df = pd.read_csv('dados/raw/pnad_covid_05_2020.csv', sep=';', encoding='latin-1')
print(df.shape)
"
```

### Erro: "Gráficos não gerados"
```bash
# Solução: Garantir matplotlib backend
python -c "
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
"
```

---

## 📞 Contato e Suporte

Para dúvidas:
1. Consulte `05_Relatorios/ANALISE_TECNICA.md`
2. Revise logs de execução
3. Valide dados em `dados/processed/`

---

**Tempo Total Estimado:** 3-4 semanas  
**Recursos Necessários:** 1 Cientista de Dados + 1 Epidemiologista  
**Custo Computacional:** ~2GB RAM, 10GB disco
