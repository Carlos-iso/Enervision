from sensores import ler_consumo
from previsao import detectar_pico
from otimizador import otimizar
from anomalias import detectar_anomalia
from relatorios import exibir
import time
import os
historico = []
while True:
    os.system("cls" if os.name == "nt" else "clear")
    consumo = ler_consumo()
    historico.append(consumo)
    pico = detectar_pico(consumo)
    consumo_otimizado = otimizar(consumo)
    anomalia = detectar_anomalia(historico)
    exibir(consumo, consumo_otimizado, pico, anomalia)
    time.sleep(2)