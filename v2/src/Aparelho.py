from abc import ABC, abstractmethod

class Aparelho(ABC):
    def __init__(self, nome, potencia_watts, horas_diarias, localizacao):
        self.nome = nome
        self.potencia_watts = potencia_watts
        self.horas_diarias = horas_diarias
        self.localizacao = localizacao
        self._ativo = True

    @property
    def potencia_watts(self):
        return self._potencia_watts

    @potencia_watts.setter
    def potencia_watts(self, valor):
        if valor <= 0:
            raise ValueError("Potencia inválida. Deve ser maior que zero.")
        self._potencia_watts = float(valor)

    def ligar(self):
        self._ativo = True

    def desligar(self):
        self._ativo = False

    def calcular_consumo_mensal(self):
        if not self._ativo:
            return 0
        return (self.potencia_watts / 1000) * self.horas_diarias * 30

    def obter_informacoes(self):
        return (
            f"{self.nome} | "
            f"Local: {self.localizacao} | "
            f"Consumo: {self.calcular_consumo_mensal():.2f} kWh/mês"
        )

    @abstractmethod
    def sugerir_economia(self):
        pass

class Refrigerador(Aparelho):
    def __init__(self, nome, potencia_watts, horas_diarias, localizacao, temperatura_celsius):
        super().__init__(nome, potencia_watts, horas_diarias, localizacao)
        self.temperatura_celsius = temperatura_celsius

    def sugerir_economia(self):
        return (
            f"Ajuste a temperatura para -2°C. "
            f"Consumo atual: {self.calcular_consumo_mensal():.2f} kWh/mês"
        )

class Chuveiro(Aparelho):
    def __init__(self, nome, potencia_watts, horas_diarias, localizacao, temperatura_agua):
        super().__init__(nome, potencia_watts, horas_diarias, localizacao)
        self.temperatura_agua = temperatura_agua

    def sugerir_economia(self):
        economia = self.calcular_consumo_mensal() * 0.18
        return f"Reduza o tempo de banho: economize {economia:.2f} kWh/mês"

class ArCondicionado(Aparelho):
    def __init__(self, nome, potencia_watts, horas_diarias, localizacao, temperatura_setpoint):
        super().__init__(nome, potencia_watts, horas_diarias, localizacao)
        self.temperatura_setpoint = temperatura_setpoint

    def sugerir_economia(self):
        economia = self.calcular_consumo_mensal() * 0.12
        return f"Aumente a temperatura em 2°C: economize {economia:.2f} kWh/mês"

class LuzLED(Aparelho):
    def __init__(self, nome, potencia_watts, horas_diarias, localizacao, quantidade_lampadas):
        super().__init__(nome, potencia_watts, horas_diarias, localizacao)
        self.quantidade_lampadas = quantidade_lampadas

    def calcular_consumo_mensal(self):
        if not self._ativo:
            return 0
        consumo_unitario = (self.potencia_watts / 1000) * self.horas_diarias * 30
        return consumo_unitario * self.quantidade_lampadas

    def sugerir_economia(self):
        economia = self.calcular_consumo_mensal() * 0.30
        return f"Use luz natural: economize {economia:.2f} kWh/mês"