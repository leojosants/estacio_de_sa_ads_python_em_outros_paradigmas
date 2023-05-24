# script anonima.py (versão alterada do script funcao5.py)
def multiplicar_por(multiplicador):
    return lambda multiplicando: multiplicando * multiplicador


def main():
    multiplicador_10 = 10
    multiplicador_5 = 5
    multiplicando_1 = 1
    multiplicando_2 = 2

    multiplicar_por_10 = multiplicar_por(multiplicador_10)
    print(multiplicar_por_10(multiplicando_1))
    print(multiplicar_por_10(multiplicando_2))

    multiplicar_por_5 = multiplicar_por(multiplicador_5)
    print(multiplicar_por_5(multiplicando_1))
    print(multiplicar_por_5(multiplicando_2))


if __name__ == "__main__":
    main()
