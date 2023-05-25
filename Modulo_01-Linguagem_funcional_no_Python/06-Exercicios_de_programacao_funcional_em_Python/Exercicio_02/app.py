lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(f"\nlista original: {lista}")


def retorna_pares(item):
    return item % 2 == 0


def main():
    lista_de_pares_1 = list(filter(retorna_pares, lista))
    print(f"Nova lista: {lista_de_pares_1}")

    lista_de_pares_2 = list(filter(lambda item: item % 2 == 0, lista))
    print(f"Nova lista: {lista_de_pares_2}")


if __name__ == "__main__":
    main()
