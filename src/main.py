from previsao import detectar_pico
from otimizador import otimizar
from anomalias import detectar_anomalia
from relatorios import exibir
from sensores import cadastrar_sensor, ler_consumos
import time
import os
historico = []
cadastrar_sensor("Cozinha", 500)
cadastrar_sensor("Quarto", 1500)
cadastrar_sensor("Sala", 600)
cadastrar_sensor("Banheiro", 1700)
while True:
    os.system("cls" if os.name == "nt" else "clear")
    leituras = ler_consumos()
    consumo_total = sum(sensor["consumo"] for sensor in leituras)
    historico.append(consumo_total)
    pico = detectar_pico(consumo_total)
    consumo_otimizado = otimizar(consumo_total)
    anomalia = detectar_anomalia(historico)
    exibir(consumo_total, consumo_otimizado, pico, anomalia)
    print("\n🔌 Sensores:")
    for sensor in leituras:
        print(f"• {sensor['nome']}: {sensor['consumo']} W / {sensor['potencia_maxima']} W")
    print("\n==============================================================================")
    print("\n📈 Histórico (últimos 10 registros):")
    for valor in historico[-10:]:
        print(f"• {round(valor, 2)} W")
    print("\n==============================================================================")
    time.sleep(2)