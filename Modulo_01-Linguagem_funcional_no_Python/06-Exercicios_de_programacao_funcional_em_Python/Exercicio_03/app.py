lista_numeros = [9.56783, 7.57568, 3.00914, 6.2321]
lista_precisao = [2, 3, 3, 3]


def main():
    nova_lista = list(map(lambda x, y: round(
        x, y), lista_numeros, lista_precisao))
    print(f"\nLista original: {lista_numeros}")
    print(f"Nova lista: {nova_lista}")


if __name__ == "__main__":
    main()
