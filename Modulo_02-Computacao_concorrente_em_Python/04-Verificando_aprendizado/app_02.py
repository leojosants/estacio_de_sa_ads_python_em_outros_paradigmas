# script processos.py
from threading import Thread
from multiprocessing import Process

minha_lista = []


def adiciona():
    for _indice in range(100):
        minha_lista.append(1)


def main():
    tarefas = []

    for indice in range(10):
        _t = Thread(target=adiciona)
        tarefas.append(_t)
        _t.start()

    for indice in range(10):
        _p = Process(target=adiciona)
        tarefas.append(_p)
        _p.start()

    for tarefa in tarefas:
        tarefa.join()

    print(f"\n{len(minha_lista)} \n")


if __name__ == '__main__':
    main()
