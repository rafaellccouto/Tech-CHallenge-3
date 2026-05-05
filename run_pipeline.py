#!/usr/bin/env python3
"""
Script Master: Executa todo o pipeline PNAD-COVID-19
- ETL: Lê dados XLSX de Dados_Base/ e consolida
- EDA: Gera 4 gráficos de análise exploratória
- SEIR: Simula 4 cenários e gera 2 gráficos comparativos
"""

import subprocess
import sys
from pathlib import Path

# Configuração de cores para terminal


class Cores:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_header(msg):
    print(f"\n{Cores.HEADER}{Cores.BOLD}{'='*80}{Cores.ENDC}")
    print(f"{Cores.HEADER}{Cores.BOLD}{msg:^80}{Cores.ENDC}")
    print(f"{Cores.HEADER}{Cores.BOLD}{'='*80}{Cores.ENDC}\n")


def print_success(msg):
    print(f"{Cores.OKGREEN}[OK] {msg}{Cores.ENDC}")


def print_error(msg):
    print(f"{Cores.FAIL}[ERRO] {msg}{Cores.ENDC}")


def print_info(msg):
    print(f"{Cores.OKCYAN}[INFO] {msg}{Cores.ENDC}")


def run_script(script_path, description):
    """Executa um script Python e verifica sucesso"""
    print_info(f"Executando: {description}")

    try:
        subprocess.run(
            [sys.executable, script_path],
            capture_output=False,
            check=True,
            cwd=str(Path(script_path).parent)
        )
        print_success(f"{description} concluído!")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"{description} falhou com código {e.returncode}")
        return False
    except FileNotFoundError:
        print_error(f"Script não encontrado: {script_path}")
        return False


def main():
    """Executa pipeline completo"""

    print_header("PNAD-COVID-19: Pipeline Completo de Análise")

    # Verificar estrutura de diretórios
    print_info("Verificando estrutura de diretórios...")

    dirs_necessarios = [
        'dados/processed',
        'dados/csv_meses',
        'relatorios/graficos',
        '02_ETL',
        '03_Analise_Exploratoria',
        '04_Modelo_SEIR'
    ]

    for dir_path in dirs_necessarios:
        Path(dir_path).mkdir(parents=True, exist_ok=True)

    print_success("Diretórios verificados/criados")

    # Fase 1: ETL
    print_header("FASE 1: ETL - Extração, Transformação e Carga")
    if not run_script('./02_ETL/etl_pnad_covid.py',
                      'ETL (Limpeza de dados XLSX)'):
        print_error("Falha no ETL. Abortando...")
        return False

    # Fase 2: EDA
    print_header("FASE 2: EDA - Análise Exploratória de Dados")
    if not run_script('./03_Analise_Exploratoria/eda_pnad_covid.py',
                      'EDA (Gráficos exploratórios)'):
        print_error("Falha no EDA. Abortando...")
        return False

    # Fase 3: SEIR
    print_header("FASE 3: SEIR - Modelo Epidemiológico")
    if not run_script('./04_Modelo_SEIR/modelo_seir.py',
                      'SEIR (Simulação de cenários)'):
        print_error("Falha no SEIR. Abortando...")
        return False

    # Copiar arquivos SEIR para pasta central
    print_info("Consolidando arquivos...")
    try:
        import shutil

        # Copiar gráficos SEIR
        seir_graficos = Path('04_Modelo_SEIR/relatorios/graficos')
        if seir_graficos.exists():
            for png_file in seir_graficos.glob('*.png'):
                shutil.copy(png_file, 'relatorios/graficos/')
            print_success("Gráficos SEIR copiados")

        # Copiar métricas
        seir_metrics = Path(
            '04_Modelo_SEIR/relatorios/metricas_seir_cenarios.csv')
        if seir_metrics.exists():
            shutil.copy(seir_metrics, 'relatorios/')
            print_success("Métricas SEIR copiadas")

    except Exception as e:
        print_error(f"Erro ao consolidar arquivos: {e}")

    # Relatório final
    print_header("PIPELINE CONCLUÍDO COM SUCESSO!")

    print(f"\n{Cores.OKGREEN}{Cores.BOLD}Arquivos Gerados:{Cores.ENDC}")
    print(f"\n{Cores.OKGREEN}Gráficos (6 PNG com 300dpi):{Cores.ENDC}")
    graficos = list(Path('relatorios/graficos').glob('*.png'))
    for i, g in enumerate(sorted(graficos), 1):
        print(f"   {i}. {g.name}")

    print(f"\n{Cores.OKGREEN}Dados Processados:{Cores.ENDC}")
    dados = list(Path('dados/processed').glob('*.csv'))
    for d in sorted(dados):
        size_mb = d.stat().st_size / (1024 * 1024)
        print(f"   • {d.name} ({size_mb:.2f} MB)")

    print(f"\n{Cores.OKGREEN}Métricas:{Cores.ENDC}")
    metrics_file = Path('relatorios/metricas_seir_cenarios.csv')
    if metrics_file.exists():
        print(f"   • {metrics_file.name}")

    print(f"\n{Cores.WARNING}{Cores.BOLD}Próximos Passos:{Cores.ENDC}")
    print(f"   1. Revisar gráficos em: relatorios/graficos/")
    print("   2. Ler documentação:")
    print("      - README.md (visão geral)")
    print("      - 05_Relatorios/RELATORIO_EXECUTIVO.md")
    print("      - 05_Relatorios/RECOMENDACOES_HOSPITAL.md")
    print(
        f"\n{Cores.OKGREEN}Todos os arquivos foram salvos com sucesso!{Cores.ENDC}\n")

    return True


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
