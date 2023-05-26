import threading
import time


def funcao(mensagem):
    for _i in range(3):
        print(f"{_i} - {mensagem}")
        time.sleep(1)


def main():
    print("\nIniciando o programa!")

    _x = threading.Thread(target=funcao, args=("Executando!", ))
    _x.start()

    print("\nFinalizando o programa!")


if __name__ == "__main__":
    main()
