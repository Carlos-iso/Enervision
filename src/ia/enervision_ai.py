import math

class EnerVisionAI:
    """
    Classe responsável pelas decisões inteligentes do sistema EnerVision.

    Funções principais:
    - Detecção de anomalias
    - Previsão de consumo
    - Otimização energética
    """

    def __init__(self, janela=10):
        """
        Inicializa a IA com uma janela de análise.

        Parâmetros:
        - janela (int): Quantidade de leituras usadas para análise estatística
        """
        self.janela = janela
        self.historico = []

    def atualizar(self, consumo):
        """
        Atualiza o histórico de consumo com a leitura mais recente.

        Parâmetros:
        - consumo (float): Consumo total atual da casa
        """
        self.historico.append(consumo)
        if len(self.historico) > self.janela:
            self.historico.pop(0)

    def _media(self):
        """
        Calcula a média do consumo na janela atual.

        Retorno:
        - float: Média de consumo
        """
        return sum(self.historico) / len(self.historico)

    def _desvio(self):
        """
        Calcula o desvio padrão do consumo.

        Retorno:
        - float: Desvio padrão
        """
        media = self._media()
        return math.sqrt(
            sum((x - media) ** 2 for x in self.historico) / len(self.historico)
        )

    def detectar_anomalia(self, consumo):
        """
        Detecta anomalias usando Z-Score.

        Retorno:
        - bool: True se uma anomalia for detectada
        """
        if len(self.historico) < 5:
            return False

        desvio = self._desvio()
        if desvio == 0:
            return False

        z_score = abs(consumo - self._media()) / desvio
        return z_score > 2.5

    def prever_consumo(self):
        """
        Realiza uma previsão simples baseada na tendência recente.

        Retorno:
        - float | None: Consumo previsto ou None se não houver dados suficientes
        """
        if len(self.historico) < 5:
            return None

        diffs = [
            self.historico[i + 1] - self.historico[i]
            for i in range(len(self.historico) - 1)
        ]

        tendencia = sum(diffs) / len(diffs)
        return self.historico[-1] + tendencia

    def otimizar(self, consumo):
        """
        Aplica uma estratégia simples de otimização de energia.

        Se a previsão indicar aumento significativo,
        reduz preventivamente o consumo.

        Retorno:
        - float: Consumo otimizado
        """
        previsao = self.prever_consumo()
        media = self._media()

        if previsao and previsao > media * 1.2:
            return consumo * 0.85

        return consumo