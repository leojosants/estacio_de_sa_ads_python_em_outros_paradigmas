# script funcao3.py

# captando os valores do campo Input
valores = input("\nInforme os valores separados por espaço: ")

""" Separando os valores pelo espaço em branco e transformando-os em uma lista de inteiros  """
valores = [int(i) for i in valores.split()]


def altera_lista(lista):
    lista[2] = lista[2] + 10
    return lista


def main():
    print(f"Lista original = {valores}")
    print(f"Nova lista = {altera_lista(valores)}")
    print(f"Nova lista = {altera_lista(valores)} \n")


if __name__ == "__main__":
    main()
