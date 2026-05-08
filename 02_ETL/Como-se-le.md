# 📊 Estrutura e Formato dos Dados de Saída

---

## 1. **Arquivos Individuais por Mês**
### `pnad_covid_05_processado.csv`, `pnad_covid_08_processado.csv`, `pnad_covid_11_processado.csv`

Estes arquivos contêm os dados **após limpeza**, mas ainda **separados por mês**.

**Estrutura genérica de uma linha:**

```
mes_entrevista,coluna1,coluna2,coluna3,...,colunaN
5,valor1,valor2,valor3,...,valorN
5,valor1,valor2,valor3,...,valorN
5,valor1,valor2,valor3,...,valorN
```

### Exemplo Real (imaginário, baseado em PNAD-COVID)

```csv
mes_entrevista,UF,idade,renda,tosse,febre,dificuldade_respiratoria,testado_covid
5,São Paulo,35,2500.5,0,1,0,0
5,São Paulo,42,1800.0,1,1,1,1
5,Rio de Janeiro,28,3200.75,0,0,0,0
5,Minas Gerais,55,1200.0,,1,1,
5,Bahia,22,950.5,1,0,0,1
```

**Como ler:**

| Coluna | Tipo | Significado |
|--------|------|-------------|
| `mes_entrevista` | Número (int) | Mês da coleta: 5, 8 ou 11 |
| `UF` | Texto | Estado (São Paulo, Rio de Janeiro, etc.) |
| `idade` | Número (float) | Idade da pessoa entrevistada |
| `renda` | Número (float) | Renda em reais |
| `tosse` | Número (0/1) ou vazio | 1=tem tosse, 0=não tem, vazio=não respondeu |
| `febre` | Número (0/1) ou vazio | 1=tem febre, 0=não tem, vazio=não respondeu |
| `dificuldade_respiratoria` | Número (0/1) ou vazio | 1=tem, 0=não tem, vazio=não respondeu |
| `testado_covid` | Número (0/1) ou vazio | 1=foi testado, 0=não foi, vazio=não respondeu |

**Observações importantes:**
- Células vazias = dados faltantes (NaN do pandas)
- Números com ponto = valores decimais/floats
- 0 e 1 = valores booleanos (sim/não)
- Cada **linha = 1 pessoa entrevistada**
- Cada **coluna = 1 variável/atributo**

---

## 2. **Arquivo Consolidado**
### `pnad_covid_consolidado_maio_agosto_novembro_2020.csv`

Este é o arquivo **FINAL** que une os 3 meses em um único DataFrame.

**Estrutura:**

```csv
mes_entrevista,UF,idade,renda,tosse,febre,dificuldade_respiratoria,testado_covid
5,São Paulo,35,2500.5,0,1,0,0
5,São Paulo,42,1800.0,1,1,1,1
5,Rio de Janeiro,28,3200.75,0,0,0,0
8,São Paulo,45,2100.0,0,0,0,1
8,Minas Gerais,33,1500.0,1,0,0,0
11,Bahia,50,900.0,0,1,1,
11,São Paulo,29,2800.5,0,0,0,0
```

**Como ler:**

- **Linha 1:** Cabeçalho (nomes das colunas)
- **Linhas 2+:** Dados dos 3 meses misturados
- **Total de linhas:** Soma de todas as pessoas dos 3 meses
  - Se maio tem 10.000 linhas
  - Se agosto tem 10.500 linhas
  - Se novembro tem 9.800 linhas
  - **Total = 30.300 linhas**

**Diferença do arquivo mensal:**
- Arquivo mensal tem apenas dados de 1 mês
- Arquivo consolidado tem dados de TODOS os 3 meses
- Coluna `mes_entrevista` permite filtrar por mês se necessário

---

## 3. **Arquivo de Indicadores Agregados**
### `indicadores_agregados_por_mes.csv`

Este é um **resumo estatístico** (não dados brutos).

**Estrutura:**

```csv
mes,mes_nome,total_entrevistados,total_colunas
5,Maio,10000,47
8,Agosto,10500,47
11,Novembro,9800,47
```

**Como ler:**

| Coluna | Tipo | Significado |
|--------|------|-------------|
| `mes` | Número | 5, 8 ou 11 |
| `mes_nome` | Texto | "Maio", "Agosto" ou "Novembro" |
| `total_entrevistados` | Número | Quantidade de pessoas entrevistadas naquele mês |
| `total_colunas` | Número | Quantidade de variáveis/atributos coletados |

**Exemplo completo:**

```
Maio 2020:
  - 10.000 pessoas entrevistadas
  - 47 variáveis/colunas de dados

Agosto 2020:
  - 10.500 pessoas entrevistadas
  - 47 variáveis/colunas de dados

Novembro 2020:
  - 9.800 pessoas entrevistadas
  - 47 variáveis/colunas de dados

Total geral: 30.300 pessoas
```

---

## 4. **Visualização em Python (Como Ler os Dados)**

Se você quiser **abrir e analisar** esses arquivos:

```python
import pandas as pd

# Ler arquivo consolidado
df = pd.read_csv('../dados/processed/pnad_covid_consolidado_maio_agosto_novembro_2020.csv')

# Ver primeiras 5 linhas
print(df.head())

# Ver informações gerais
print(df.info())

# Ver estatísticas
print(df.describe())

# Filtrar apenas maio
maio = df[df['mes_entrevista'] == 5]
print(f"Total de entrevistados em maio: {len(maio)}")

# Contar valores faltantes
print(df.isnull().sum())
```

**Saída esperada:**

```
   mes_entrevista          UF  idade      renda  tosse  febre  ...
0               5  São Paulo      35    2500.50      0      1  ...
1               5  São Paulo      42    1800.00      1      1  ...
2               5 Rio de Janeiro  28    3200.75      0      0  ...
3               8  São Paulo      45    2100.00      0      0  ...
4               8 Minas Gerais    33    1500.00      1      0  ...

[30300 rows x 47 columns]
```

---

## 5. **Estrutura Completa com Exemplos**

### Visualização em Tabela (Excel/LibreOffice)

Quando você abre `pnad_covid_consolidado_maio_agosto_novembro_2020.csv` em Excel:

```
┌─────┬─────────────────┬────────┬───────┬─────┬───────┬──────────────┬────────────┐
│ Row │ mes_entrevista  │ UF     │ idade │ ... │ tosse │ febre        │ testado_covid
├─────┼─────────────────┼────────┼───────┼─────┼───────┼──────────────┼────────────┤
│  1  │ 5               │ SP     │ 35    │ ... │ 0     │ 1            │ 0          │
│  2  │ 5               │ SP     │ 42    │ ... │ 1     │ 1            │ 1          │
│  3  │ 5               │ RJ     │ 28    │ ... │ 0     │ 0            │ 0          │
│  4  │ 5               │ MG     │ 55    │ ... │       │ 1            │            │
│  5  │ 8               │ BA     │ 22    │ ... │ 1     │ 0            │ 1          │
│ ... │ ...             │ ...    │ ...   │ ... │ ...   │ ...          │ ...        │
│ 30300
</parameter>
│ 11              │ SP     │ 29    │ ... │ 0     │ 0            │ 0          │
└─────┴─────────────────┴────────┴───────┴─────┴───────┴──────────────┴────────────┘
```

---

## 6. **Interpretação de Dados Faltantes**

Durante a execução, o script mostra um **relatório de dados faltantes**:

```
Dados Faltantes (top 10):
  tosse: 1500 (14.9%)
  febre: 2100 (20.9%)
  dificuldade_respiratoria: 850 (8.5%)
  testado_covid: 3200 (31.8%)
  renda: 4500 (44.8%)
```

**Como interpretar:**
- **tosse**: 1.500 pessoas não responderam (14,9% do total)
- **renda**: 4.500 pessoas não informaram renda (44,8% - bastante!)
- **testado_covid**: 3.200 pessoas não responderam (31,8%)

Essas células vazias aparecem como campos em branco no CSV.

---

## 7. **Resumo Visual Dos 3 Arquivos**

```
┌─────────────────────────────────────────────────────┐
│         ARQUIVOS DE SAÍDA DO SCRIPT                │
└──────────────────��──────────────────────────────────┘

1. pnad_covid_05_processado.csv
   ├─ Apenas dados de MAIO
   ├─ ~10.000 linhas (pessoas)
   ├─ 47 colunas (variáveis)
   └─ Já limpo e processado

2. pnad_covid_08_processado.csv
   ├─ Apenas dados de AGOSTO
   ├─ ~10.500 linhas (pessoas)
   ├─ 47 colunas (variáveis)
   └─ Já limpo e processado

3. pnad_covid_11_processado.csv
   ├─ Apenas dados de NOVEMBRO
   ├─ ~9.800 linhas (pessoas)
   ├─ 47 colunas (variáveis)
   └─ Já limpo e processado

4. pnad_covid_consolidado_maio_agosto_novembro_2020.csv
   ├─ TODOS os 3 meses combinados
   ├─ ~30.300 linhas (pessoas)
   ├─ 47 colunas (variáveis)
   ├─ Coluna "mes_entrevista" permite identificar mês
   └─ PRONTO para análise SEIR

5. indicadores_agregados_por_mes.csv
   ├─ RESUMO dos 3 meses
   ├─ 3 linhas (1 por mês)
   ├─ Colunas: mes, mes_nome, total_entrevistados, total_colunas
   └─ Útil para relatório executivo
```

---

## 8. **Comparação: Antes vs Depois da Limpeza**

**ANTES (arquivo XLSX original):**
```csv
Unnamed: 0,index,coluna1,coluna2,coluna_vazia,coluna3
1,0,valor1,abc,,,valor3
2,1,valor2,def,,,valor3
3,2,valor3,"texto",,,valor3
```

**DEPOIS (arquivo CSV processado):**
```csv
mes_entrevista,coluna1,coluna2,coluna3
5,1.0,1.0,3.0
5,2.0,2.0,3.0
5,3.0,3.0,3.0
```

**Mudanças:**
- ✅ Removidas colunas "Unnamed: 0", "index" e "coluna_vazia"
- ✅ Valores textos convertidos para números (NaN se não conseguiu)
- ✅ Adicionada coluna "mes_entrevista"
- ✅ Formatado para análise

---

## 9. **Como Usar os Dados no Modelo SEIR**

O arquivo consolidado está **pronto para o modelo SEIR** porque:

1. **Todas as linhas são pessoas** (unidade de análise)
2. **Todas as colunas são variáveis** (atributos da pessoa)
3. **Dados numéricos** (0/1 para sintomas, números para idade/renda)
4. **Temporalidade** (coluna `mes_entrevista` marca o tempo)
5. **Sem valores anormais** (limpeza removeu colunas inúteis)

Exemplo de como filtrar:

```python
# Pessoas com tosse em Maio
tosse_maio = df[(df['mes_entrevista'] == 5) & (df['tosse'] == 1)]
print(f"Pessoas com tosse em maio: {len(tosse_maio)}")

# Taxa de positividade por mês
taxa_positivos = df.groupby('mes_entrevista')['testado_covid'].mean()
```