import threading
import time

from urllib.request import urlopen
# import urllib2

# O Python "ModuleNotFoundError: No module named 'urllib2'" ocorre
# porque o urllib2módulo foi dividido em urllib.requeste urllib.responseno Python 3.
# Para resolver o erro, importe o módulo como from urllib.request import urlopen.
# https://bobbyhadz.com/blog/python-no-module-named-urllib2

start = time.time()
urls = ["http://www.google.com", "http://www.Apple.com",
        "http://www.Microsofit.com", "http://www.instagram.com"]


def chama_url(url):

    # req = urllib2.Request(url)
    # response = urllib2.urlopen(url)
    req_res = urlopen(url)
    the_page = req_res.read()

    print("'%s\' carregado em %ss" % (url, (time.time() - start)))
    # print(the_page)


def main():
    threads = [threading.Thread(target=chama_url, args=(url,)) for url in urls]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Elapsed Time: %s" % (time.time() - start))


if __name__ == "__main__":
    main()
