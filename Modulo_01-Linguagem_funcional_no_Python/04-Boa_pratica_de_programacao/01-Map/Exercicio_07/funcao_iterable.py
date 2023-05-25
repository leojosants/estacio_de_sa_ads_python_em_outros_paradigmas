# script funcao_iterable.py
lista = [1, 2, 3, 4, 5]


def triplica_itens(iterable):
    lista_aux = []

    for item in iterable:
        lista_aux.append(item * 3)

    return lista_aux


def main():
    print(f"\nLista original = {lista}")

    nova_lista = triplica_itens(lista)

    print(f"Nova lista = {nova_lista} \n")


if __name__ == "__main__":
    main()

# Definimos uma função chamada triplica_itens, que recebe um iterável como parâmetro (linha 5)
# Cria uma lista auxiliar para garantir imutabilidade (linha 6)
# Percorre os itens do iterável passado como parâmetro (linha 8)
# Adiciona os itens triplicados à lista auxiliar (linha 9) e retorna a lista auxiliar (linha 11).
# Essa função é chamada com o argumento lista (linha 11) e o resultado é impresso (linha 12).
