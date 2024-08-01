#!/usr/bin/env python3

"""
Projeto
--Exibir um relatório de crianças por atividade.
--Imprimir a lista de crianças agrupadas por sala
--que frequentem cada uma das atividades.


"""

__version__= "0.1.1"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [("Ingles", aula_ingles), 
              ("Musica", aula_musica), 
               ("Dança", aula_danca)]

for nome_atividade, atividade in atividades:

    # Listar alunos em cada atividade por sala
    print("-" * 40)

    print(f"Alunos da atividade {nome_atividade}")
    
    print("-" * 40,"\n")

    # Sala1 que tem interseção com a atividade

    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(atividade)
       
    print(f"{nome_atividade} sala1", atividade_sala1)
    print(f"{nome_atividade} sala2", atividade_sala2)

    print()
    print("#" * 40,"\n")
