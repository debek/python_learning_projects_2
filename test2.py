import random

imiona = ["Burek", "Rex", "Reksio", "Diesel"]

def main():
    class AnimalException(Exception):
        pass

    class Zwierzak:
        wolne_imiona = set(imiona)
        print(wolne_imiona)

main()