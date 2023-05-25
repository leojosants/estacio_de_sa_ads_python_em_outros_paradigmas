# script funcao_filter_lambda.py
lista = [1, 2, 3, 4, 5]

nova_lista = filter(lambda item: item % 2 != 0, lista)


def main():
    print(f"\nLista original = {lista}")
    print(f"Nova lista = {list(nova_lista)} \n")


if __name__ == "__main__":
    main()

# Substituímos a função ímpar pela função lambda (lambda item: item%2 != 0)
# que foi utilizada como argumento para a função filter (linha 4).
# Esta vai aplicar a função lambda em cada item da lista, retornando um novo iterável
# que foi impresso posteriormente (linha 9).
