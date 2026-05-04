# 📅 CRONOGRAMA DETALHADO: PNAD-COVID-19 ANALYSIS

## Linha do Tempo: 12 Semanas

```
SEMANA 1-2: PLANEJAMENTO E PREPARAÇÃO
│
├─ SEMANA 1: Aprovação e Kickoff
│  ├─ Seg 01: Apresentar ao Conselho
│  ├─ Ter 02: Obter aprovação orçamentária (R$ 80-120M)
│  ├─ Qua 03: Designar responsáveis
│  ├─ Qui 04: Primeira reunião comitê de crise
│  └─ Sex 05: Comunicação interna iniciada
│
├─ SEMANA 2: Setup Técnico
│  ├─ Seg 08: Python env + dependências
│  ├─ Ter 09: Download PNAD-COVID-19 (Maio, Ago, Nov)
│  ├─ Qua 10: Validar integridade dados
│  ├─ Qui 11: Documentação técnica lida por analistas
│  └─ Sex 12: Teste de pipeline (versão piloto)
│
├─ SEMANA 3: ETL E ORGANIZAÇÃO
│  ├─ Seg 15: Executar etl_pnad_covid.py (completo)
│  ├─ Ter 16: Validar base consolidada (120K registros)
│  ├─ Qua 17: Indicadores agregados por mês calculados
│  ├─ Qui 18: Revisão de dados com epidemiologista
│  └─ Sex 19: Base pronta para análise (GO)
│
├─ SEMANA 4: ANÁLISE EXPLORATÓRIA
│  ├─ Seg 22: Executar eda_pnad_covid.py
│  ├─ Ter 23: Gráficos 01-04 gerados + validados
│  ├─ Qua 24: Análise de sintomas concluída
│  ├─ Qui 25: Cálculo de parâmetro β (transmissão)
│  └─ Sex 26: Resultados EDA documentados
│
├─ SEMANA 5: MODELO SEIR
│  ├─ Seg 29: Executar modelo_seir.py (v1)
│  ├─ Ter 30: Simulações dos 4 cenários concluídas
│  ├─ Qua 01: Gráficos 05-06 gerados
│  ├─ Qui 02: Validação do modelo com dados reais
│  └─ Sex 03: Métricas SEIR finalizadas (CSV)
│
├─ SEMANA 6: RELATÓRIOS E DOCUMENTAÇÃO
│  ├─ Seg 05: ANALISE_TECNICA.md escrito
│  ├─ Ter 06: RECOMENDACOES_HOSPITAL.md estruturado
│  ├─ Qua 07: RELATORIO_EXECUTIVO.md para decisores
│  ├─ Qui 08: Revisão cruzada de documentação
│  └─ Sex 09: Todos relatórios finalizados
│
└─ SEMANA 7: APRESENTAÇÃO EXECUTIVA
   ├─ Seg 12: Preparar deck PowerPoint
   ├─ Ter 13: Ensaio de apresentação
   ├─ Qua 14: Ajustes finais
   ├─ Qui 15: Apresentação para Conselho/Direção
   └─ Sex 16: Feedback e aprovação para implementação


SEMANA 8-12: IMPLEMENTAÇÃO (PARALELO)
│
├─ SEMANA 8: INFRAESTRUTURA
│  ├─ Seg 19: Audit hospitalar (capacidade atual)
│  ├─ Ter 20: Identificar 1.200 leitos clínicos conversíveis
│  ├─ Qua 21: Identificar 600 leitos intermediários
│  ├─ Qui 22: Identificar 400 leitos UTI
│  └─ Sex 23: Plano de conversão documentado
│
├─ SEMANA 9: CADEIA DE SUPRIMENTOS
│  ├─ Seg 26: Contato com fornecedores oxigênio (3+)
│  ├─ Ter 27: Assinar contratos (5 dias estoque)
│  ├─ Qua 28: Pedido EPIs iniciado (90 dias consumo)
│  ├─ Qui 29: Verificar estoque medicamentos críticos
│  └─ Sex 30: Fornecimento garantido até mês 6
│
├─ SEMANA 10: RECURSOS HUMANOS
│  ├─ Seg 02: Contato com 3-5 terceirizadas
│  ├─ Ter 03: Assinatura MOUs (standby contracts)
│  ├─ Qua 04: Programa incentivo desenhado (+30-50%)
│  ├─ Qui 05: Comunicação de oportunidade para pessoal
│  └─ Sex 06: 100-200 profissionais em standby
│
├─ SEMANA 11: SISTEMAS E COMUNICAÇÃO
│  ├─ Seg 09: Dashboard MVP desenvolvido
│  ├─ Ter 10: Integração com sistema de vigilância
│  ├─ Qua 11: Testes de carga do dashboard
│  ├─ Qui 12: Protocolo clínico unificado finalizado
│  └─ Sex 13: Triagem por risco (4 níveis) pronta
│
└─ SEMANA 12: VALIDAÇÃO E GO-LIVE
   ├─ Seg 16: Simulado Full-Scale (todos hospitais)
   ├─ Ter 17: Avaliação e ajustes
   ├─ Qua 18: Aprovação regulatória obtida
   ├─ Qui 19: Comunicado à população / governo
   └─ Sex 20: GO-LIVE - Sistema pronto para vigilância contínua
```

---

## 📊 GANTT CHART (Textual)

```
ATIVIDADE                    SEMANA 1-3    4-6      7-9      10-12
─────────────────────────────────────────────────────────────────
Aprovação & Kickoff          ████
Setup Técnico                   ████
ETL                                ████
EDA                                   ████
Modelo SEIR                             ████
Relatórios                               ████
Apresentação                              ████
Infraestrutura                              ────────────
Suprimentos                                 ────────────
RH & Pessoal                                ────────────
Sistemas & Dashboard                       ────────────
Validação & GO-LIVE                                  ────
```

---

## 🎯 MILESTONES CRÍTICOS

### Milestone 1: Dados Consolidados (Dia 21)
```
✓ Base PNAD unificada (120.000 registros)
✓ 20 variáveis selecionadas
✓ 3 meses (Maio, Agosto, Novembro)
✓ Qualidade validada
```

**Responsável:** Cientista de Dados  
**Entregável:** `dados/processed/pnad_covid_consolidado...csv`

---

### Milestone 2: Análises Concluídas (Dia 40)
```
✓ EDA: Sintomas, comportamento, economia
✓ Parâmetro β calculado (0.45 → 0.65 → 0.35)
✓ 4 gráficos de análise
✓ Modelo SEIR validado
✓ 2 gráficos SEIR
✓ Cenários simulados
```

**Responsável:** Cientista de Dados + Epidemiologista  
**Entregáveis:** 6 gráficos + 3 CSVs

---

### Milestone 3: Decisão (Dia 45)
```
✓ Apresentação executiva para Conselho
✓ Aprovação de 3.000 leitos estruturados
✓ Aprovação de orçamento (R$ 80-120M)
✓ Designação de responsáveis por pilar
✓ Comunicação à rede hospitalar
```

**Responsável:** Head de Dados + Diretor Hospital  
**Entregável:** Aprovação em Ata

---

### Milestone 4: Estrutura Pronta (Dia 60)
```
✓ Mapa de leitos conversíveis identificado
✓ Contratos oxigênio assinados
✓ MOUs com hotéis/albergues assinadas
✓ Terceirizadas sob contrato standby
✓ Dashboard MVP desenvolvido
```

**Responsável:** Gestor Hospitalar + Procurador  
**Entregável:** Documentos assinados

---

### Milestone 5: Simulado Bem-Sucedido (Dia 70)
```
✓ Ativação de 500 leitos em <48h
✓ Pessoal respondeu adequadamente
✓ Dashboard funcionou (tempo real)
✓ Fluxo de pacientes testado
✓ Ajustes finalizados
```

**Responsável:** Comitê de Crise + Direção Clínica  
**Entregável:** Relatório de simulado

---

### Milestone 6: GO-LIVE (Dia 84)
```
✓ Sistema de vigilância 24/7 ativo
✓ Dashboard público atualizando
✓ Protocolos clínicos publicados
✓ Pessoal treinado
✓ Fornecedores validados
✓ PRONTO PARA NOVO SURTO
```

**Responsável:** Head de Dados + Secretário Saúde  
**Entregável:** Declaração de readiness

---

## 👥 ATRIBUIÇÃO POR FUNÇÃO

### Head de Dados (Responsável Geral)
```
Semana 1:   Apresentação + aprovação
Semana 2-3: Supervisão técnica
Semana 4-7: Validação análises + recomendações
Semana 8-12: Coordenação implementação
```

### Cientista de Dados (2x)
```
Semana 2-3: ETL completo
Semana 4-5: EDA + SEIR
Semana 6:   Documentação técnica
Semana 8-12: Ajustes modelo em tempo real
```

### Epidemiologista
```
Semana 3:   Revisão dados
Semana 5:   Validação modelo SEIR
Semana 6:   Recomendações clínicas
Semana 8-12: Calibração em tempo real
```

### Gestor Hospitalar
```
Semana 1:   Planejamento infraestrutura
Semana 8-9: Contatos fornecedores
Semana 10:  Revisão RH
Semana 11-12: Validação simulado
```

### Diretor Clínico
```
Semana 7:   Apresentação + aprovação
Semana 10-11: Protocolo clínico
Semana 12:  Assinatura final
```

### Secretário de Saúde
```
Semana 1:   Aprovação política
Semana 7:   Apresentação + decisão
Semana 12:  Comunicado à população
```

---

## 💰 ALOCAÇÃO DE RECURSOS

### Budget por Fase

| Fase | Semanas | Item | Custo | Total |
|------|---------|------|-------|-------|
| Prep | 1-2 | Pessoal + consultoria | R$ 5M | R$ 5M |
| Análise | 3-6 | Computação + software | R$ 2M | R$ 7M |
| Implementação | 8-12 | Infraestrutura + contratos | R$ 73-118M | R$ 80-125M |
| **TOTAL** | 12 | - | - | **R$ 87-132M** |

### FTE (Full-Time Equivalent) Alocado

```
Cientista Dados (2):     100% × 12 semanas = 24 FTE
Epidemiologista (1):     80% × 12 semanas = 9.6 FTE
Gestor Hospitalar (1):   100% × 12 semanas = 12 FTE
Head de Dados (1):       100% × 12 semanas = 12 FTE
Diretor Clínico (0.5):   50% × 12 semanas = 6 FTE
─────────────────────────────────────────────────────
TOTAL:                                      ~63.6 FTE
(ou ~0.5-1 time dedicado)
```

---

## 📋 DOCUMENTOS GERADOS CRONOGRAMA

### Por Semana

**Semana 1-2:** Kickoff  
- Ata de aprovação  
- Termo de referência

**Semana 3:** ETL  
- `dados/processed/pnad_covid_consolidado...csv`

**Semana 4-5:** Análise  
- 6 gráficos PNG (300 DPI)
- `relatorios/metricas_seir_cenarios.csv`

**Semana 6:** Relatórios  
- `ANALISE_TECNICA.md` (50 páginas)
- `RECOMENDACOES_HOSPITAL.md` (40 páginas)
- `RELATORIO_EXECUTIVO.md` (15 páginas)

**Semana 7:** Apresentação  
- PowerPoint deck (50 slides)
- Folheto executivo (4 páginas)

**Semana 8-12:** Implementação  
- Plano infraestrutura
- Contratos (oxigênio, hotéis, pessoal)
- Protocolo clínico
- Manual de dashboard
- Relatório simulado
- Declaração de readiness

---

## ⚠️ CRITICAL PATH

Caminho crítico (não pode atrasar):

```
Aprovação → ETL → EDA → SEIR → Recomendações → Apresentação
  (Dia 2)   (15)   (35)  (50)      (60)          (45)
     │
     └──→ Infraestrutura → Suprimentos → Validação
           (Dia 5)           (Dia 40)      (Dia 70)
                ↓
              ATRASO AQUI = ATRASO FINAL
```

Se **ETL atrasar 1 semana** → Todo projeto atrasa 1 semana  
Se **Aprovação atrasar 2 semanas** → Implementação atrasa 2 semanas

**Recomendação:** Paralelizar Semanas 8-12 (não esperar tudo pronto)

---

## 📞 DEFINIÇÃO DO SUCESSO

### Semana 6: Sucesso Analítico
- ✅ Base de dados consolidada (120K registros)
- ✅ Todos os gráficos gerados
- ✅ Modelo SEIR validado (erro < 10%)
- ✅ Documentação completa

### Semana 7: Sucesso de Comunicação
- ✅ Conselho aprova 3.000 leitos
- ✅ Budget de R$ 80-120M aprovado
- ✅ Comunicação clara de risco

### Semana 12: Sucesso de Implementação
- ✅ 3.000 leitos estruturados
- ✅ Oxigênio estocado (5 dias)
- ✅ Pessoal em standby
- ✅ Dashboard 24/7
- ✅ Simulado bem-sucedido
- ✅ **PRONTO PARA NOVO SURTO**

---

## 🚨 CENÁRIOS DE RISCO

### Risco 1: ETL Falha (Semana 3)
```
Probabilidade: Baixa (dados públicos, validados)
Impacto: Alto (atrasa tudo)
Mitigação: Ter especialista SQL disponível
Contingência: Usar base alternativa ou re-download
```

### Risco 2: Aprovação Política Atrasa (Semana 7)
```
Probabilidade: Média (dependência política)
Impacto: Alto (atrasa implementação)
Mitigação: Engajamento desde semana 1
Contingência: Pedir aprovação por fases
```

### Risco 3: Fornecedores Indisponíveis (Semana 9)
```
Probabilidade: Média (mercado tenso)
Impacto: Alto (crítico para oxigênio)
Mitigação: Contatar 3-5 fornecedores, assinar rápido
Contingência: Fornecedores estatais como backup
```

### Risco 4: Pessoal Insuficiente (Semana 10)
```
Probabilidade: Média (mercado de RH tenso)
Impacto: Crítico (saturam leitos)
Mitigação: Incentivo +50%, comunicar cedo
Contingência: Combinar com universidades + reformados
```

---

## ✅ PRÉ-REQUISITOS PARA INÍCIO

- [ ] Dados PNAD-COVID-19 disponíveis (Maio, Ago, Nov 2020)
- [ ] Equipe técnica de 2+ cientistas dados
- [ ] 1 Epidemiologista disponível
- [ ] Aprovação política + orçamentária
- [ ] Ambiente Python + servidor preparado
- [ ] Acesso a dados históricos hospitalar (validação)

---

## 📌 RESUMO EXECUTIVO CRONOGRAMA

| Fase | Semanas | Foco | Entreg | Status |
|------|---------|------|--------|--------|
| Prep | 1-2 | Aprovação | Ata | Kickoff |
| Tech | 3-6 | Análise | Relatórios | Core |
| Exec | 7 | Apresentação | Aprovação | Gate |
| Impl | 8-12 | Implementação | Sistema | GO-LIVE |

**Total:** 12 semanas = ~3 meses (conforme especificação do projeto)  
**Custo:** R$ 80-130M (preparação + implementação)  
**Resultado:** Hospital preparado para responder a novo surto em <48h

---

**Versão:** 1.0  
**Data:** 2020  
**Atualizado:** Conforme progresso real
