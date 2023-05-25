# script funcao_map.py
lista = [1, 2, 3, 4, 5]


def triplica(item):
    return item * 3


def main():
    print(f"\nLista original = {lista}")

    nova_lista = map(triplica, lista)

    print(f"Nova lista = {list(nova_lista)} \n")


if __name__ == "__main__":
    main()

# Definimos a função triplica, que triplica e retorna o item passado como parâmetro (linhas 5 e 6).
# É utilizada, assim como a variável lista, como argumentos para a função map (linha 12).

# A map vai aplicar internamente a função passada como parâmetro em cada item da lista,
# retornando um novo iterável(que pode ser convertido em listas, tuplas etc.).
# O resultado da função map é armazenado na variável nova_lista, para então ser impresso (linha 12).

# A função map garante a imutabilidade dos iteráveis passados como argumento.
# Como a função map retorna um iterável, utilizamos o construtor list (iterável)
# para imprimir o resultado (linha 14).
