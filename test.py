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
    #
    # #2. dekorator zbierający w listę
    #
    # class ListaObiektow:
    #     def __init__(self):
    #         self.lista = []
    #
    #     def dodaj_do_listy(self, x):
    #         """ Dekorator, możliwy do użycia na obiekcie i funkcji.
    #         Nie modyfikuje obiektu/funkcji, a jedynie dodaje go do self.lista"""
    #         # self.lista.append(print(args[0].__name__))
    #         self.lista.append(x)
    #         return x
    #
    # widoki = ListaObiektow()
    #
    # @widoki.dodaj_do_listy
    # def home(request):
    #     return "Witaj na stronie"
    #
    # @widoki.dodaj_do_listy
    # def greet(request):
    #     return "Witaj, twój request to " + str(request)
    #
    # assert home in widoki.lista
    # # print(home)
    # # print(widoki.lista)
    #
    # assert greet in widoki.lista
    # # print(greet)
    # # print(widoki.lista)
    #
    # assert home(None) == "Witaj na stronie"
    # # print(home(None))
    #
    # assert greet(1) == "Witaj, twój request to 1"
    # # print(greet(1))

    # 3. fabryka fukncji-kluczy do sortowania

    l = ["Ala", "pies", "kot", "i tak dalej", "..."]
    l.sort(key=len)  # to by posortowało po długości
    l.sort(key=lambda x: x[1])  # to by posortowało po drugiej literze

    def fabryka_funkcji_pobierajacych_dana_litere(idx_litery):
        def sortowanie(x):
            return x.sort(x[idx_litery])
        # zadanie dodatkowe: jeśli jest za mało liter to podać ostatnią

    a = l.sort(key=fabryka_funkcji_pobierajacych_dana_litere(0))  # ma sortowac po pierszej literze
    print(a)
    b = l.sort(key=fabryka_funkcji_pobierajacych_dana_litere(1))  # ma sortowac po pierszej literze

    # assert fabryka_funkcji_pobierajacych_dana_litere(0)("Abcd") == "A"
    # assert fabryka_funkcji_pobierajacych_dana_litere(2)("Abcd") == "c"

if __name__ == '__main__':
    main()

