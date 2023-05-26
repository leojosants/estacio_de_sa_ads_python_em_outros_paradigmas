# script principal.py
from threading import Thread
from multiprocessing import Process


def funcao_a(nome):
    print(nome)


def main():
    _t = Thread(target=funcao_a, args=("Minha Thread",))
    _t.start()

    _p = Process(target=funcao_a, args=("Meu Processo",))
    _p.start()


if __name__ == '__main__':
    main()


# Criando uma thread e um processo que executam a mesma função.
#
# Na linha 11, criamos uma thread para executar a função funcao_a utilizando a classe thread.
# O construtor tem como parâmetros a função que deverá ser executada (target) e
# quais parâmetros serão passados para essa função (args).
# O parâmetro args espera um iterável (lista, tupla etc.), onde cada elemento será mapeado
# para um parâmetro da função target.
#
# Como a funcao_a espera apenas um parâmetro, definimos uma tupla de apenas
# um elemento (‘Minha Thread”).
# O primeiro elemento da tupla, a string Minha Thread, será passada para
# o parâmetro nome da funcao_a.
#
# Na linha 12, enviamos o comando para a thread iniciar sua execução,
# chamando o método start() do objeto t do tipo thread,
#
# A criação do processo é praticamente igual, porém utilizando a classe process,
# conforme a linha 14.
# Para iniciar o processo, chamamos o método start() na linha 15.
