def main():

    # O que voce quer - Funcional
    def funcional():
        print("\nPrimeiro exemplo")
        numeros = [1, 2, 3, 4]
        print(f"\tTotal = {sum(numeros)}")

    # Segundo exemplo
    def segundo_exemplo():
        print("\nSegundo exemplo")
        print("\tTudo certo!" if True else '\tops')

    funcional()
    segundo_exemplo()


if __name__ == "__main__":
    main()
