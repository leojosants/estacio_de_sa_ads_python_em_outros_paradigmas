from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def main():
    print(f"\nLista original: {numeros}")

    soma_total = reduce((lambda x, y: x + y), numeros)
    print(f"A soma de todos os elementos da lista é: {soma_total}")


if __name__ == "__main__":
    main()
