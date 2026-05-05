"""
PNAD-COVID-19: Script de ETL e Preparação de Dados
Prepara os dados XLSX de Dados_Base/ para análise no modelo SEIR
"""

import pandas as pd
import os
from pathlib import Path
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ==============================================================================
# CONFIGURAÇÕES INICIAIS
# ==============================================================================

MESES_ANALISE = [5, 8, 11]  # Maio, Agosto, Novembro (2020)
MESES_NOMES = {5: 'Maio', 8: 'Agosto', 11: 'Novembro'}

# Mapeamento de arquivos XLSX disponíveis de saúde
ARQUIVOS_DADOS = {
    5: '../Dados_Base/pnad_covid19_202005_saude_BR_GR_UF.xlsx',
    8: '../Dados_Base/pnad_covid19_202008_saude_BR_GR_UF.xlsx',
    11: '../Dados_Base/pnad_covid19_202011_saude_BR_GR_UF.xlsx',
}

# ==============================================================================
# FUNÇÕES AUXILIARES
# ==============================================================================


def criar_diretorio_dados():
    """Cria estrutura de diretórios para armazenar dados"""
    dirs = [
        '../dados/processed',
        '../dados/csv_meses'
    ]
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        logger.info(f"[OK] Diretório criado/verificado: {dir_path}")


def carregar_dados_xlsx(file_path: str, mes: int) -> pd.DataFrame:
    """Carrega arquivo XLSX e extrai dados relevantes"""

    logger.info(f"Carregando dados do mês {MESES_NOMES[mes]}...")

    try:
        # Carregar arquivo XLSX (primeira aba)
        df = pd.read_excel(file_path, sheet_name=0)

        logger.info(f"Dimensões originais: {df.shape}")
        logger.info(f"Primeiras colunas: {list(df.columns)[:10]}")

        # Adicionar coluna de mês
        df['mes_entrevista'] = mes

        # Tentar extrair colunas relevantes
        colunas_disponiveis = [
            col for col in df.columns if col not in [
                'Unnamed: 0', 'index']]

        if len(colunas_disponiveis) > 0:
            df_filtrado = df[colunas_disponiveis].copy()
            logger.info(f"[OK] Dimensões filtradas: {df_filtrado.shape}")
            logger.info(
                f"[OK] Colunas após seleção: {len(df_filtrado.columns)}")
            return df_filtrado
        else:
            logger.warning("Nenhuma coluna válida encontrada")
            return df.copy()

    except FileNotFoundError:
        logger.error(f"Arquivo não encontrado: {file_path}")
        return pd.DataFrame()
    except Exception as e:
        logger.error(f"Erro ao carregar dados: {e}")
        import traceback
        traceback.print_exc()
        return pd.DataFrame()


def limpar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpa e padroniza os dados
    """
    df_limpo = df.copy()

    logger.info("Iniciando limpeza de dados...")

    # 1. Remover colunas completamente vazias
    df_limpo.dropna(axis=1, how='all', inplace=True)

    # 2. Remover linhas completamente vazias
    df_limpo.dropna(axis=0, how='all', inplace=True)

    # 3. Converter valores para numéricos quando possível
    for col in df_limpo.columns:
        if col not in ['mes_entrevista', 'UF']:
            try:
                # Tentar conversão numérica
                df_limpo[col] = pd.to_numeric(df_limpo[col], errors='coerce')
            except BaseException:
                pass

    # 4. Reportar dados faltantes
    logger.info("\nDados Faltantes (top 10):")
    missing = df_limpo.isnull().sum().sort_values(ascending=False).head(10)
    if missing.sum() > 0:
        for col, count in missing.items():
            if count > 0:
                pct = (count / len(df_limpo)) * 100
                logger.info(f"  {col}: {count} ({pct:.1f}%)")
    else:
        logger.info("  Nenhum dado faltante após limpeza!")

    logger.info(
        f"[OK] Limpeza concluída. Linhas: {len(df_limpo):,}, Colunas: {len(df_limpo.columns)}")

    return df_limpo


def gerar_indicadores_agregados(df: pd.DataFrame, mes: int) -> dict:
    """Gera indicadores agregados por mês"""

    indicadores = {
        'mes': mes,
        'mes_nome': MESES_NOMES[mes],
        'total_entrevistados': len(df),
        'total_colunas': len(df.columns),
    }

    return indicadores

# ==============================================================================
# EXECUÇÃO PRINCIPAL
# ==============================================================================


def main():
    """Executa pipeline completo de ETL"""

    logger.info("=" * 80)
    logger.info("🏥 PNAD-COVID-19: ETL e Preparação de Dados")
    logger.info("=" * 80)

    # 1. Criar estrutura de diretórios
    criar_diretorio_dados()

    # 2. Processar cada mês
    dfs_processados = []
    indicadores_todos_meses = []

    for mes in MESES_ANALISE:
        logger.info(f"\n{'='*80}")
        logger.info(f"Processando: {MESES_NOMES[mes]}/2020")
        logger.info(f"{'='*80}")

        # Obter caminho do arquivo
        file_path = ARQUIVOS_DADOS.get(mes)

        if file_path and os.path.exists(file_path):
            # Carregar dados
            df = carregar_dados_xlsx(file_path, mes)

            if not df.empty:
                # Limpar dados
                df_limpo = limpar_dados(df)

                # Gerar indicadores
                indicadores = gerar_indicadores_agregados(df_limpo, mes)
                indicadores_todos_meses.append(indicadores)

                # Salvar processado
                output_path = f'../dados/csv_meses/pnad_covid_{mes:02d}_processado.csv'
                df_limpo.to_csv(output_path, index=False)
                logger.info(f"[OK] Salvo em: {output_path}")

                dfs_processados.append(df_limpo)
        else:
            logger.error(
                f"[ERRO] Arquivo não encontrado para {MESES_NOMES[mes]}")

    # 3. Combinar todos os meses
    if dfs_processados:
        logger.info(f"\n{'='*80}")
        logger.info("Combinando dados de todos os meses...")
        logger.info(f"{'='*80}")

        df_final = pd.concat(dfs_processados, ignore_index=True)

        # Salvar base consolidada
        output_consolidado = '../dados/processed/pnad_covid_consolidado_maio_agosto_novembro_2020.csv'
        df_final.to_csv(output_consolidado, index=False)
        logger.info(f"[OK] Base consolidada salva: {output_consolidado}")
        logger.info(f"[OK] Total de linhas: {len(df_final):,}")
        logger.info(f"[OK] Total de colunas: {len(df_final.columns)}")

        # Salvar indicadores agregados
        df_indicadores = pd.DataFrame(indicadores_todos_meses)
        indicadores_path = '../dados/processed/indicadores_agregados_por_mes.csv'
        df_indicadores.to_csv(indicadores_path, index=False)
        logger.info(f"[OK] Indicadores agregados salvos: {indicadores_path}")

        # Exibir resumo
        logger.info("\nRESUMO DOS INDICADORES POR MÊS:")
        logger.info(df_indicadores.to_string(index=False))

        logger.info("\nPipeline ETL Concluído com Sucesso!")
        return df_final
    else:
        logger.error("[ERRO] Nenhum arquivo foi processado com sucesso.")
        return None


if __name__ == "__main__":
    df_consolidado = main()
