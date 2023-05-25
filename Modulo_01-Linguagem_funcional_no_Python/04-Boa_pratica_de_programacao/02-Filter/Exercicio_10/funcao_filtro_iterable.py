# script funcao_filtro_iterable.py
lista = [1, 2, 3, 4, 5]


def impares(iterable):
    lista_aux = []

    for item in iterable:
        if item % 2 != 0:
            lista_aux.append(item)

    return lista_aux


def main():
    print(f"\nLista original = {lista}")

    nova_lista = impares(lista)

    print(f"Nova lista = {nova_lista} \n")


if __name__ == "__main__":
    main()

# Definimos uma função chamada ímpares, que recebe um iterável como parâmetro (linha 5).
# Cria uma lista auxiliar para garantir imutabilidade (linha 6).
# Percorre os itens do iterável passados como parâmetros (linha 8)
# Adiciona os itens ímpares à lista auxiliar (linhas 10) e retorna a lista auxiliar (linha 12).
# Essa função é chamada com o argumento lista (linha 18) e o resultado é impresso (linha 20).
