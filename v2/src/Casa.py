class Casa:
    def __init__(self, comodo):
        self.comodo = comodo
        self.aparelhos = []

    def adicionar_aparelho(self, aparelho):
        self.aparelhos.append(aparelho)

    def consumo_total(self):
        return sum(a.calcular_consumo_mensal() for a in self.aparelhos)

    def aparelhos_ordenados_por_consumo(self):
        return sorted(
            self.aparelhos,
            key=lambda a: a.calcular_consumo_mensal(),
            reverse=True
        )

    def exibir_relatorio(self, custo_kwh):
        print("=" * 50)
        print(f"RELATÓRIO ENERGÉTICO - {self.comodo}")
        print("=" * 50)
        if not custo_kwh:
            print("Valor kW/h Não Cadastrado")
            return

        print("\n=== APARELHOS ORDENADOS POR CONSUMO ===\n")
        for a in self.aparelhos_ordenados_por_consumo():
            print(f"{a.nome}: {a.calcular_consumo_mensal():.2f} kWh/mês")

        total = self.consumo_total()
        print(f"\nCONSUMO TOTAL MENSAL: {total:.2f} kWh")
        print(f"Custo estimado (R$ {custo_kwh:.2f}/kWh): R$ {total * custo_kwh:.2f}")

        print("\n=== RECOMENDAÇÕES DE ECONOMIA ===\n")
        for a in self.aparelhos:
            print(a.sugerir_economia())
    
    def __repr__(self) -> str:
        a = self.aparelhos_ordenados_por_consumo()
        return (f"Aparelho(nome='{a.nome}', potencia_watts={a.potencia_watts}, "
                f"horas_diarias={a.horas_diarias}, localizacao='{a.localizacao}', ativo={a.ativo})")