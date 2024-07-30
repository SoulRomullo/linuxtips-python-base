"""
    Criando um Ambiente Virtual 

    Ambiente Virtual é uma copia do python que fica isolado do python do sistema onde cada projeto e repositório são exclusivos do projeto e não interfere 
    no python do sistema, onde podemos instalar qualquer Biblioteca que não afetará o sistema.

    Usando os comando dentro do terminal do Linux, para copiar o Python do sistema para o projeto. 
    -$ python3 -m venv .venv

    "OBS: Lembrando que temos que ATIVAR A PASTA .VENV no projeto."
    
    Para saber em qual sistema Python '.venv' estamos acessando usamos o comando no Terminal Linux
    -$ which python3

    Para ativar o .venv no projeto local usamos o comando no Terminal Linux 
    -$ source .venv/bin/activate
"""

print('Hello World!!!')