import random
sensores = []
def cadastrar_sensor(nome, potencia_maxima):
    sensor = {
        "nome": nome,
        "potencia_maxima": potencia_maxima
    }
    sensores.append(sensor)
def listar_sensores():
    return sensores
def ler_consumos():
    leituras = []
    for sensor in sensores:
        consumo = round(random.uniform(0, sensor["potencia_maxima"]), 2)
        leituras.append({
            "nome": sensor["nome"],
            "consumo": consumo,
            "potencia_maxima": sensor["potencia_maxima"]
        })
    return leituras