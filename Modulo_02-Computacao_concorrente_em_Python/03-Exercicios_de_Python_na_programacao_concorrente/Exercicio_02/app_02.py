from threading import Thread
from time import sleep


def tarefa(tempo_espera, nome_da_tarefa):
    print(f"Iniciando a tarefa {nome_da_tarefa}")
    sleep(tempo_espera)
    print(f"Conclusão da tarefa {nome_da_tarefa}")


def main():
    print()

    thread_1 = Thread(
        target=tarefa, args=(3, "A"))
    thread_1.start()

    thread_2 = Thread(
        target=tarefa, args=(2, "B"))
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("Execução concuída das Threads! \n")


if __name__ == "__main__":
    main()
