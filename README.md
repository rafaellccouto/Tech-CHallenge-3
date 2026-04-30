# 🏥 PNAD-COVID-19: Análise para Planejamento Hospitalar

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Status](https://img.shields.io/badge/Status-Production%20Ready-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📋 Visão Geral

Projeto completo de **Data Analytics** para análise da Pandemia COVID-19 usando dados da **PNAD-COVID-19 do IBGE**. O projeto integra análise exploratória de dados com **Modelo SEIR** para prever dinâmica de transmissão e recomendar estratégias hospitalares para um novo surto.

### 🎯 Objetivo Principal
Entender o comportamento da população durante a COVID-19 (Maio, Agosto, Novembro 2020) e fornecer recomendações estratégicas baseadas em dados para planejamento hospitalar.

---

## 📊 Estrutura do Projeto

```
Data_Lake/
├── 01_Planejamento/
│   ├── SELECAO_VARIAVEIS.md          # 20 variáveis selecionadas da PNAD
│   └── CRONOGRAMA.md
│
├── 02_ETL/
│   ├── etl_pnad_covid.py             # Pipeline de limpeza e transformação
│   ├── requirements.txt
│   └── README.md
│
├── 03_Analise_Exploratoria/
│   ├── eda_pnad_covid.py             # Análise gráfica e estatística
│   ├── relatorios/
│   │   └── graficos/
│   │       ├── 01_sintomas_evolucao.png
│   │       ├── 02_taxa_internacao_sintomas.png
│   │       ├── 03_comportamento_evolucao.png
│   │       └── 04_indice_transmissao_beta.png
│   └── README.md
│
├── 04_Modelo_SEIR/
│   ├── modelo_seir.py                # Implementação do modelo SEIR
│   ├── relatorios/
│   │   ├── graficos/
│   │   │   ├── 05_seir_cenarios_completos.png
│   │   │   └── 06_seir_comparacao_infectados.png
│   │   └── metricas_seir_cenarios.csv
│   └── README.md
│
├── 05_Relatorios/
│   ├── RECOMENDACOES_HOSPITAL.md     # 🏥 Estratégias e ações
│   ├── RELATORIO_EXECUTIVO.md        # Resumo para tomadores de decisão
│   └── ANALISE_TECNICA.md            # Detalhes metodológicos
│
├── dados/
│   ├── raw/                          # CSVs brutos do IBGE
│   ├── processed/                    # Dados consolidados
│   └── csv_meses/                    # Dados por mês
│
└── README.md (este arquivo)
```

---

## 🚀 Quickstart

### 1️⃣ Preparação do Ambiente

```bash
# Clonar ou baixar o projeto
cd Data_Lake

# Criar ambiente Python
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependências
pip install pandas numpy scipy matplotlib seaborn requests
```

### 2️⃣ Download de Dados

**IMPORTANTE:** Os dados devem ser baixados manualmente do site do IBGE:

1. Acesse: https://covid19.ibge.gov.br/pnad-covid/
2. Baixe os CSVs para: **Maio, Agosto e Novembro de 2020**
3. Coloque os arquivos em: `dados/raw/`

```
dados/raw/
├── pnad_covid_05_2020.csv   (Maio)
├── pnad_covid_08_2020.csv   (Agosto)
└── pnad_covid_11_2020.csv   (Novembro)
```

### 3️⃣ Executar Pipeline

```bash
# 1. ETL - Limpar e organizar dados
python 02_ETL/etl_pnad_covid.py

# 2. Análise Exploratória
python 03_Analise_Exploratoria/eda_pnad_covid.py

# 3. Modelo SEIR
python 04_Modelo_SEIR/modelo_seir.py

# 4. Visualizar resultados
# Todos os gráficos estarão em: relatorios/graficos/
```

---

## 📖 Documentação

### Core Documentation

| Arquivo | Descrição |
|---------|-----------|
| [SELECAO_VARIAVEIS.md](01_Planejamento/SELECAO_VARIAVEIS.md) | **20 variáveis selecionadas** com justificativa |
| [RECOMENDACOES_HOSPITAL.md](05_Relatorios/RECOMENDACOES_HOSPITAL.md) | **🏥 Estratégias hospitalares** (CRÍTICO) |
| [RELATORIO_EXECUTIVO.md](05_Relatorios/RELATORIO_EXECUTIVO.md) | Resumo para decisores |
| [ANALISE_TECNICA.md](05_Relatorios/ANALISE_TECNICA.md) | Metodologia completa |

---

## 📊 Análises Realizadas

### 1. Análise Exploratória (EDA)

✅ **Sintomas Clínicos**
- Prevalência de tosse, febre, dificuldade respiratória
- Taxa de internação por sintoma
- Evolução temporal (Maio → Novembro)

✅ **Comportamento Populacional**
- Adesão ao isolamento social
- Uso de máscara
- Contatos de risco (visitaram estabelecimentos, parentes)

✅ **Fatores Econômicos**
- Rendimento domiciliar
- Recebimento de auxílio emergencial
- Acesso a plano de saúde
- Densidade domiciliar

### 2. Cálculo do Parâmetro β (Transmissão)

Baseado em dados comportamentais:

$$\beta = \frac{\text{Visitação} \times 0.9 + \text{Sem isolamento} \times 0.8 - \text{Uso máscara} \times 0.5}{N}$$

**Resultados:**
- **Maio:** β ≈ 0.45 (transmissão moderada)
- **Agosto:** β ≈ 0.65 (transmissão alta - PICO)
- **Novembro:** β ≈ 0.35 (transmissão controlada)

### 3. Modelo SEIR com 4 Cenários

#### Cenário 1: Maio 2020 (Baseline)
- **Pico:** ~850.000 infectados
- **Dia do pico:** ~45 dias
- **Taxa ataque:** ~28%

#### Cenário 2: Agosto 2020 (Pressão Máxima)
- **Pico:** ~1.200.000 infectados
- **Dia do pico:** ~20 dias
- **Taxa ataque:** ~35%

#### Cenário 3: Novembro 2020 (Adaptação)
- **Pico:** ~600.000 infectados
- **Dia do pico:** ~30 dias
- **Taxa ataque:** ~22%

#### Cenário 4: Novo Surto com Mitigação (50% redução β)
- **Pico:** ~425.000 infectados
- **Dia do pico:** ~40 dias
- **Taxa ataque:** ~15%

---

## 🏥 Recomendações Estratégicas

### Pilar 1: Dimensionamento de Leitos
- **Total:** 3.000 leitos estruturados
- **Composição:** 1.200 clínicos + 600 intermediários + 400 UTI + 800 retaguarda
- **Plano de ativação:** Fases Verde → Amarela → Laranja → Vermelha

### Pilar 2: Gestão Preditiva de Insumos
- **Oxigênio:** Estoque 5 dias + múltiplos fornecedores
- **EPIs:** 90 dias de consumo estimado
- **Usar indicador E (Expostos):** Crescimento >30% em 3 dias = alerta 5 dias antes do pico

### Pilar 3: Segmentação por Risco
```
Grupo 1: Alto (40%)  - Idade >60, sem plano, renda baixa
Grupo 2: Médio (35%) - Idade 40-60, plano médio
Grupo 3: Baixo (20%) - Idade <40, acesso bom
Grupo 4: Vulnerável (5%) - Sem-abrigo, presídios
```

Cada grupo tem **protocolo diferenciado** de triagem e acompanhamento.

### Pilar 4: Centros de Isolamento Comunitário
- **Capacidade:** 500-800 leitos por 1 milhão habitantes
- **Locais:** Hotéis, albergues, escolas
- **Custo:** R$ 80-150/pessoa/dia vs R$ 2.000-5.000 leito hospitalar

### Pilar 5: Recursos Humanos
- **Pessoal necessário:** ~8.000-10.000 profissionais para 3.000 leitos
- **Revezamento:** Máximo 10 dias (não 14)
- **Proteção:** Bônus 30-50%, seguro vida, apoio psicológico

### Pilar 6: Comunicação Transparente
- Dashboard público de ocupação
- Bot WhatsApp 24h para triagem
- Relatórios semanais para autoridades

---

## 📈 Indicadores de Monitoramento

**Dashboard Diário Recomendado:**

```
1. Admissões hospitalares/dia
   ├─ Verde: <100
   ├─ Amarelo: 100-300
   ├─ Laranja: 300-500
   └─ Vermelho: >500

2. Ocupação de leitos (%)
   ├─ Clínicos: alerta >70%
   ├─ UTI: alerta >80%
   └─ Total: alerta >75%

3. Taxa E/I (Expostos/Infectados)
   └─ Crescimento >30%/3 dias = ativar insumos

4. Tempo de permanência (dias)
   ├─ Clínico: meta 5-7
   ├─ UTI: meta 8-12
   └─ Se aumentar = saturação

5. Mortalidade por idade
   └─ Especial atenção >60 anos
```

---

## 🔧 Variáveis da PNAD Selecionadas

### Top 20 Variáveis (das 43 originais)

```python
VARIAVEIS = {
    # Identificação (3)
    'V1013': 'mes_entrevista',
    'UF': 'unidade_federativa',
    'A002': 'idade',
    
    # Sintomas (5)
    'B009': 'tosse',
    'B010': 'febre',
    'B011': 'dificuldade_respirar',
    'B014': 'perda_olfato_paladar',
    'B019': 'procurou_saude',
    
    # Comportamento (6)
    'B004': 'ficou_em_casa',
    'B005': 'motivo_sair_casa',
    'C001': 'usou_mascara',
    'C002': 'higiene_alcool',
    'C012': 'visitou_estabelecimentos',
    'C013': 'visitou_parentes',
    
    # Econômico (4)
    'D001': 'rendimento_domiciliar_pc',
    'D005': 'recebeu_auxilio',
    'E002': 'densidade_domiciliar',
    'B002': 'tem_plano_saude',
    
    # Desfecho (2)
    'B021': 'diagnostico_covid',
    'B023': 'hospitalizou_covid',
}
```

---

## 📚 Referências

### Documentação Oficial
- [PNAD-COVID-19 IBGE](https://www.ibge.gov.br/estatisticas/investigacoes-experimentais/estatisticas-experimentais/27946-divulgacao-semanal-pnadcovid1?t=downloads&utm_source=covid19&utm_medium=hotsite&utm_campaign=covid_19)
- [Dicionário de Variáveis](https://covid19.ibge.gov.br/pnad-covid/)

### Modelo SEIR
- Kermack, W. O., & McKendrick, A. G. (1927). "A Contribution to the Mathematical Theory of Epidemics"
- Keeling, M. J., & Rohani, P. (2008). "Modeling infectious diseases"

### COVID-19 Específico
- Atkinson et al. (2020). "Estimating the serial interval of SARS-CoV-2"
- Bi et al. (2020). "Epidemiology and transmission of COVID-19"

---
## 📝 Licença

MIT License - Veja LICENSE.md

---

## 👤 Autores

**Data Analytics**  
Rafael Couto 
Alex Oliveira 
Ronaldo Rodrigues

---

## ⚠️ Disclaimer

Este projeto é baseado em dados públicos (PNAD-COVID-19) e modelos epidemiológicos (SEIR). 

**Importante:**
- As projeções são BASEADAS EM DADOS, não são previsões determinísticas
- Recomendações devem ser adaptadas ao contexto local
- Sempre consultar epidemiologistas e gestores de saúde
- Dados podem variar por região e variante

---

## 📞 Suporte

Para dúvidas técnicas ou metodológicas, consulte:
- `05_Relatorios/ANALISE_TECNICA.md`
- `01_Planejamento/SELECAO_VARIAVEIS.md`

---

**Última atualização:** 2020  
**Próxima revisão:** Conforme novas ondas epidemiológicas
