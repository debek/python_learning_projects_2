import time

def main():
    # #1. dekorator liczący czas
    # # w środku rozwiązania znajdzie się:
    #
    # def liczik_czasu(func):
    #     def inner():
    #         time_start = time.perf_counter()
    #         func()
    #         time_end = time.perf_counter()
    #         print("Wywołanie funkcji zajęło", time_end - time_start)
    #     return inner
    #
    # @liczik_czasu
    # def test():
    #     print("Testowa apka")
    #
    # test()

    #2. dekorator zbierający w listę

    class ListaObiektow:
        def __init__(self):
            self.lista = []

        def dodaj_do_listy(self, *args, **kwargs):
            """ Dekorator, możliwy do użycia na obiekcie i funkcji.
            Nie modyfikuje obiektu/funkcji, a jedynie dodaje go do self.lista"""
            self.lista.append(print(args[0].__name__))

    widoki = ListaObiektow()

    @widoki.dodaj_do_listy
    def home(*args, **kwargs):
        def inner(*args, **kwargs):
            return "Witaj na stronie"
        return inner

    @widoki.dodaj_do_listy
    def greet(request):
        return "Witaj, twój request to " + str(request)

    assert home in widoki.lista
    # print(home)
    # print(widoki.lista)

    assert greet in widoki.lista
    # print(greet)
    # print(widoki.lista)

    # assert home(None) == "Witaj na stronie"
    # print(home(None))

    # assert greet(1) == "Witaj, twój request to 1"
    print(greet(1))

if __name__ == '__main__':
    main()

