"""
PNAD-COVID-19: Modelo SEIR Integrado
Simula dinâmica de transmissão com parâmetros calibrados em dados reais
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from pathlib import Path
import logging
import warnings

warnings.filterwarnings('ignore')

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

plt.style.use('seaborn-v0_8-darkgrid')

# ==============================================================================
# DEFINIÇÃO DO MODELO SEIR
# ==============================================================================


class ModeloSEIR:
    """
    Implementação do Modelo SEIR (Susceptible-Exposed-Infected-Recovered)

    S(t) = Suscetíveis (podem contrair o vírus)
    E(t) = Expostos (infectados, mas sem transmissão)
    I(t) = Infectados (transmitem o vírus)
    R(t) = Recuperados/Removidos (imunidade ou morte)

    Equações Diferenciais:
        dS/dt = -β * S * I / N
        dE/dt = β * S * I / N - σ * E
        dI/dt = σ * E - γ * I
        dR/dt = γ * I

    Parâmetros:
        β = Taxa de transmissão (contatos × probabilidade de transmissão)
        σ = 1 / período de incubação (dias)
        γ = 1 / período de infecção (dias)
    """

    def __init__(self, populacao: int = 10_000_000,
                 beta: float = 0.5,
                 sigma: float = 1 / 5.5,
                 gamma: float = 1 / 10):
        """
        Inicializa o modelo SEIR

        Args:
            populacao: População total (N)
            beta: Taxa de transmissão (padrão: 0.5)
            sigma: Taxa de incubação (padrão: 1/5.5, ~5.5 dias)
            gamma: Taxa de recuperação (padrão: 1/10, ~10 dias)
        """
        self.N = populacao
        self.beta = beta
        self.sigma = sigma
        self.gamma = gamma

        logger.info(f"Modelo SEIR Inicializado:")
        logger.info(f"   População (N): {populacao:,}")
        logger.info(f"   β (transmissão): {beta}")
        logger.info(f"   σ (incubação): {sigma:.4f} (≈ {1/sigma:.1f} dias)")
        logger.info(f"   γ (recuperação): {gamma:.4f} (≈ {1/gamma:.1f} dias)")
        logger.info(f"   R₀ (número de reprodução básica): {beta/gamma:.2f}")

    def derivadas(self, y, t):
        """
        Calcula as derivadas de S, E, I, R

        Args:
            y: [S, E, I, R] no tempo t
            t: tempo (não usado, mas necessário para odeint)

        Returns:
            [dS/dt, dE/dt, dI/dt, dR/dt]
        """
        S, E, I, R = y

        dS_dt = -self.beta * S * I / self.N
        dE_dt = self.beta * S * I / self.N - self.sigma * E
        dI_dt = self.sigma * E - self.gamma * I
        dR_dt = self.gamma * I

        return [dS_dt, dE_dt, dI_dt, dR_dt]

    def simular(self, dias: int = 365,
                S0: int = None,
                E0: int = 10,
                I0: int = 1,
                R0: int = 0):
        """
        Simula o modelo SEIR

        Args:
            dias: Número de dias a simular
            S0: População suscetível inicial (padrão: N-E0-I0-R0)
            E0: Expostos iniciais
            I0: Infectados iniciais
            R0: Recuperados iniciais

        Returns:
            (t, S, E, I, R) - Séries temporais
        """

        if S0 is None:
            S0 = self.N - E0 - I0 - R0

        y0 = [S0, E0, I0, R0]
        t = np.linspace(0, dias, dias)

        solucao = odeint(self.derivadas, y0, t)

        S, E, I, R = solucao.T

        return t, S, E, I, R

    def calcular_metricas(self, S, E, I, R):
        """Calcula métricas importantes da simulação"""

        pico_infectados = np.max(I)
        dia_pico = np.argmax(I)
        # % da população que foi infectada
        taxa_ataque = (R[-1] / self.N) * 100

        return {
            'pico_infectados': int(pico_infectados),
            'dia_pico': int(dia_pico),
            'total_infectados': int(E[-1] + I[-1] + R[-1]),
            'taxa_ataque_final': round(taxa_ataque, 2),
            'R0': self.beta / self.gamma
        }

# ==============================================================================
# CENÁRIOS DE SIMULAÇÃO
# ==============================================================================


class CenariosSEIR:
    """Define e simula diferentes cenários de surto"""

    def __init__(self, dados_comportamento: dict):
        """
        Inicializa cenários com dados comportamentais reais

        Args:
            dados_comportamento: Dicionário com indicadores da PNAD
                Deve conter: beta_maio, beta_agosto, beta_novembro
        """
        self.dados = dados_comportamento
        self.resultados = {}

    def cenario_1_baseline_maio(self):
        """Cenário 1: Linha de Base (Maio 2020)"""

        logger.info("\n" + "=" * 80)
        logger.info("CENÁRIO 1: BASELINE - MAIO 2020 (Susto Inicial)")
        logger.info("=" * 80)

        beta = self.dados.get('beta_maio', 0.45)

        modelo = ModeloSEIR(beta=beta, sigma=1 / 5.5, gamma=1 / 10)
        t, S, E, I, R = modelo.simular(dias=180, S0=9_999_000, I0=100)
        metricas = modelo.calcular_metricas(S, E, I, R)

        logger.info(
            f"\n[OK] Pico de infectados: {metricas['pico_infectados']:,} pessoas")
        logger.info(f"[OK] Dia do pico: Dia {metricas['dia_pico']}")
        logger.info(
            f"[OK] Taxa de ataque final: {metricas['taxa_ataque_final']:.1f}%")
        logger.info(f"[OK] R₀ estimado: {metricas['R0']:.2f}")

        self.resultados['maio'] = {
            'modelo': modelo,
            't': t, 'S': S, 'E': E, 'I': I, 'R': R,
            'metricas': metricas
        }

        return t, S, E, I, R, metricas

    def cenario_2_pressao_agosto(self):
        """Cenário 2: Pressão Máxima (Agosto 2020 - Pico Histórico)"""

        logger.info("\n" + "=" * 80)
        logger.info("CENÁRIO 2: PRESSÃO - AGOSTO 2020 (Pico Histórico)")
        logger.info("=" * 80)

        beta = self.dados.get('beta_agosto', 0.65)  # Maior transmissão

        modelo = ModeloSEIR(beta=beta, sigma=1 / 5.5, gamma=1 / 10)

        # Em agosto, já havia muitos expostos e infectados
        S0 = 8_500_000
        E0 = 150_000
        I0 = 250_000
        R0 = 1_100_000

        t, S, E, I, R = modelo.simular(dias=120, S0=S0, E0=E0, I0=I0, R0=R0)
        metricas = modelo.calcular_metricas(S, E, I, R)

        logger.info(
            f"\n[OK] Pico de infectados: {metricas['pico_infectados']:,} pessoas")
        logger.info(f"[OK] Dia do pico: Dia {metricas['dia_pico']}")
        logger.info(
            f"[OK] Taxa de ataque final: {metricas['taxa_ataque_final']:.1f}%")
        logger.info(f"[OK] R₀ estimado: {metricas['R0']:.2f}")

        self.resultados['agosto'] = {
            'modelo': modelo,
            't': t, 'S': S, 'E': E, 'I': I, 'R': R,
            'metricas': metricas
        }

        return t, S, E, I, R, metricas

    def cenario_3_adaptacao_novembro(self):
        """Cenário 3: Nova Dinâmica (Novembro 2020 - Controle Relativo)"""

        logger.info("\n" + "=" * 80)
        logger.info("CENÁRIO 3: ADAPTAÇÃO - NOVEMBRO 2020 (Controle Relativo)")
        logger.info("=" * 80)

        # Menor transmissão (mais medidas)
        beta = self.dados.get('beta_novembro', 0.35)

        modelo = ModeloSEIR(beta=beta, sigma=1 / 5.5, gamma=1 / 10)

        # Em novembro, muita população já tinha sido infectada
        S0 = 6_500_000
        E0 = 80_000
        I0 = 120_000
        R0 = 3_300_000

        t, S, E, I, R = modelo.simular(dias=90, S0=S0, E0=E0, I0=I0, R0=R0)
        metricas = modelo.calcular_metricas(S, E, I, R)

        logger.info(
            f"\n[OK] Pico de infectados: {metricas['pico_infectados']:,} pessoas")
        logger.info(f"[OK] Dia do pico: Dia {metricas['dia_pico']}")
        logger.info(
            f"[OK] Taxa de ataque final: {metricas['taxa_ataque_final']:.1f}%")
        logger.info(f"[OK] R₀ estimado: {metricas['R0']:.2f}")

        self.resultados['novembro'] = {
            'modelo': modelo,
            't': t, 'S': S, 'E': E, 'I': I, 'R': R,
            'metricas': metricas
        }

        return t, S, E, I, R, metricas

    def cenario_4_novo_surto_mitigacao(self):
        """
        Cenário 4: Novo Surto com Mitigação Agressiva
        Simula resposta hospitalar otimizada
        """

        logger.info("\n" + "=" * 80)
        logger.info("CENÁRIO 4: NOVO SURTO COM MITIGAÇÃO AGRESSIVA")
        logger.info("=" * 80)

        # β reduzido por 50% (máximas medidas: lockdown, vacina)
        beta_mitigado = self.dados.get('beta_maio', 0.45) * 0.5

        modelo = ModeloSEIR(beta=beta_mitigado, sigma=1 / 5.5, gamma=1 / 10)

        # Novo surto começa com menos infecções
        t, S, E, I, R = modelo.simular(dias=200, S0=9_990_000, I0=100)
        metricas = modelo.calcular_metricas(S, E, I, R)

        logger.info(
            f"\n[OK] Pico de infectados (com mitigação): {metricas['pico_infectados']:,} pessoas")
        logger.info(
            f"[OK] Redução vs Cenário 1: {((1 - metricas['pico_infectados']/self.resultados['maio']['metricas']['pico_infectados'])*100):.1f}%")
        logger.info(
            f"[OK] Taxa de ataque: {metricas['taxa_ataque_final']:.1f}%")

        self.resultados['novo_surto_mitigado'] = {
            'modelo': modelo,
            't': t, 'S': S, 'E': E, 'I': I, 'R': R,
            'metricas': metricas
        }

        return t, S, E, I, R, metricas

    def simular_todos_cenarios(self):
        """Executa simulação de todos os cenários"""

        logger.info("\n" + "=" * 80)
        logger.info("EXECUÇÃO DE TODOS OS CENÁRIOS")
        logger.info("=" * 80)

        self.cenario_1_baseline_maio()
        self.cenario_2_pressao_agosto()
        self.cenario_3_adaptacao_novembro()
        self.cenario_4_novo_surto_mitigacao()

        logger.info("\nSimulação de cenários concluída!")

    def plotar_comparacao_cenarios(self):
        """Plota todos os cenários lado a lado"""

        logger.info("\n📊 Gerando gráficos comparativos...")

        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle(
            'Modelo SEIR: Comparação de Cenários',
            fontsize=16,
            fontweight='bold')

        cenarios_plot = [
            ('maio', axes[0, 0], 'Cenário 1: Baseline Maio'),
            ('agosto', axes[0, 1], 'Cenário 2: Pressão Agosto'),
            ('novembro', axes[1, 0], 'Cenário 3: Adaptação Novembro'),
            ('novo_surto_mitigado', axes[1, 1], 'Cenário 4: Novo Surto Mitigado')
        ]

        for cenario_key, ax, titulo in cenarios_plot:
            if cenario_key in self.resultados:
                resultado = self.resultados[cenario_key]
                t, S, E, I, R = resultado['t'], resultado['S'], resultado['E'], resultado['I'], resultado['R']

                ax.plot(
                    t,
                    S / 1_000_000,
                    label='Suscetíveis (S)',
                    linewidth=2,
                    color='blue')
                ax.plot(
                    t,
                    E / 1_000_000,
                    label='Expostos (E)',
                    linewidth=2,
                    color='orange')
                ax.plot(
                    t,
                    I / 1_000_000,
                    label='Infectados (I)',
                    linewidth=2,
                    color='red')
                ax.plot(
                    t,
                    R / 1_000_000,
                    label='Recuperados (R)',
                    linewidth=2,
                    color='green')

                pico = np.max(I)
                dia_pico = np.argmax(I)
                ax.plot(
                    dia_pico,
                    pico / 1_000_000,
                    'r*',
                    markersize=15,
                    label=f'Pico: {pico/1_000_000:.1f}M')

                ax.set_xlabel('Dias', fontsize=11)
                ax.set_ylabel('População (milhões)', fontsize=11)
                ax.set_title(titulo, fontsize=12, fontweight='bold')
                ax.legend(fontsize=9)
                ax.grid(True, alpha=0.3)

        plt.tight_layout()
        Path('relatorios/graficos').mkdir(parents=True, exist_ok=True)
        plt.savefig(
            'relatorios/graficos/05_seir_cenarios_completos.png',
            dpi=300,
            bbox_inches='tight')
        logger.info(
            "[OK] Gráfico salvo: relatorios/graficos/05_seir_cenarios_completos.png")
        plt.close()

    def plotar_comparacao_infectados(self):
        """Compara apenas a curva de infectados entre cenários"""

        fig, ax = plt.subplots(figsize=(14, 8))

        cores = {
            'maio': '#FF6B6B',
            'agosto': '#FFA500',
            'novembro': '#4CAF50',
            'novo_surto_mitigado': '#2196F3'}

        for cenario_key, cor in cores.items():
            if cenario_key in self.resultados:
                resultado = self.resultados[cenario_key]
                t, I = resultado['t'], resultado['I']

                label = {
                    'maio': 'Maio 2020 (Baseline)',
                    'agosto': 'Agosto 2020 (Pressão)',
                    'novembro': 'Novembro 2020 (Adaptação)',
                    'novo_surto_mitigado': 'Novo Surto (Mitigado)'
                }[cenario_key]

                ax.plot(
                    t,
                    I / 1_000_000,
                    label=label,
                    linewidth=2.5,
                    color=cor)

        ax.set_xlabel('Dias', fontsize=12)
        ax.set_ylabel('Infectados (milhões)', fontsize=12)
        ax.set_title('Comparação: Curva de Infectados (I) - Todos os Cenários',
                     fontsize=14, fontweight='bold')
        ax.legend(fontsize=11, loc='upper right')
        ax.grid(True, alpha=0.3)
        ax.axhline(
            y=1,
            color='red',
            linestyle='--',
            alpha=0.5,
            label='1 milhão infectados')

        plt.tight_layout()
        plt.savefig(
            'relatorios/graficos/06_seir_comparacao_infectados.png',
            dpi=300,
            bbox_inches='tight')
        logger.info(
            "[OK] Gráfico salvo: relatorios/graficos/06_seir_comparacao_infectados.png")
        plt.close()

    def gerar_tabela_metricas(self):
        """Gera tabela comparativa de métricas entre cenários"""

        linhas = []

        for cenario_key, nome in [('maio', 'Maio'), ('agosto', 'Agosto'), (
                'novembro', 'Novembro'), ('novo_surto_mitigado', 'Novo Surto Mitigado')]:
            if cenario_key in self.resultados:
                metricas = self.resultados[cenario_key]['metricas']
                linhas.append({
                    'Cenário': nome,
                    'Pico Infectados': f"{metricas['pico_infectados']:,}",
                    'Dia do Pico': metricas['dia_pico'],
                    'Taxa Ataque (%)': metricas['taxa_ataque_final'],
                    'R₀': f"{metricas['R0']:.2f}"
                })

        df_metricas = pd.DataFrame(linhas)

        logger.info("\n" + "=" * 80)
        logger.info("📊 TABELA COMPARATIVA DE MÉTRICAS")
        logger.info("=" * 80)
        logger.info(df_metricas.to_string(index=False))

        return df_metricas

# ==============================================================================
# EXECUÇÃO PRINCIPAL
# ==============================================================================


def main():
    """Executa o pipeline completo do modelo SEIR"""

    logger.info("=" * 80)
    logger.info("MODELO SEIR: Dinâmica de Transmissão COVID-19")
    logger.info("=" * 80)

    # Dados comportamentais da PNAD (estimativas)
    dados_comportamento = {
        'beta_maio': 0.45,      # Transmissão inicial
        'beta_agosto': 0.65,    # Pico
        'beta_novembro': 0.35   # Controle
    }

    # Criar cenários
    cenarios = CenariosSEIR(dados_comportamento)
    cenarios.simular_todos_cenarios()

    # Gerar visualizações
    cenarios.plotar_comparacao_cenarios()
    cenarios.plotar_comparacao_infectados()

    # Tabela comparativa
    df_metricas = cenarios.gerar_tabela_metricas()

    # Salvar tabela
    Path('relatorios').mkdir(parents=True, exist_ok=True)
    df_metricas.to_csv('relatorios/metricas_seir_cenarios.csv', index=False)
    logger.info(
        "\n[OK] Métricas salvas: relatorios/metricas_seir_cenarios.csv")

    logger.info("\n" + "=" * 80)
    logger.info("MODELO SEIR EXECUTADO COM SUCESSO")
    logger.info("=" * 80)
    logger.info("\nArquivos gerados:")
    logger.info("   - relatorios/graficos/05_seir_cenarios_completos.png")
    logger.info("   - relatorios/graficos/06_seir_comparacao_infectados.png")
    logger.info("   - relatorios/metricas_seir_cenarios.csv")


if __name__ == "__main__":
    main()
