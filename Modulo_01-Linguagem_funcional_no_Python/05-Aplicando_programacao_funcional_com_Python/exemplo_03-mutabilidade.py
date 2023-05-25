def main():

    # Mutabilidade
    def sum(numeros):
        print("\nPrimeiro exemplo")
        total = 0
        for numero in numeros:
            total += numero
        return total

    # Segundo exemplo #
    def segundo_exemplo():
        print("\nSegundo exemplo")
        lista = ["ferrari"]
        print(f"\t{lista}")

        lista.append("porche")
        print(f"\t{lista}")

    print(f"\tTotal = {sum([2, 4, 6, 8, 10])}")
    segundo_exemplo()


if __name__ == "__main__":
    main()
