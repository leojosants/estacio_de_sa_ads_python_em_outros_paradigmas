import operator
from functools import reduce


def main():

    def sum(numeros):
        if not numeros:
            return 0
        primeiro = numeros[0]
        resto = numeros[1:]
        return primeiro + sum(resto)

    def segundo_exemplo():
        lista = ["ferrari"]
        nova_lista = lista + ["porche"]
        print(f"\t{nova_lista}")

    def terceito_exemplo():
        print(f"\t{operator.add(10, 20)}")

    def quarto_exemplo():
        print(f"\t{reduce(operator.add, [10, 20])}")
        print(f"\t{reduce(operator.concat, ['Aprendendo reduce!'])}")

    print("\nPrimeiro exemplo")
    print(f"\t{sum([2, 4, 8, 10])}")

    print("\nSegundo exemplo")
    segundo_exemplo()

    print("\nTerceiro exemplo")
    terceito_exemplo()

    print("\nQuarto exemplo")
    quarto_exemplo()


if __name__ == "__main__":
    main()
