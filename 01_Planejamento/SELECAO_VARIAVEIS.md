# PNAD-COVID-19: Seleção de 20 Variáveis Estratégicas

## Projeto: Análise de Comportamento Populacional e Indicadores Hospitalares na Pandemia COVID-19

**Período Analisado:** Maio, Agosto e Novembro de 2020  
**Base de Dados:** PNAD-COVID-19 (IBGE)  
**Público-Alvo:** Hospital para Planejamento de Futuro Surto

---

## 📋 Estrutura DAS 20 VARIÁVEIS SELECIONADAS

### **GRUPO 1: IDENTIFICAÇÃO E CONTEXTO (3 variáveis)**

| # | Código IBGE | Descrição | Pilar | Justificativa |
|---|---|---|---|---|
| 1 | V1013 | Mês da Entrevista | Identificação | Baseline temporal para análise evolutiva |
| 2 | UF | Unidade Federativa | Identificação | Segmentação geográfica para vulnerabilidade regional |
| 3 | A002 | Idade | Identificação | Fator crítico para severidade da COVID-19 |

---

### **GRUPO 2: SINTOMAS CLÍNICOS (5 variáveis)** ⚕️
*Foco: Sintomas que demandam internação hospitalar*

| # | Código IBGE | Descrição | Pilar | Tipo | Justificativa |
|---|---|---|---|---|---|
| 4 | B009 | Tosse | Clínico | Binário (Sim/Não) | Sintoma de infecção respiratória alta |
| 5 | B010 | Febre | Clínico | Binário (Sim/Não) | Indicador de inflamação sistêmica |
| 6 | B011 | Dificuldade de Respirar | Clínico | Binário (Sim/Não) | **Indicador crítico para internação** |
| 7 | B014 | Perda de Cheiro/Paladar | Clínico | Binário (Sim/Não) | Sintoma específico de COVID-19 |
| 8 | B019 | Procurou Estabelecimento de Saúde | Clínico/Comportamento | Binário (Sim/Não) | Indicador de gravidade e procura por atendimento |

---

### **GRUPO 3: COMPORTAMENTO POPULACIONAL (6 variáveis)** 👥
*Foco: Adesão a medidas de prevenção e isolamento social*

| # | Código IBGE | Descrição | Pilar | Tipo | Justificativa |
|---|---|---|---|---|---|
| 9 | B004 | Ficou em Casa | Comportamento | Categórico | Parâmetro β (transmissão) do modelo SEIR |
| 10 | B005 | Motivo Sair de Casa | Comportamento | Categórico | Essencialidade de deslocamento |
| 11 | C001 | Usou Máscara | Comportamento | Binário | Redução de transmissão (afeta β) |
| 12 | C002 | Álcool/Higiene | Comportamento | Binário | Medida preventiva individual |
| 13 | C012 | Visitou Estabelecimentos Fechados | Comportamento | Binário | Contato de risco |
| 14 | C013 | Visitou Parentes (Sem Isolamento) | Comportamento | Binário | Transmissão intrafamiliar |

---

### **GRUPO 4: CARACTERÍSTICAS ECONÔMICAS (4 variáveis)** 💰
*Foco: Vulnerabilidade econômica e capacidade de isolamento*

| # | Código IBGE | Descrição | Pilar | Tipo | Justificativa |
|---|---|---|---|---|---|
| 15 | D001 | Rendimento Domiciliar per Capita | Econômico | Contínuo | Capacidade de manter isolamento |
| 16 | D005 | Recebeu Auxílio Emergencial | Econômico | Binário | Indicador de vulnerabilidade |
| 17 | E002 | Densidade Domiciliar | Econômico | Contínuo | Fator de risco (S inicial no SEIR) |
| 18 | B002 | Tem Plano de Saúde | Econômico | Binário | Acesso a atendimento privado vs SUS |

---

### **GRUPO 5: DESFECHO/RECUPERAÇÃO (2 variáveis)** 📊

| # | Código IBGE | Descrição | Pilar | Tipo | Justificativa |
|---|---|---|---|---|---|
| 19 | B021 | Teve Diagnóstico de COVID | Desfecho | Binário | Confirmação oficial vs suspeita |
| 20 | B023 | Hospitalizou por COVID | Desfecho | Binário | Métrica crítica: taxa de internação por sintoma |

---

## 🔗 MAPEAMENTO PARA O MODELO SEIR

| Parâmetro SEIR | Variáveis PNAD | Cálculo |
|---|---|---|
| **β (Transmissão)** | B004, C001, C002, C012, C013 | Proporção que NÃO segue isolamento + uso de máscara |
| **σ (Incubação)** | B009, B010, B011 (período médio) | Dias até aparição de sintomas respiratórios |
| **γ (Recuperação)** | B023 (internados) vs total casos | Taxa de recuperação hospitalar |
| **S Inicial (Suscetíveis)** | E002, A002 (idade), D001 (renda) | População não exposta + vulnerabilidade |
| **Taxa de Hospitalização** | B011 + B023 | Proporção de I que necessita internação |

---

## 📊 ESPERADO: DIMENSIONAMENTO DO BANCO DE DADOS

```
Fonte: https://covid19.ibge.gov.br/pnad-covid/

Estimativa de Linhas por Mês:
- Maio 2020: ~40.000 observações
- Agosto 2020: ~42.000 observações
- Novembro 2020: ~38.000 observações

TOTAL: ~120.000 linhas × 20 colunas = BASE MANEJÁVEL EM BIGQUERY/AZURE/AWS
```

---

## ✅ PRÓXIMOS PASSOS

1. ✓ Download dos dados da PNAD-COVID-19 (formato CSV/PARQUET)
2. ✓ ETL: Filtrar 20 variáveis, 3 meses, limpar dados faltantes
3. ✓ Análise Exploratória: Distribuições, correlações, evolução temporal
4. ✓ Modelo SEIR: Calibrar parâmetros com base nos dados
5. ✓ Simulações: Cenários de novo surto com diferentes políticas de isolamento
6. ✓ Relatório: Recomendações estratégicas para o hospital

---

## 📝 Notas de Implementação

- **Banco de Dados:** Usar BigQuery, AWS S3 ou Azure SQL conforme disponibilidade
- **Linguagem:** Python (pandas, numpy, scipy) + SQL
- **Visualização:** Power BI ou Plotly para dashboards
- **Modelo:** Scipy.integrate.odeint para SEIR
