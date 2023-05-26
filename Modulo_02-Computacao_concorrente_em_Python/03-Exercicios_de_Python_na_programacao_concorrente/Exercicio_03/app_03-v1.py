from threading import Thread
from time import sleep


def realizar_operacoes(tempo_espera, operacao, numero):
    print(f"-> Iniciando o cálculo de {numero} ao {operacao}")

    if operacao == "cubo":
        print(f"\tO cubo de {numero} é {numero ** 3}")
    else:
        print(f"\tO quadrado de {numero} é {numero ** 4}")

    sleep(tempo_espera)
    print(f"-> Conclusão do cálculo {operacao}")


def main():
    print("\nExecução iniciada das Threads!")

    thread_1 = Thread(
        target=realizar_operacoes, args=(3, "cubo", 2))
    thread_1.start()

    thread_2 = Thread(
        target=realizar_operacoes, args=(2, "quadrado", 2))
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("Execução concluída das Threads! \n")


if __name__ == "__main__":
    main()
