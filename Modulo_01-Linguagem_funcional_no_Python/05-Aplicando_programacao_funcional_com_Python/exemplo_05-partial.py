import collections
import operator
from functools import partial
from operator import attrgetter


def main():

    def primeiro_exemplo():
        adiciona_um = partial(operator.add, 1)
        print(f"\t{adiciona_um(5)}")

    def segundo_exemplo():
        pessoa = collections.namedtuple("pessoa", "nome idade")
        pessoas = [pessoa("Joao", 40), pessoa("Ana", 20), pessoa("Renata", 25)]
        print(f"\t{sorted(pessoas, key=attrgetter('nome'))}")
        print(f"\t{sorted(pessoas, key=attrgetter('idade'))}")

    def terceito_exemplo():
        pessoa = collections.namedtuple("pessoa", "nome idade")
        pessoas = [pessoa("Joao", 40), pessoa("Ana", 20), pessoa("Renata", 25)]
        sort_nome = partial(sorted, key=attrgetter("nome"))
        sort_idade = partial(sorted, key=attrgetter("idade"))
        print(f"\t{sort_nome(pessoas)}")
        print(f"\t{sort_idade(pessoas)}")

    print("\nPrimeiro exemplo")
    primeiro_exemplo()

    print("\nSegundo exemplo")
    segundo_exemplo()

    print("\nTerceiro exemplo")
    terceito_exemplo()


if __name__ == "__main__":
    main()
