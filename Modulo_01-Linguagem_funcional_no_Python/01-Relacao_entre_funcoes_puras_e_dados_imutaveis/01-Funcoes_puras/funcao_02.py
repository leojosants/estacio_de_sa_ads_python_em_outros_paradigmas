valor = 20


def multiplica(valor, fator):
    valor = valor * fator
    return valor


def main():
    numero = int(input("\nDigite um valor inteiro: "))
    print(f"Resultado = {multiplica(valor, numero)}")
    print(f"Resultado = {multiplica(valor, numero)} \n")


if __name__ == "__main__":
    main()
