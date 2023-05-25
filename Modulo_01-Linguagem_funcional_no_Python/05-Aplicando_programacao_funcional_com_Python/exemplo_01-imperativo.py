def main():

    # Como fazer - imperativo #
    def imperativo():
        numeros = [1, 2, 3, 4]
        total = 0
        for numero in numeros:
            total += numero
        print(f"\tTotal = {total}")

    # Segundo exemplo #
    def segundo_exemplo():
        if True:
            print("\tTudo certo")
        else:
            print("\tops")

    print("\nPrimeiro exemplo")
    imperativo()

    print("\nSegundo exemplo")
    segundo_exemplo()


if __name__ == "__main__":
    main()
