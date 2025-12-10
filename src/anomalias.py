def detectar_anomalia(historico):
    if len(historico) < 5:
        return False
    media = sum(historico) / len(historico)
    ultimo = historico[-1]
    return ultimo > media * 1.5