import threading
import time

# Sincronizando threads
ls = []


def contador_1(n):
    for _i in range(1, n + 1):
        print(_i)
        ls.append(_i)
        time.sleep(0.4)


def contador_2(n):
    for _i in range(6, n + 1):
        print(_i)
        ls.append(_i)
        time.sleep(0.5)


def main():
    _x = threading.Thread(target=contador_1, args=(5,))
    _x.start()
    _x.join()

    _y = threading.Thread(target=contador_2, args=(10,))
    _y.start()
    _y.join()

    print()
    print(ls)


if __name__ == "__main__":
    main()
