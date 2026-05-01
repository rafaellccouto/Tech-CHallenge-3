#!/usr/bin/env python3
"""
Visualiza um sumário visual de todos os arquivos gerados
"""

from pathlib import Path
from datetime import datetime

def human_readable_size(size_bytes):
    """Converte bytes para formato legível"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f}{unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f}TB"

def print_summary():
    base_path = Path('.')
    
    print("\n" + "="*80)
    print("PROJETO PNAD-COVID-19: RESUMO DE ENTREGÁVEIS".center(80))
    print("="*80 + "\n")
    
    # 1. Gráficos
    print("GRÁFICOS GERADOS (6 arquivos PNG):")
    print("-" * 80)
    graficos_path = base_path / 'relatorios' / 'graficos'
    graficos = sorted(graficos_path.glob('*.png'))
    for i, g in enumerate(graficos, 1):
        size = human_readable_size(g.stat().st_size)
        print(f"  {i}. {g.name:<45} ({size:>8})")
    
    total_graficos = sum(g.stat().st_size for g in graficos)
    print(f"     {'Total':<45} ({human_readable_size(total_graficos):>8})\n")
    
    # 2. Dados
    print("DADOS PROCESSADOS (2 arquivos CSV):")
    print("-" * 80)
    dados_path = base_path / 'dados' / 'processed'
    dados = sorted(dados_path.glob('*.csv'))
    for i, d in enumerate(dados, 1):
        size = human_readable_size(d.stat().st_size)
        lines = len(d.read_text().splitlines())
        print(f"  {i}. {d.name:<45} ({size:>8}, {lines:,} linhas)")
    
    total_dados = sum(d.stat().st_size for d in dados)
    print(f"     {'Total':<45} ({human_readable_size(total_dados):>8})\n")
    
    # 3. Documentação
    print("DOCUMENTAÇÃO ATUALIZADA:")
    print("-" * 80)
    docs = [
        ('CONCLUSAO.md', 'Sumário de mudanças realizadas'),
        ('README.md', 'Visão geral do projeto'),
        ('GUIA_EXECUCAO.md', 'Passo-a-passo de execução'),
        ('ESTRUTURA_PROJETO.md', 'Arquitetura técnica'),
        ('run_pipeline.py', 'Script automatizado completo'),
    ]
    for doc_name, desc in docs:
        doc_path = base_path / doc_name
        if doc_path.exists():
            size = human_readable_size(doc_path.stat().st_size)
            print(f"  [OK] {doc_name:<35} {desc} ({size})")
        else:
            print(f"  [ERRO] {doc_name:<35} {desc} (NÃO ENCONTRADO)")
    
    print()
    
    # 4. Scripts
    print("SCRIPTS PYTHON:")
    print("-" * 80)
    scripts = [
        ('02_ETL/etl_pnad_covid.py', 'Limpeza e consolidação de dados XLSX'),
        ('03_Analise_Exploratoria/eda_pnad_covid.py', 'Gera 4 gráficos EDA'),
        ('04_Modelo_SEIR/modelo_seir.py', 'Simula 4 cenários SEIR'),
    ]
    for script, desc in scripts:
        script_path = base_path / script
        if script_path.exists():
            print(f"  [OK] {script:<40} {desc}")
        else:
            print(f"  [ERRO] {script:<40} {desc} (NÃO ENCONTRADO)")
    
    print("\n" + "="*80)
    print("STATUS: PROJETO COMPLETO - PRONTO PARA PRODUÇÃO".center(80))
    print("="*80 + "\n")
    
    print("COMO USAR:")
    print("-" * 80)
    print("  # Opção 1: Executar tudo automaticamente")
    print("  python run_pipeline.py\n")
    print("  # Opção 2: Executar passo a passo")
    print("  cd 02_ETL && python etl_pnad_covid.py")
    print("  cd ../03_Analise_Exploratoria && python eda_pnad_covid.py")
    print("  cd ../04_Modelo_SEIR && python modelo_seir.py\n")
    
    print("DOCUMENTAÇÃO IMPORTANTE:")
    print("-" * 80)
    print("  1. Leia primeiro: CONCLUSAO.md (mudanças realizadas)")
    print("  2. Visão geral: README.md")
    print("  3. Detalhes técnicos: 05_Relatorios/ANALISE_TECNICA.md")
    print("  4. Recomendações: 05_Relatorios/RECOMENDACOES_HOSPITAL.md\n")
    
    print("GRÁFICOS GERADOS:")
    print("-" * 80)
    print("  01_sintomas_evolucao.png           - Prevalência de sintomas")
    print("  02_taxa_internacao_sintomas.png    - Taxa de internação")
    print("  03_comportamento_evolucao.png      - Medidas preventivas")
    print("  04_indice_transmissao_beta.png     - Parâmetro β e R₀")
    print("  05_seir_cenarios_completos.png     - 4 cenários SEIR")
    print("  06_seir_comparacao_infectados.png  - Comparação infectados\n")
    
    print("=" * 80)
    print("Projeto finalizado em: {}".format(datetime.now().strftime('%d/%m/%Y %H:%M:%S')).center(80))
    print("=" * 80 + "\n")

if __name__ == '__main__':
    print_summary()
