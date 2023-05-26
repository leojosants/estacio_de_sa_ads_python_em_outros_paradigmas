from threading import Thread
from time import sleep


def calcular_cubo(tempo_espera, numero, mensagem):
    print(f"-> Iniciando o cálculo '{mensagem}'...")
    print(f"\tO cubo de {numero} é {numero ** 3}")
    sleep(tempo_espera)
    print(f"-> Conclusão do cálculo '{mensagem}'...")


def calcular_quadrado(tempo_espera, numero, mensagem):
    print(f"-> Iniciando o cálculo '{mensagem}'...")
    print(f"\tO Quadrado de {numero} é {numero ** 2}")
    sleep(tempo_espera)
    print(f"-> Conclusão do cálculo '{mensagem}'...")


def main():
    print("\nExecução iniciada das Threads!")

    thread_1 = Thread(
        target=calcular_cubo, args=(3, 5, "CUBO"))
    thread_1.start()

    thread_2 = Thread(
        target=calcular_quadrado, args=(2, 5, "QUADRADO"))
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("Execução concluída das Threads! \n")


if __name__ == "__main__":
    main()
