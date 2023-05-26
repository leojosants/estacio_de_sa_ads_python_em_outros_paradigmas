import threading
import time

# Exemplo de função sem parâmetros


def funcao():
    for _i in range(3):
        print(f'{_i} - Executando a thread!')
        time.sleep(1)


def main():
    print("\nIniciando o programa!")

    threading.Thread(target=funcao).start()

    print("\nFinalizando o programa!")


if __name__ == "__main__":
    main()
