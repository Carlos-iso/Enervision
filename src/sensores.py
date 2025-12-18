import random

# Lista que armazena os cômodos cadastrados
comodos = []

# Estado atual de consumo de cada cômodo (valor contínuo)
estado_comodos = {}

# Histórico de consumo de cada cômodo (lista de leituras anteriores)
historico_comodos = {}

def cadastrar_comodo(nome, potencia_maxima):
    """
    Cadastra um novo cômodo da casa no sistema de monitoramento.

    Cada cômodo funciona como um sensor virtual de consumo energético.

    Parâmetros:
    - nome (str): Nome do cômodo (ex: Sala, Cozinha)
    - potencia_maxima (float): Potência máxima estimada do cômodo em watts
    """
    comodo = {
        "nome": nome,
        "potencia_maxima": potencia_maxima
    }
    comodos.append(comodo)

    # Inicializa o consumo em um valor baixo (standby),
    # simulando equipamentos ligados porém ociosos
    estado_comodos[nome] = potencia_maxima * 0.1

    # Inicializa o histórico de consumo do cômodo
    historico_comodos[nome] = []

def _proximo_consumo(atual, potencia_maxima):
    """
    Calcula o próximo valor de consumo de forma realista e estável.

    Este modelo simula o comportamento real da energia elétrica:
    - Oscilações pequenas
    - Forte inércia (não muda bruscamente)
    - Desligamentos graduais
    - Respeito aos limites físicos do sistema

    Parâmetros:
    - atual (float): Consumo atual do cômodo
    - potencia_maxima (float): Potência máxima permitida

    Retorno:
    - float: Novo valor de consumo
    """

    # Define a variação máxima permitida (1% da potência)
    variacao_max = potencia_maxima * 0.01

    # Gera um pequeno ruído aleatório
    ruido = random.uniform(-variacao_max, variacao_max)

    # Aplica inércia: mudanças suaves e progressivas
    novo = atual + ruido * 0.3

    # Pequena chance de iniciar um desligamento gradual
    if random.random() < 0.01:
        novo = atual * 0.9

    # Limita quedas bruscas de consumo
    queda_max = potencia_maxima * 0.02
    novo = max(novo, atual - queda_max)

    # Garante que o consumo fique dentro dos limites físicos
    novo = max(0.0, min(novo, potencia_maxima))

    return round(novo, 2)

def ler_consumos():
    """
    Atualiza e retorna as leituras de consumo de todos os cômodos.

    Para cada cômodo:
    - Calcula o próximo consumo
    - Atualiza o estado atual
    - Armazena o histórico recente
    - Retorna os dados formatados

    Retorno:
    - list[dict]: Lista de leituras por cômodo
    """
    leituras = []

    for comodo in comodos:
        nome = comodo["nome"]
        potencia_max = comodo["potencia_maxima"]

        # Obtém o consumo atual
        atual = estado_comodos[nome]

        # Calcula o novo consumo
        novo_consumo = _proximo_consumo(atual, potencia_max)

        # Atualiza o estado interno
        estado_comodos[nome] = novo_consumo

        # Atualiza o histórico do cômodo
        historico_comodos[nome].append(novo_consumo)

        # Mantém apenas os últimos 15 registros
        if len(historico_comodos[nome]) > 15:
            historico_comodos[nome].pop(0)

        # Adiciona leitura formatada
        leituras.append({
            "nome": nome,
            "consumo": novo_consumo,
            "potencia_maxima": potencia_max
        })

    return leituras

def obter_historico_comodos():
    """
    Retorna o histórico de consumo de todos os cômodos.

    Retorno:
    - dict: Histórico de consumo por cômodo
    """
    return historico_comodos