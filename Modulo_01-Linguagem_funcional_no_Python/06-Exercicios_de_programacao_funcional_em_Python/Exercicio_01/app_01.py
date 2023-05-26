veiculos = ['aviao', 'carro', 'navio', 'onibus']


def transforma_em_maiusculo(lista):
    return lista.upper()


def main():

    # Transformar em uma lista, pois o map gera um objeto
    nova_lista = list(map(transforma_em_maiusculo, veiculos))

    print(f"\nLista original: {veiculos}")
    print(f"Nova lista: {nova_lista}")


if __name__ == "__main__":
    main()
