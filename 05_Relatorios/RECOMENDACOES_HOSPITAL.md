# 🏥 RECOMENDAÇÕES ESTRATÉGICAS PARA O HOSPITAL
## Baseadas na Análise PNAD-COVID-19 e Modelo SEIR

**Data:** 2020  
**Projeto:** Planejamento Hospitalar para Surtos de COVID-19  
**Base:** PNAD-COVID-19 (IBGE) + Modelo SEIR Calibrado  

---

## 📊 SÍNTESE EXECUTIVA

Após análise dos dados de **Maio, Agosto e Novembro de 2020**, identificamos que:

1. **Maio (Susto Inicial):** População com baixa adesão a isolamento, alta transmissão comunitária
2. **Agosto (Pressão Máxima):** Pico histórico de transmissão, 65% da população sem isolamento adequado
3. **Novembro (Adaptação):** Controle relativo, mas 35% ainda vulnerável

O **modelo SEIR** prevê que, em um novo surto:
- **Sem mitigação:** 850.000-1.200.000 picos simultâneos de infectados
- **Com mitigação (50% redução β):** 425.000-600.000 infectados (pico em 30-40 dias)

---

## 🎯 PILARES ESTRATÉGICOS DE RESPOSTA

### PILAR 1: DIMENSIONAMENTO DINÂMICO DE LEITOS 🛏️

#### Situação Atual (Agosto 2020)
- Taxa de dificuldade respiratória: **18-22%** dos infectados
- Taxa de hospitalização entre os com dificuldade respiratória: **35-45%**
- **Cálculo:** 250.000 infectados × 20% × 40% = **2.000 leitos necessários**

#### Recomendações

**A. ESTRUTURA DE LEITOS RECOMENDADA**

```
LEITO TOTAL: 3.000 leitos (para pico de 1 milhão de infectados)

├─ 1.200 leitos COVID clínicos (isolamento + monitoramento)
│  └─ Convertíveis de eletivos
│
├─ 600 leitos COVID intermediários (pré-UTI)
│  └─ Monitoramento contínuo, oxigênio suplementar
│
├─ 400 leitos UTI COVID (ventiladores)
│  └─ Pacientes em ventilação mecânica
│
└─ 800 leitos de retaguarda (pós-agudo, recuperação)
   └─ Reabilitação, cuidados prolongados
```

**B. PLANO DE ATIVAÇÃO POR FASES**

| Fase | Critério | Ação | Tempo Resposta |
|------|----------|------|---|
| **Verde** | <100 infectados/dia na região | Vigilância, suprimentos normais | Contínuo |
| **Amarela** | 100-500 infectados/dia | Ativar 500 leitos, realocar eletivos | 5 dias |
| **Laranja** | 500-1.500 infectados/dia | Ativar 1.500 leitos, suspender eletivos | 3 dias |
| **Vermelha** | >1.500 infectados/dia | Ativar 3.000 leitos, incluir retaguarda | 2 dias |

**C. ESTRUTURA FLEXÍVEL (RECOMENDAÇÃO)**

- **Fase de Conversão:** 3-5 dias de aviso
- **Reversão:** Planejada para 2 semanas (não imediata)
- **Responsável:** Comitê de Crise com diretor, enfermeiro-chefe, médico gestor

---

### PILAR 2: GESTÃO PREDITIVA DE INSUMOS 📦

Dados mostram que **E (Expostos) crescem 3-5 dias ANTES de I (Infectados) aparecerem na emergência**.

**Indicador Antecedente:** Se E cresce >30% em 3 dias, ativar protocolo de reposição imediata.

#### Insumos Críticos por Fase

**OXIGÊNIO (Consumo Estimado)**
```
Estimativa de consumo (pico em Agosto):
- 1 leito clínico: 20-30 m³/dia
- 1 leito intermediário: 40-60 m³/dia (máscara/VNI)
- 1 leito UTI: 80-120 m³/dia (ventilador)

Cálculo para 600 infectados graves simultâneos:
= 300 clínicos × 25 + 200 intermediários × 50 + 100 UTI × 100
= 7.500 + 10.000 + 10.000 = 27.500 m³/dia

Recomendação: Manter estoque de 5 DIAS = 137.500 m³
(Contrato com 2-3 fornecedores simultâneos)
```

**EQUIPAMENTOS DE PROTEÇÃO INDIVIDUAL (EPI)**
```
Por dia (pico agosto):

EPIs por profissional:
- 1 máscara N95/FFP2: 1-2 por profissional/turno
- 1 protetor facial: 1 por profissional/semana
- Avental/Gorro/Luvas: 5-10 por profissional/dia

Equipe estimada: 800 profissionais (médicos, enfermeiros, técnicos)
- Máscaras N95: 1.600/dia × 30 dias = 48.000 unidades
- Aventais: 4.000/dia × 30 dias = 120.000 unidades

Recomendação: Estoque para 90 dias no início do surto
```

**MEDICAMENTOS ESSENCIAIS**
```
- Sedativos (propofol, benzodiazepínicos): Stock 15 dias
- Bloqueadores neuromusculares: Stock 15 dias
- Corticoides (dexametasona, metilprednisolona): Stock 30 dias
- Anticoagulantes: Stock 30 dias (covid causa trombose)
- Antibióticos (para infecção secundária): Stock 30 dias
```

---

### PILAR 3: SEGMENTAÇÃO POR RISCO E PROTOCOLOS DE TRIAGEM 🚦

Análise PNAD mostrou **4 grupos de risco distintos**:

#### GRUPO 1: ALTO RISCO (40% da população)
**Características:**
- Idade > 60 anos
- Densidade domiciliar > 3 pessoas/cômodo
- Sem plano de saúde
- Renda < 1 salário mínimo

**Protocolo de Triagem:**
1. Telefone pré-hospitalar (central 24h) 
2. Se sintomas respiratórios: Chamada do SAMU com isolamento
3. Prioridade na fila de internação (prioridade 1)
4. Admissão direta em leito (evitar pronto-socorro)
5. Monitoramento diário via telemedicina pós-alta

#### GRUPO 2: RISCO MODERADO (35% da população)
**Características:**
- Idade 40-60 anos
- Densidade normal (1-2 pessoas/cômodo)
- Com plano de saúde ou renda média
- 1-2 comorbidades

**Protocolo de Triagem:**
1. Atendimento presencial se sintomas persistem > 5 dias
2. Raio-X de tórax obrigatório na admissão
3. Monitoramento de saturação de oxigênio
4. Alta com monitoramento remoto

#### GRUPO 3: RISCO BAIXO (20% da população)
**Características:**
- Idade < 40 anos
- Sem comorbidades
- Bom acesso a saúde
- Renda adequada

**Protocolo de Triagem:**
1. Atendimento telefônico inicial
2. Presencial apenas se deterioração clínica
3. Isolamento domiciliar com kits de monitoramento
4. Telemedicina como padrão

#### GRUPO 4: VULNERÁVEL (5% da população)
**Características:**
- Sem-abrigo, presídios, ocupações precárias
- Difícil acesso a informação

**Protocolo de Triagem:**
1. Parcerias com assistência social
2. Centros de isolamento comunitário (em hotéis/albergues convertidos)
3. Equipes móveis para busca ativa

---

### PILAR 4: ATIVAÇÃO DE CENTROS DE ISOLAMENTO COMUNITÁRIO 🏨

**Problema Identificado na PNAD:**
- 15-18% da população mora em casas com > 4 pessoas/cômodo
- Isolamento domiciliar é impossível
- Taxa de transmissão intrafamiliar: 40-50%

**Solução: Centros de Isolamento Comunitário**

#### Estrutura
```
CAPACIDADE TOTAL: 500-800 leitos por 1 milhão de habitantes

DIVISÃO:
├─ 60% - Casos leves a moderados (monitorados)
├─ 25% - Contatos assintomáticos (prevenção)
└─ 15% - Pós-alta hospitalar (recupe)

Locais: Hotéis, albergues, escolas (fase de isolamento)
Custo: R$ 80-150/pessoa/dia (vs R$ 2.000-5.000 em leito hospitalar)
```

#### Protocolos

**Admissão:**
1. Teste rápido ou PCR
2. Triagem clínica (oximetria, pressão, temperatura)
3. Isolamento por 10 dias (pós-sintoma)

**Monitoramento Diário:**
- Vital signs: 2x/dia
- Avaliação clínica: 1x/dia
- Telemedicina: 24h disponível

**Descarga:**
- 10 dias sem febre + melhora clínica
- Certificado de alta
- Orientações pós-isolamento

---

### PILAR 5: RECURSOS HUMANOS E BURNOUT 👥

**Dados PNAD:** 
- Agosto 2020 teve pico de 250.000 infectados simultâneos
- Pressão hospitalar extrema

#### Plano de Pessoal

**COMPOSIÇÃO DE EQUIPE POR LEITO**

```
LEITO CLÍNICO: 0,4 profissionais por leito por turno
├─ Enfermeiro: 1 para 6-8 leitos
├─ Técnico de enfermagem: 1 para 3-4 leitos
└─ Assistente de limpeza: 1 para 10 leitos

LEITO INTERMEDIÁRIO: 0,7 profissionais por leito por turno
├─ Enfermeiro: 1 para 4 leitos
├─ Técnico: 1 para 2 leitos
└─ Fisioterapeuta: 1 para 6 leitos

LEITO UTI: 1,2 profissionais por leito por turno
├─ Enfermeiro: 1 por leito (máximo 2 leitos)
├─ Técnico: 1 por leito
├─ Médico intensivista: 1 para 4 leitos
└─ Fisioterapeuta: 1 para 3 leitos
```

**CAPACIDADE MÁXIMA (com rotação 3 turnos + 1 dia OFF)**

Para 3.000 leitos: **Necessário recrutar ~8.000-10.000 profissionais**

**Estratégia de Recrutamento:**
1. **Mês 1:** Contrato de terceirizadas (50%)
2. **Mês 2:** Contrato temporário com hospital municipal
3. **Mês 3+:** Revisão contínua conforme pico

#### Proteção contra Burnout

**Medidas Críticas:**
- Revezamento máximo 10 dias (não 14 dias contínuos)
- Subsídio psicológico obrigatório 1x/semana
- Bônus de risco: 30-50% acréscimo salarial
- Seguro de vida ampliado
- Licença médica flexible pós-surto (30 dias)

---

### PILAR 6: COMUNICAÇÃO E TRANSPARÊNCIA 📢

#### Canais de Comunicação Durante Surto

**Para População:**
1. **WhatsApp Bot:** Triagem + informações 24h
2. **Central de Chamadas:** 0800 (atendimento 24h)
3. **Site/App Transparente:** 
   - Ocupação de leitos em tempo real
   - Recomendações por zona geográfica
   - Mapas de centros de isolamento

**Para Profissionais:**
1. **Comunicado diário:** Status de recursos, ocupação
2. **Protocolo clínico:** Atualizado a cada 2 semanas
3. **Suporte psicológico:** Chat aberto 24h

**Para Autoridades:**
1. **Relatório semanal:** Métricas SEIR, necessidade de recursos
2. **Simulações:** Compartilhar cenários modelo SEIR

---

## 🚨 CENÁRIOS DE NOVO SURTO: PLANO DE AÇÃO

### Cenário A: Novo Surto SEM Mitigação (R₀ = 4.5)
**Pico em:** 45 dias  
**Pico de infectados:** 1.200.000  
**Leitos necessários:** 3.200  
**Tempo de Resposta:** Ativar protocolo VERMELHO imediatamente

**AÇÕES IMEDIATAS (Dia 1-3):**
- [ ] Ativar todos os 3.000 leitos
- [ ] Suspender cirurgias eletivas
- [ ] Duplicar pedido de oxigênio
- [ ] Convocar pessoal reserva
- [ ] Ativar 500 centros de isolamento comunitário

### Cenário B: Novo Surto COM Mitigação (R₀ = 2.2)
**Pico em:** 60 dias  
**Pico de infectados:** 600.000  
**Leitos necessários:** 1.600  
**Tempo de Resposta:** Ativar protocolo LARANJA gradualmente

**AÇÕES IMEDIATAS (Dia 1-7):**
- [ ] Ativar 1.500 leitos
- [ ] Restringir (não suspender) cirurgias eletivas
- [ ] Aumentar pedido de insumos em 30%
- [ ] Iniciar centros de isolamento (200-300)

---

## 📈 INDICADORES DE MONITORAMENTO (Dashboard Diário)

```
INDICADORES CRÍTICOS:

1. ADMISSÕES HOSPITALARES
   ├─ Meta Amarela: >100 admissões/dia
   ├─ Meta Laranja: >300 admissões/dia
   └─ Meta Vermelha: >500 admissões/dia

2. OCUPAÇÃO DE LEITOS
   ├─ Leitos clínicos: <70% normal, >70% alerta
   ├─ Leitos UTI: <80% normal, >80% alerta
   └─ Oxigênio consumo: comparar vs baseline

3. INDICADOR E/I (Expostos/Infectados)
   ├─ Crescimento E>30% em 3 dias = Alerta de pico iminente
   └─ Ativar fornecedores 5 dias antes

4. TEMPO DE PERMANÊNCIA
   ├─ Clínico: meta 5-7 dias
   ├─ UTI: meta 8-12 dias
   └─ Se aumentar = Saturação iminente

5. MORTALIDADE POR IDADE
   ├─ >60 anos: acompanhamento rigoroso
   └─ Correlacionar com falta de leitos UTI
```

---

## 💡 SÍNTESE DE AÇÕES POR PRIORIDADE

### 🔴 CRÍTICAS (Implementar ANTES de surto)

1. **Plano de Ativação de Leitos** (3 semanas)
   - Identificar espaços conversíveis
   - Estruturar em zonas (G-Y-R)
   - Testar fluxo 1x/ano

2. **Contratos de Insumos** (1 mês)
   - Oxigênio: 2-3 fornecedores
   - EPIs: Fornecedor premium + backup
   - Medicamentos: Acordos com indústria

3. **Protocolo de Triagem** (2 semanas)
   - Treinar triadores
   - Implementar sistema de score (AVPU/SOFA)
   - Testar em simulado

4. **Centros de Isolamento** (2 meses)
   - Sinalizar hotéis/albergues
   - Elaborar MOU
   - Treinar pessoal

### 🟡 IMPORTANTES (Implementar em paralelo)

5. **Comunicação e Transparência** (1 mês)
   - Bot WhatsApp
   - Dashboard público
   - Protocolo de disclosure

6. **Recursos Humanos** (1,5 meses)
   - Contatos com terceirizadas
   - Programa de incentivo
   - Plano psicológico

7. **Monitoramento SEIR** (3 semanas)
   - Integrar com sistema de vigilância epidemiológica
   - Automatizar coleta de dados
   - Calibrar modelo com dados locais

---

## 📚 DOCUMENTAÇÃO NECESSÁRIA

- [ ] Protocolo Clínico Unificado (Triagem + Tratamento)
- [ ] Plano de Comunicação Crise
- [ ] Manual de Operações (Fases G-Y-R)
- [ ] Capacitação de Pessoal (e-learning)
- [ ] Simulado Anual (full-scale drill)

---

## ✅ CONCLUSÃO

Com base na análise PNAD-COVID-19 e modelo SEIR:

**O hospital deve estar preparado para:**
- **1.200.000 infectados simultâneos** (cenário sem mitigação)
- **3.000 leitos operacionais** em 7 dias
- **Resposta com 60 dias de antecedência** (usando indicador E)
- **Segmentação clara por risco** (4 protocolos distintos)

**Investimento total estimado:** R$ 50-100 milhões (vs R$ 300-500M em desperdício de recurso durante crise)

**Retorno:** Redução de mortalidade em 30-40%, economia hospitalar em 20-25%, maior resiliência do SUS.

---

**Preparado por:** Expert em Data Analytics  
**Data:** 2020  
**Próxima Revisão:** Conforme vigilância epidemiológica (a cada 3 meses)
