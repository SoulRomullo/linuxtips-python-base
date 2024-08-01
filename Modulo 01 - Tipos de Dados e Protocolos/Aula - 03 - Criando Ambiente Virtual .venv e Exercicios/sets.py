#!/usr/bin/env python3

"""

    Trabalhando com SET conhecido como Conjunto 
    Como criar um set fazemos dessa forma usando o Terminal IPYTHON3
    -$ c1 = {1, 2, 3}
    -$ type(c1)

    Para melhor ser aplicado o SET, é aconsenhavél usar o comando dessa maneira
    -$ c1 = set() --> dentro das colchetes passar os valores
    -$ c1 = set([1, 2, 3]) --> dentro do SET podemos tanto passar LIST ou Tupla

    Para unir duas listas destintas em apenas um SET com os valores ultilizamos dessa forma
    -$ conjunto_a = [1, 2, 3, 4, 5]
    -$ conjunto_b = [4, 5, 6, 7, 8]

    -$ set(conjunto_a) | set(conjunto_b)

    Ou pode ser feito dessa maneira
    -$ set(conjunto_a).union(set(conjunto_b))

    Podemos também fazer dessa fornma declarando o SET antes de fazer a união
    -$ conjunto_a = set([1, 2, 3, 4, 5])
    -$ conjunto_b = set([4, 5, 6, 7, 8])

    -$ conjunto_a | conjunto_b

    Ou 

    conjunto_a.union(conjunto_b)

    Para verificar se tem numeros iguais no conjunto_a e conjunto_b fazemos uma intersection dessa forma
    -$ conjunto_a = set([1, 2, 3, 4, 5])
    -$ conjunto_b = set([4, 5, 6, 7, 8])

    -$ conjunto_a.intersection(conjunto_b)

    Ou pode ser dessa forma
    
    -$ conjunto_a & conjunto_b

    Para verificar quais os numeros que tem no conjunto_a e não tem no conjunto conjunto_b fazemos dessa forma
    -$ conjunto_a = set([1, 2, 3, 4, 5])
    -$ conjunto_b = set([4, 5, 6, 7, 8])

    -$ conjunto_a.difference(conjunto_b)

    Ou pode ser dessa forma
    
    -$ conjunto_a - conjunto_b
    
    Para a diferença assimétrica ele pega dodos todos os elementos do conjunto_a e do conjunto_b dessa forma, a ordem faz a diferênça
    
    -$ conjunto_a.symmetric_difference(conjunto_b)
    
    ou pode ser dessa forma
    
    -$ conjunto_a ^ conjunto_b

    Dá para colocar os elementos dentro so SET adicionando com o add
    declaramos a variável e setamos ela como SET como no exemplo abaixo
    -$ c1 = set()
    inserido valores
    -$ c1.add(1) --> Passamos o valor dentro do add
    -$ c1.add(2)
    -$ c1.add(3)

    Conhecendo Hash Table
    Criando uma list
    -$ numeros = [1,2,3,4,1,1,1,7,8,9]

    Para fazer uma verificação de numeros contendo dentro da lista pode demorar muito então usamos o comando SET para 
    Remover os numeros duplicados e fazer uma busca mais eficiente como no exemplo abaixo
    
    -$ numeros = set([1,2,3,4,1,1,1,7,8,9])

    Esse modelo e representado como O(1) ou constante
"""

c1 = {1, 2, 3}
print(type(c1))

print("-" * 20)

c1 = set("banana") # --> Neste caso ele fatia a palavra e não trás os carecteres em ordem, 
print(c1)          # --> ele só retorna os carecteres e não repete os carecteres iguais.

print("-" * 20)

conjunto_a = [1, 2, 3, 4, 5]
conjunto_b = [4, 5, 6, 7, 8]

print(set(conjunto_a) | set(conjunto_b))
print(set(conjunto_a).union(set(conjunto_b)))

print("-" * 20)

conjunto_a = set([1, 2, 3, 4, 5])
conjunto_b = set([4, 5, 6, 7, 8])

print(conjunto_a.intersection(conjunto_b))
print(conjunto_a & conjunto_b)

print("-" * 20)

print(conjunto_a.difference(conjunto_b))
print(conjunto_a - conjunto_b)

print("-" * 20)

print(conjunto_a.symmetric_difference(conjunto_b))
print(conjunto_a ^ conjunto_b)

print("-" * 20)

c1 = set()
c1.add(1) # --> Se você tentar setar o mesmo valor várias vezes o SET não irá deixar acontecer isso
c1.add(1)
c1.add(1)
c1.add(1)
c1.add(2)
c1.add(3)

print(type(c1))
print(c1)
