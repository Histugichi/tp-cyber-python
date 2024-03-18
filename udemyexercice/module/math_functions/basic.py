# Dans le fichier basic.py

def factorielle(n):
    """Calcule la factorielle d'un entier n"""
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)