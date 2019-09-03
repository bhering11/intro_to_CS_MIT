# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 08:29:18 2019

@author: tdomi
"""

# obj: ver quantos "bob" aparecem em um string s

# inicie a contagem
nbob = 0

# percorra todos os elementos de s
for i in range(len(s)):
# se passarmos do último elemento, termine o loop    
    if (i+3) > len(s):
        break
# veja se cada 3 letras em sequencia são iguais a bob    
    if s[i:(i+3)] == "bob":
# adicione ao contador se for        
        nbob += 1

# imprima o resultado
print("Number of times bob occurs is: " + str(nbob))
