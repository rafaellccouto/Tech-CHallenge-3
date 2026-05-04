# ❓ FAQ E DICAS PRÁTICAS

## Perguntas Frequentes

### 🔧 TÉCNICAS

#### P1: Como inicio o projeto do zero?
**R:** Siga em ordem:
1. Leia `README.md` (5 min)
2. Leia `GUIA_EXECUCAO.md` (30 min)
3. Setup Python: `python -m venv venv && pip install -r requirements.txt`
4. Execute `python 02_ETL/etl_pnad_covid.py`
5. Pronto para análise

#### P2: Preciso dos dados originais do IBGE ou posso usar dados simulados?
**R:** **DEVE SER ORIGINAL**. O projeto é validado com dados reais da PNAD-COVID-19.

Passos:
1. Acesse: https://covid19.ibge.gov.br/pnad-covid/
2. Selecione: Maio, Agosto, Novembro 2020
3. Download em CSV
4. Coloque em `dados/raw/`

Se não conseguir, posso criar script de simulação (mock data) para testes.

#### P3: Qual versão Python preciso?
**R:** Python 3.8 ou superior
```bash
python --version
# Esperado: Python 3.8.X, 3.9.X, 3.10.X, 3.11.X
```

#### P4: Quanto tempo leva para rodar tudo?
**R:** 
- ETL: 5-10 minutos
- EDA: 5-8 minutos
- SEIR: 3-5 minutos
- **Total: ~15 minutos**

(Primeira execução pode ser mais lenta enquanto baixa bibliotecas)

#### P5: Posso rodar em Windows? Linux? Mac?
**R:** SIM para todos. Apenas ajuste:
- **Windows:** `venv\Scripts\activate`
- **Linux/Mac:** `source venv/bin/activate`

Resto do código é 100% compatível.

#### P6: Posso usar Google Colab?
**R:** SIM! Colab é ideal:
```python
# No Colab:
!pip install pandas numpy scipy matplotlib seaborn
# Rest of code runs the same
```

---

### 📊 DADOS

#### P7: O que fazer se os dados do IBGE tiverem encoding diferente?
**R:** O script ETL trata automaticamente:
```python
# Tenta UTF-8 primeiro, depois Latin-1
try:
    df = pd.read_csv(arquivo, sep=';', encoding='utf-8')
except:
    df = pd.read_csv(arquivo, sep=';', encoding='latin-1')
```

Se ainda houver problema:
```bash
# Converter arquivo para UTF-8
iconv -f LATIN1 -t UTF-8 arquivo.csv -o arquivo_utf8.csv
```

#### P8: Há dados faltantes? Como lidar?
**R:** O script detecta e relata. Para variáveis críticas (sintomas):
- Se >20% faltando: usar dropna()
- Se <5% faltando: usar forward fill
- Reportar no OUTPUT

#### P9: Preciso validar os dados antes de usar?
**R:** SIM, execute check:
```python
import pandas as pd

for arquivo in ['05', '08', '11']:
    caminho = f'dados/raw/pnad_covid_{arquivo}_2020.csv'
    df = pd.read_csv(caminho, sep=';', encoding='latin-1')
    print(f'{arquivo}: {df.shape} - colunas: {list(df.columns)[:10]}')
```

---

### 📈 ANÁLISE

#### P10: Como interpretar o índice β?
**R:**
- β = 0.35 (Novembro) → Transmissão BAIXA (isolamento funciona)
- β = 0.45 (Maio) → Transmissão MODERADA
- β = 0.65 (Agosto) → Transmissão ALTA (CRÍTICO)

**Fórmula prática:**
```
β alto = muita gente visitando + pouca máscara = R₀ alto = pico breve
β baixo = gente isolada + máscara = R₀ baixo = pico suave
```

#### P11: Qual sintoma é mais preditivo de internação?
**R:** **Dificuldade Respiratória** > Febre > Tosse

Dados PNAD mostram:
- Com dif.respirar: 40% internado
- Com febre: 10% internado
- Com tosse: 5% internado

**Use como ordem de prioridade triagem.**

#### P12: Como validar que o modelo SEIR está correto?
**R:** Checklist:
1. ✅ S + E + I + R = N (conservação de população)
2. ✅ I decresce para 0 (doença extinta)
3. ✅ Pico infectados entre 15-50 dias (plausível)
4. ✅ Taxa ataque 15-35% (COVID-19 realista)
5. ✅ R₀ entre 3-7 (literatura COVID)

Se falhar alguma, debugar.

#### P13: Como interpretar os 4 cenários SEIR?
**R:**
- **Maio:** Linha de base (primeira onda)
- **Agosto:** Pior cenário (use como estimativa máxima)
- **Novembro:** Melhor cenário (com medidas de controle)
- **Novo Surto Mitigado:** Planejamento ideal (com vacina + isolamento)

**Recomendação:** Estruturar para Agosto (pior caso).

---

### 💼 NEGÓCIO

#### P14: Como apresentar isso para o Conselho?
**R:** Use este deck (50 slides):
1. **Executive Summary** (3 slides)
   - Contexto: Agosto 2020 teve 1.2M infectados
   - Problema: Hospital não preparado
   - Solução: Estruturar 3.000 leitos

2. **Evidências Quantitativas** (5 slides)
   - Gráficos EDA (sintomas + comportamento)
   - Parâmetro β calibrado
   - Taxa internação por sintoma

3. **Modelo SEIR** (4 slides)
   - 4 cenários simulados
   - Gráficos SEIR
   - Tabela de métricas

4. **Recomendações** (15 slides)
   - 6 Pilares estratégicos
   - Cronograma 12 semanas
   - Orçamento (R$ 80-120M)

5. **ROI & Impacto** (5 slides)
   - Custo-benefício (8-14x retorno)
   - Vidas salvas (100K+)
   - Economia (R$ 800M-1.4B)

6. **Next Steps** (3 slides)
   - Aprovação orçamento
   - Implementação imediata
   - Dashboard em tempo real

#### P15: Como convencer o CFO (Financeiro) do ROI?
**R:** Mostre números:

```
INVESTIMENTO: R$ 100M
ECONOMIA IMPROVISO: R$ 800M-1.4B
GANHO LÍQUIDO: R$ 700M-1.3B
ROI: 7x-13x

MAIS IMPORTANTE:
- Sem preparação: Hospital saturas em 5 dias
- Com preparação: Hospital funciona por 6 meses

Escolha: Perder R$ 800M ou investir R$ 100M?
```

#### P16: Como vender a ideia politicamente?
**R:** Foque no seguinte:
1. **Segurança:** "Hospital preparado para qualquer surto"
2. **Economia:** "Economiza R$ 800M vs improviso"
3. **Vidas:** "Protege 100K+ vidas"
4. **Tempo:** "Resposta em 48h vs 2 semanas"
5. **Transparência:** "Dashboard público, população informada"

---

### 🏥 IMPLEMENTAÇÃO

#### P17: Por onde começo com 6 pilares?
**R:** Ordem sugerida (por criticidade):

1. **Pilar 2 (Oxigênio)** [SEMANA 1]
   - Assinar contratos HOJE
   - Oxigênio é gargalo crítico

2. **Pilar 1 (Leitos)** [SEMANA 2-3]
   - Mapear infraestrutura
   - Planejar conversão

3. **Pilar 4 (Isolamento)** [SEMANA 3-4]
   - Parcerias hotéis
   - MOUs rápidos

4. **Pilar 5 (Pessoal)** [SEMANA 4-5]
   - Contatos terceirizadas
   - Programa incentivo

5. **Pilar 3 (Triagem)** [SEMANA 5-6]
   - Protocolo clínico
   - Treinamento pessoal

6. **Pilar 6 (Comunicação)** [SEMANA 6-7]
   - Dashboard
   - Site público

#### P18: Que documentação devo distribuir?
**R:**
- **Para Conselho/Direção:** `RELATORIO_EXECUTIVO.md` (20 min leitura)
- **Para Gestores:** `RECOMENDACOES_HOSPITAL.md` (60 min)
- **Para Equipe Técnica:** `ANALISE_TECNICA.md` (90 min)
- **Para Tomador de Decisão:** PowerPoint com gráficos

#### P19: Como monitorar o progresso da implementação?
**R:** Use dashboard:
```
KPI: Leitos estruturados
Meta: 3.000 leitos (100%)
Semana 4: 500 (17%)
Semana 8: 1.500 (50%)
Semana 12: 3.000 (100%) ✅

KPI: Estoque oxigênio
Meta: 500K m³ (5 dias)
Semana 2: 200K (40%)
Semana 6: 500K (100%) ✅

KPI: Pessoal em standby
Meta: 8K-10K profissionais
Semana 6: 2K (25%)
Semana 10: 8K (80%)
Semana 12: 10K (100%) ✅
```

---

### 🆘 TROUBLESHOOTING

#### P20: "ModuleNotFoundError: No module named 'pandas'"
**R:**
```bash
pip install --upgrade pip
pip install pandas numpy scipy matplotlib seaborn
```

Se persistir:
```bash
python -m pip install pandas==1.5.3
```

#### P21: "FileNotFoundError: dados/raw/pnad_covid_05_2020.csv"
**R:** Você não baixou os dados. Faça:
1. Acesse: https://covid19.ibge.gov.br/pnad-covid/
2. Download CSV para cada mês
3. Coloque em `dados/raw/`
4. Renomeie para: `pnad_covid_05_2020.csv`, etc

#### P22: "Erro de encoding/decodificação"
**R:** O arquivo não está em UTF-8. Solução:
```bash
# Linux/Mac
iconv -f LATIN1 -t UTF-8 arquivo.csv -o arquivo_utf8.csv

# Windows (usar editor como Notepad++)
# Abrir → Converter para UTF-8 → Salvar
```

Ou deixe o script Python tratar (ele tenta UTF-8 depois Latin-1 automaticamente).

#### P23: "Os gráficos não foram salvos"
**R:** Crie diretório:
```bash
mkdir -p relatorios/graficos
```

Ou edite script para usar caminho completo:
```python
plt.savefig('./relatorios/graficos/meu_grafico.png')
```

#### P24: "Script demora muito para rodar"
**R:** Otimizações:
```python
# Reduzir amostra para teste
df = df.sample(n=10000)  # 10K linhas vs 120K

# Ou rodar apenas 1 mês
df = df[df['mes_entrevista'] == 5]  # Só Maio

# Depois rodar tudo para produção
```

---

## 💡 DICAS PRÁTICAS

### Dica 1: Use Jupyter Notebooks para Exploração
```bash
jupyter notebook

# Celula 1:
import pandas as pd
df = pd.read_csv('dados/processed/pnad_covid_consolidado...csv')
df.info()
df.describe()

# Celula 2:
df.groupby('mes_entrevista')['tosse'].mean()

# Etc...
```

### Dica 2: Version Control é Essencial
```bash
git init
git add .
git commit -m "PNAD-COVID-19 analysis - initial"
git branch -b feature/seir-refinement

# Permite rastrear mudanças e reverter se necessário
```

### Dica 3: Backup de Dados Críticos
```bash
cp dados/processed/pnad_covid_consolidado_maio_agosto_novembro_2020.csv \
   dados/backup/pnad_covid_consolidado_maio_agosto_novembro_2020_v1.csv
```

### Dica 4: Teste em Pequena Escala Primeiro
```python
# Antes de rodar em 120K registros:
df_teste = df.head(1000)  # Teste com 1K primeiros

# Se tudo OK:
df_prod = df  # Use todos os dados
```

### Dica 5: Use Print/Logging para Debug
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug(f"Dados carregados: {df.shape}")
logger.info(f"Limpeza concluída")
logger.warning(f"Dados faltantes: {df.isnull().sum()}")
logger.error(f"Falha na validação!")
```

### Dica 6: Documente Suas Mudanças
```python
"""
Modificações em eda_pnad_covid.py - v2.1

MUDANÇA 1: Adicionado filtro por idade (>18)
RAZÃO: Menores de 18 tinham dados inconsistentes
DATA: 2024-04-29

MUDANÇA 2: Alterado cálculo de β para incluir distância social
RAZÃO: Especificação atualizada do modelo SEIR
DATA: 2024-04-30

PRÓXIMA: Incluir dados de vacinação quando disponível
"""
```

### Dica 7: Integre com Ferramentas BI
```python
# Exportar para Power BI / Tableau
df.to_csv('relatorios/dashboard_dados.csv', index=False)

# Depois:
# 1. Abra Power BI/Tableau
# 2. Conecte CSV
# 3. Crie dashboard com gráficos interativos
# 4. Publique em servidor
```

### Dica 8: Mantenha Documentação Atualizada
```markdown
# Cada semana, atualize:

## Status Atual
- ETL: Completo ✅
- EDA: Completo ✅
- SEIR: 50% (validação em andamento)
- Relatórios: Iniciado

## Próximos Passos
- Finalizar validação SEIR
- Gerar relatórios finais
- Agendarpresentação

## Bloqueadores
- Nenhum no momento
```

### Dica 9: Teste Hipóteses com Dados
```python
# Hipótese 1: "Agosto teve transmissão 50% maior que Maio"
df_maio = df[df['mes_entrevista'] == 5]
df_agosto = df[df['mes_entrevista'] == 8]

beta_maio = calcular_beta(df_maio)
beta_agosto = calcular_beta(df_agosto)

aumento = ((beta_agosto - beta_maio) / beta_maio) * 100
print(f"Aumento β Maio→Agosto: {aumento:.1f}%")
# Resultado: ~45% (compatível com literatura COVID-19)
```

### Dica 10: Prepare Apresentação Iterativamente
```
Versão 1 (Dia 30): Draft com gráficos brutos
Versão 2 (Dia 35): Análise com insights
Versão 3 (Dia 40): Recomendações estratégicas
Versão 4 (Dia 43): Design final + branding
Versão 5 (Dia 44): Apresentação final para conselho
```

---

## 📚 REFERÊNCIAS RÁPIDAS

### Matplotlib Customization
```python
plt.style.use('seaborn-v0_8-darkgrid')
plt.figure(figsize=(12, 6))
plt.title('Título', fontsize=14, fontweight='bold')
plt.xlabel('Eixo X', fontsize=12)
plt.ylabel('Eixo Y', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('grafico.png', dpi=300, bbox_inches='tight')
```

### Pandas Tricks
```python
# Seleção eficiente
df_filtrado = df[df['mes_entrevista'].isin([5, 8, 11])]

# Agregação rápida
df.groupby('mes_entrevista').agg({
    'tosse': 'sum',
    'febre': 'mean',
    'idade': 'median'
})

# Pivot table
df.pivot_table(
    values='hospitalizou_covid',
    index='unidade_federativa',
    columns='mes_entrevista',
    aggfunc='mean'
)
```

### Scipy SEIR
```python
from scipy.integrate import odeint

def derivadas(y, t, beta, sigma, gamma, N):
    S, E, I, R = y
    dS_dt = -beta * S * I / N
    dE_dt = beta * S * I / N - sigma * E
    dI_dt = sigma * E - gamma * I
    dR_dt = gamma * I
    return [dS_dt, dE_dt, dI_dt, dR_dt]

solucao = odeint(derivadas, [S0, E0, I0, R0], t, 
                  args=(beta, sigma, gamma, N))
S, E, I, R = solucao.T
```

---

## 🎯 CHECKLIST FINAL

Antes de apresentar para o Conselho:

- [ ] Todos os 6 gráficos gerados e validados
- [ ] Base de dados consolidada (120K registros)
- [ ] Modelo SEIR rodou para 4 cenários
- [ ] Métricas calculadas (pico, R₀, taxa ataque)
- [ ] Documentação completa (técnica + executiva)
- [ ] Relatório executivo pronto (15 slides)
- [ ] PowerPoint com visual profissional
- [ ] Orçamento detalhado (R$ 80-120M)
- [ ] Cronograma 12 semanas aprovado
- [ ] Responsáveis designados (Head + Diretor + Epidemiologista)
- [ ] ROI apresentado (8-14x retorno)

✅ Se tudo OK: **APRESENTAR PARA CONSELHO**

---

**Dúvidas restantes?** Consulte os READMEs específicos em cada pasta.

Good luck! 🚀
