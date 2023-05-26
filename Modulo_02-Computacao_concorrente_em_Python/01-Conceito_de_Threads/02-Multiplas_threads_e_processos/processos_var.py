# script processos_var.py

from multiprocessing import Process

minha_lista = []


def funcao_a(indice):   # função que será paralelizada
    for _i in range(100000):
        minha_lista.append(1)
        print("Termino thread ", indice)


def main():
    tarefas = []

    # Criar 10 processos
    for indice in range(10):
        tarefa = Process(target=funcao_a, args=(indice,))   # Criar processos
        tarefas.append(tarefa)  # Armazenar processo criado
        tarefa.start()  # Iniciar

    print("Antes de aguardar o termino!", len(minha_lista))

    # Iterar lista tarefas
    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", len(minha_lista))


if __name__ == "__main__":
    main()
