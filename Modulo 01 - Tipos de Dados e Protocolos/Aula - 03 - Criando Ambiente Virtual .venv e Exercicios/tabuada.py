#!/usr/bin/env python3

"""Imprime a tabuada do 1 ao 10."""

"""

__version__ = "0.1.0"
__author__ = "Romullo"

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros = list(range(1, 11))

# Iterable (percorriveis)
# Para cada numeros em numeros:

for numero in numeros:
    print("Tabuada do: ", numero)
    for outro_numero in numeros:
        print(numero, " x ", outro_numero, " = " ,  numero * outro_numero)
    print("-" * 12)  

"""
    
__version__ = "0.1.1"
__author__ = "Romullo"

numeros = list(range(1,11))

for n1 in numeros:
    print("{:-^20}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^20}".format(f"{n1} x {n2} = {resultado}")) 
    print()   
    print("#" * 20)