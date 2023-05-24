def multiplicar(_a, _b):
    return _a * _b


def multiplicar_lambda(_a, _b):
    return lambda resultado: _a * _b


def main():
    _a = 10
    _b = 20

    resultado = multiplicar(_a, _b)
    resultado_lambda = multiplicar_lambda(_a, _b)

    print(f"\nA multiplicação entre {_a} e {_b} é: {resultado}")
    print(f"A multiplicação entre {_a} e {_b} é: {resultado_lambda} \n")


if __name__ == "__main__":
    main()
