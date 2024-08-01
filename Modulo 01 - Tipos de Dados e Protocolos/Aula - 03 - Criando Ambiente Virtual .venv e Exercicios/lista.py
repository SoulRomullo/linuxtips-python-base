#!/usr/bin/env python3

"""
    Trabalhando com Listas que são conhecidas como array ou vetores
    
    Para criar uma list fazemos dessa forma
    -$ users = []
    
    Para saber o tipo dessa variável usamos o seguinte comando
    -$ type(users)
    
    Para adicionar um dados dentro da list usamos o seguinte comando 
    -$ users.append("Bruno") --> Sempre os dados será inserido no final da list
    
    Para inserir um dados na list e escolher a posição que ele irá ser inserido usamos o seguinte comando
    -$ users.insert(0, "Miguel") --> Passamos a posição e dado a ser inserido

    Para remover um dados da list devemos usar o seguinte comando
    -$ users.remove("Alice")
    
    Podemos usar esse comando para pegar o primeiro dados, o dados do meio e o ultimo dessa forma
    head, *body, tail = users

    Podemos juntar duas list em uma única list como no exemplo abaixo
    -$ users = ["Paulo", "Pedro"]
    -$ outra_lista = ["Tiago", "João"]

    -$ users + outra_lista

    Para extender uma list com outra usamos o seguinte comando
    -$ users = ["Paulo", "Pedro"]
    -$ outra_lista = ["Tiago", "João"]
    
    -$ users.extend(outra_lista)
    OUTRO MÉTODO QUE PODE SER FEITO É A SEGUINTE
    -$ users += outra_lista --> += representa a mesma coisa de extend

    Para remover sempre o ultimo dado da list podemos usar a função pop() como no exemplo
    -$ users.pop()

"""

users = []

print("Inserindo dados na list")

users.append("Romullo")
users.append("Isaura")
users.append("Ludmilla")
users.append("Bruno")
users.append("Alice")
print(users)

print("-" * 20)

print("Inserindo dados é informando a posição na list")

users.insert(2,"João")
print(users)

print("-" * 20)

print("Removendo um dado da list")

users.remove("Alice")
print(users)

print("-" * 20)

print("Pegando os dados conforme informamos")
head, *body, tail = users

print(head)
print(body)
print(tail)

print("-" * 20)

print("Juntando duas lista")

users = ["Pedro", "João"]
outra_lista = ["Lucas", "Marcelo"]

print(users + outra_lista)

print("-" * 20)

print("Para extender uma list")

users = ["Pedro", "João"]
outra_lista = ["Lucas", "Marcelo"]

users.extend(outra_lista)
print(users)

print("-" * 20)

print("Para remover sempre o ultimo dado da list")

print(users)
users.pop()
print(users)

print("-" * 20)

print("Outro exemplo de interação com list usando o for para inserir valores dentro da list")

resultado = []
for x in range(9):
    resultado.append(x * 4)
print(resultado)



