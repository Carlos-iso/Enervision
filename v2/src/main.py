import os
from Aparelho import (
    Refrigerador,
    Chuveiro,
    ArCondicionado,
    LuzLED
)
from Casa import Casa


def menu():
    # os.system("cls" if os.name == "nt" else "clear")
    print("\n===== SISTEMA DE MONITORAMENTO ENERGÉTICO =====")
    print("1 - Adicionar aparelho")
    print("2 - Ligar / Desligar aparelho")
    print("3 - Listar aparelhos")
    print("4 - Exibir relatório energético")
    print("0 - Sair")


def criar_aparelho():
    print("\nTipos de aparelho:")
    print("1 - Refrigerador")
    print("2 - Chuveiro")
    print("3 - Ar-condicionado")
    print("4 - Luz LED")

    tipo = input("Escolha o tipo: ")

    nome = input("Nome do aparelho: ")
    potencia = float(input("Potência (W): "))
    horas = float(input("Horas de uso diário: "))
    local = input("Cômodo: ")
    if horas > 24:
        print("Maximo de horas é 24")
        print("Definindo horas para 24")
        horas = 24
    elif horas < 0:
        print("Minimo de horas é 0")
        print("Definindo horas para 0")
        horas = 0

    if potencia <= 0:
        print("Potência inválida. Deve ser maior que zero.")
        return

    if tipo == "1":
        temp = int(input("Temperatura (°C): "))
        return Refrigerador(nome, potencia, horas, local, temp)

    elif tipo == "2":
        temp = int(input("Temperatura da água (°C): "))
        return Chuveiro(nome, potencia, horas, local, temp)

    elif tipo == "3":
        temp = int(input("Temperatura desejada (°C): "))
        return ArCondicionado(nome, potencia, horas, local, temp)

    elif tipo == "4":
        qtd = int(input("Quantidade de lâmpadas: "))
        return LuzLED(nome, potencia, horas, local, qtd)

    else:
        print("Tipo inválido.")
        return None


def listar_aparelhos(casa):
    if not casa.aparelhos:
        print("\nNenhum aparelho cadastrado.")
        return

    print("\n=== APARELHOS CADASTRADOS ===")
    for i, a in enumerate(casa.aparelhos):
        status = "Ligado" if a._ativo else "Desligado"
        print(f"{i + 1} - {a.nome} ({status})")


def ligar_desligar_aparelho(casa):
    listar_aparelhos(casa)
    if not casa.aparelhos:
        print("Sem aparelho cadastrado")
        return

    try:
        idx = int(input("Escolha o índice do aparelho: "))
        if idx < 1 or idx > len(casa.aparelhos):
            print("Aparelho não encontrado")
            return
        idx_real = idx - 1
        aparelho = casa.aparelhos[idx_real]
        if aparelho._ativo:
            aparelho.desligar()
            print(f"{aparelho.nome} desligado.")
        else:
            aparelho.ligar()
            print(f"{aparelho.nome} ligado.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return


def main():
    casa = Casa("Casa De Carlos")
    while True:
        menu()
        opcao = input("Opção: ")

        if opcao == "1":
            aparelho = criar_aparelho()
            if aparelho:
                casa.adicionar_aparelho(aparelho)
                print("Aparelho adicionado com sucesso.")

        elif opcao == "2":
            ligar_desligar_aparelho(casa)

        elif opcao == "3":
            listar_aparelhos(casa)

        elif opcao == "4":
            try:
                custo = float(input("Informe o valor do kWh (R$): "))
                if custo <= 0:
                    raise ValueError
                casa.exibir_relatorio(custo)
            except ValueError:
                print("Valor inválido. Informe um número maior que zero.")

        elif opcao == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
