from sensores import cadastrar_comodo, ler_consumos, obter_historico_comodos
from relatorios import exibir
from ia.enervision_ai import EnerVisionAI
import os
import time

# Inicializa a IA com janela de análise de 10 leituras
ia = EnerVisionAI(janela=10)

# Cadastro dos cômodos da casa (sensores virtuais)
cadastrar_comodo("Sala", 1200)
cadastrar_comodo("Cozinha", 2000)
cadastrar_comodo("Quarto", 800)
cadastrar_comodo("Banheiro", 600)

# Loop principal de monitoramento
while True:
    # Limpa o terminal para atualização em tempo real
    os.system("cls" if os.name == "nt" else "clear")

    # Lê os consumos atuais dos cômodos
    leituras = ler_consumos()

    # Soma o consumo total da casa
    consumo_total = sum(c["consumo"] for c in leituras)

    # Atualiza a IA com o novo consumo
    ia.atualizar(consumo_total)

    # Executa análises inteligentes
    previsao = ia.prever_consumo()
    anomalia = ia.detectar_anomalia(consumo_total)
    consumo_otimizado = ia.otimizar(consumo_total)

    # Detecta pico de demanda
    pico = previsao is not None and previsao > consumo_total * 1.25

    # Obtém o histórico por cômodo
    historico_comodos = obter_historico_comodos()

    # Exibe o relatório no terminal
    exibir(
        consumo_total,
        consumo_otimizado,
        pico,
        anomalia,
        previsao,
        historico_comodos
    )

    # Exibe consumo atual por cômodo
    print("\n🚪 Consumo atual por cômodo:")
    for c in leituras:
        print(f"• {c['nome']}: {c['consumo']} W / {c['potencia_maxima']} W")

    time.sleep(2)