"""
    Criando um Ambiente Virtual 

    Ambiente Virtual é uma copia do python que fica isolado do python do sistema onde cada 
    projeto e repositório são exclusivos do projeto e não interfere 
    no python do sistema, onde podemos instalar qualquer Biblioteca que não afetará o sistema.

    Usando os comando dentro do terminal do Linux, para copiar o Python do sistema para o projeto. 
    -$ python3 -m venv .venv

    "OBS: Lembrando que temos que ATIVAR A PASTA .VENV no projeto."
    
    Para saber em qual sistema Python '.venv' estamos acessando usamos o comando no Terminal Linux
    -$ which python3

    Para ativar o .venv no projeto local usamos o comando no Terminal Linux 
    -$ source .venv/bin/activate

    PIP é um repositório de pacotes do Python
    O site para acessar é www.pypi.org

    Para fazer o upgrade do PIP usamos o comando no terminal
    -$ python -m pip install --upgrade pip

    Para iniciar a Biblioteca IPYTHON instalado no projeto usamos o comando no terminal, ele é interpretador do python no terminal
    -$ ipython
    
    Comando para saber o número em Binário
    -$ bin(65) --> Exemplo pode ser o nome de uma variável

    Comando para saber onde é guardado na mémoria a variável
    -$ id(65) --> Exemplo

    Comando para saber o tipo da variável
    -$ type(numero) --> Exemplo já foi guardado um valor dentro dessa variável

    OBJETO é um local de armazenamento da memória onde é guardado o valor e tipo da variável

    Para saber todos os diretórios das propriedades INT usamos o seguinte comando no terminal
    -$ dir(int)

    Para executar o comando usamos dessa forma
    -$ numero.bit_count() --> Exemplo

    __index__ este objeto é chamado de PROTOCOLO DO OBJETO, usando o comando dir(int) no terminal, vai aparecer todos os que 
    existe!

    
    
"""

print('Hello World!!!')