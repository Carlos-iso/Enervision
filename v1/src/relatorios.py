def exibir(consumo, otimizado, pico, anomalia, previsao, historico_comodos):
    """
    Exibe o painel principal do sistema EnerVision no terminal.

    Mostra:
    - Consumo total da casa
    - Consumo otimizado pela IA
    - Previsão de consumo
    - Alertas de pico e anomalia
    - Histórico recente por cômodo

    Parâmetros:
    - consumo (float): Consumo total atual
    - otimizado (float): Consumo após otimização da IA
    - pico (bool): Indica previsão de pico de demanda
    - anomalia (bool): Indica anomalia detectada
    - previsao (float | None): Previsão da próxima leitura
    - historico_comodos (dict): Histórico de consumo por cômodo
    """
    print(r"""
    ███████╗███╗   ██╗███████╗██████╗ ██╗   ██╗██╗███████╗██╗ ██████╗ ███╗   ██╗
    ██╔════╝████╗  ██║██╔════╝██╔══██╗██║   ██║██║██╔════╝██║██╔═══██╗████╗  ██║
    █████╗  ██╔██╗ ██║█████╗  ██████╔╝██║   ██║██║███████╗██║██║   ██║██╔██╗ ██║
    ██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██║╚════██║██║██║   ██║██║╚██╗██║
    ███████╗██║ ╚████║███████╗██║  ██║ ╚████╔╝ ██║███████║██║╚██████╔╝██║ ╚████║
    ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
              Visão Inteligente Para Gestão De Energia.
    """)

    print("\n==============================================================================\n")
    print(f"🏠 Consumo total da casa: {round(consumo, 2)} W")
    print(f"♻️ Consumo otimizado: {round(otimizado, 2)} W")

    if previsao:
        print(f"🔮 Previsão próxima leitura: {round(previsao, 2)} W")

    if pico:
        print("⚠️ Pico de demanda previsto!")

    if anomalia:
        print("🔧 Anomalia detectada pela IA!")

    print("\n==============================================================================")
    print("\n📈 Histórico por cômodo:")

    # Exibe os últimos registros de cada cômodo
    for nome, valores in historico_comodos.items():
        valores_str = ", ".join(f"{round(v, 1)}W" for v in valores[-5:])
        print(f"• {nome}: {valores_str}")

    print("\n==============================================================================")