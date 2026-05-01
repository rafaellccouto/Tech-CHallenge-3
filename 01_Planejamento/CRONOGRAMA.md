# 📅 CRONOGRAMA DETALHADO: PNAD-COVID-19 ANALYSIS

## Linha do Tempo

```
PLANEJAMENTO E PREPARAÇÃO
│
├─ Setup Técnico
│  ├─ Python env + dependências
│  ├─ Download PNAD-COVID-19 (Maio, Ago, Nov)
│  ├─ Validar integridade dados
│  ├─ Documentação técnica lida por analistas
│  └─ Teste de pipeline (versão piloto)
│
├─ ETL E ORGANIZAÇÃO
│  ├─ Executar etl_pnad_covid.py (completo)
│  ├─ Validar base consolidada (120K registros)
│  ├─ Indicadores agregados por mês calculados
│  ├─ Revisão de dados com epidemiologista
│  └─ Base pronta para análise 
│
├─ ANÁLISE EXPLORATÓRIA
│  ├─ Executar eda_pnad_covid.py
│  ├─ Gráficos 01-04 gerados + validados
│  ├─ Análise de sintomas concluída
│  ├─ Cálculo de parâmetro β (transmissão)
│  └─ Resultados EDA documentados
│
├─ MODELO SEIR
│  ├─ Executar modelo_seir.py (v1)
│  ├─ Simulações dos 4 cenários concluídas
│  ├─ Gráficos 05-06 gerados
│  ├─ Validação do modelo com dados reais
│  └─ Métricas SEIR finalizadas (CSV)
│
├─ RELATÓRIOS E DOCUMENTAÇÃO
│  ├─ ANALISE_TECNICA.md escrito
│  ├─ RECOMENDACOES_HOSPITAL.md estruturado
│  ├─ RELATORIO_EXECUTIVO.md para decisores
│  ├─ Revisão cruzada de documentação
│  └─ Todos relatórios finalizados
│
└─ APRESENTAÇÃO EXECUTIVA
   ├─ Preparar deck PowerPoint   ├
   ├─ Ajustes finais

```

## 📊 GANTT CHART (Textual)

```
ATIVIDADE                    
─────────────────────────────────────────────────────────────────
Setup Técnico                   ████
ETL                                ████
EDA                                   ████
Modelo SEIR                             ████
Relatórios                               ████
Apresentação                              ████
Sistemas & Dashboard                       ────────────
Validação & GO-LIVE                                  ────
```

---

## 🎯 MILESTONES CRÍTICOS

### Milestone 1: Dados Consolidados
```
✓ Base PNAD unificada (120.000 registros)
✓ 20 variáveis selecionadas
✓ 3 meses (Maio, Agosto, Novembro)
✓ Qualidade validada
```

**Entregável:** `dados/processed/pnad_covid_consolidado...csv`

---

### Milestone 2: Análises Concluídas
```
✓ EDA: Sintomas, comportamento, economia
✓ Parâmetro β calculado (0.45 → 0.65 → 0.35)
✓ 4 gráficos de análise
✓ Modelo SEIR validado
✓ 2 gráficos SEIR
✓ Cenários simulados
```

**Entregáveis:** 6 gráficos + 3 CSVs

---


## 📋 DOCUMENTOS GERADOS CRONOGRAMA
```

```
*ETL  
- `dados/processed/pnad_covid_consolidado...csv`

Análise  
- 6 gráficos PNG (300 DPI)
- `relatorios/metricas_seir_cenarios.csv`

Relatórios  
- `ANALISE_TECNICA.md` 
- `RECOMENDACOES_HOSPITAL.md` 
- `RELATORIO_EXECUTIVO.md` 

---

## ⚠️ CRITICAL PATH

Caminho crítico (não pode atrasar):

```
Aprovação → ETL → EDA → SEIR → Recomendações → Apresentação     
     │
     └──→ Infraestrutura → Suprimentos → Validação           
                ↓
              ATRASO AQUI = ATRASO FINAL
```

---

## ✅ PRÉ-REQUISITOS PARA INÍCIO

- [ ] Dados PNAD-COVID-19 disponíveis (Maio, Ago, Nov 2020)
- [ ] Ambiente Python + servidor preparado
- [ ] Acesso a dados históricos hospitalar 

---
**Versão:** 1.0  
**Data:** 2026  
**Atualizado:** Conforme progresso real
