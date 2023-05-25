# script funcao_filter.py
lista = [1, 2, 3, 4, 5]


def impar(item):
    return item % 2 != 0


def main():
    print(f"\nLista original = {lista}")

    nova_lista = filter(impar, lista)

    print(f"Nova lista = {list(nova_lista)} \n")


if __name__ == "__main__":
    main()


# Definimos a função ímpar, que retorna true se o item passado como parâmetro é ímpar
# ou false caso contrário (linhas 5 e 6).

# Utilizamos essa função, assim como a variável lista,
# como argumentos para a função filter (linha 12).

# A filter vai aplicar, internamente, a função passada como parâmetro em cada item da lista,
# retornando um novo iterável (que pode ser convertido em listas, tuplas etc.).
# O resultado da função filter é armazenado na variável nova_lista,
# para então ser impresso (linha 12).

# A função filter garante a imutabilidade dos iteráveis passados como argumento.
# Como a função filter retorna um iterável, utilizamos o construtor list(iterável)
# para imprimir o resultado (linha 14).
