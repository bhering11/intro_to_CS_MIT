# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

# obj: count the number of vowels

# inicializar uma contagem
nvwls = 0

# um loop que vá nos elementos de s
for i in s:
# caso um dos elementos seja uma vogal, adicionar 1 ao contador
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        nvwls += 1

# imprimir o contador
print("Number of vowels: " + str(nvwls))