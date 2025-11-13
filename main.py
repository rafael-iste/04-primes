"""
04-primes

Contient une fonction secondaire isprime permettant de tester si un entier est premier,
et une fonction principale affichant les nombres premiers inférieurs à 100 pour tester isprime.
"""

from math import sqrt

def isprime(p):
    """
    Vérifie si un entier est un nombre premier.

    Un nombre premier est un entier naturel supérieur ou égal à 2
    qui n'admet que deux diviseurs positifs distincts : 1 et lui-même.

    @param p: Entier à tester.
    @type p: int
    @return: True si p est un nombre premier, False sinon.
    @rtype: bool
    """
    if p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False

    limit = int(sqrt(p)) + 1
    for i in range(3, limit, 2):
        if p % i == 0:
            return False
    return True

def main():
    """
    Fonction principale du programme.

    Affiche la liste des nombres premiers inférieurs à 100 afin
    de vérifier le bon fonctionnement de la fonction secondaire.
    """

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
