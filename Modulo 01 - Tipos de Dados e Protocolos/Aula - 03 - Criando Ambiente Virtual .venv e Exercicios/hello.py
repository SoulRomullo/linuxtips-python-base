#!/usr/bin/env python3

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
    -$ ipython3
    
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

    Site com caracteres unicode com emoji e formato de letras de outros países, podemos copiar a imagem direto do site é colar no código python
    https://symbl.cc/en/

    Para guardar uma imagem no banco de dados com o código da fruta em hexadecimal devemos convertelo em UTF-8 como no exemplo abaixo 
    -$ fruta.encode("utf-8")
    Devemos colocar o código dentro de uma variável então ficará dessa forma ".encode("utf-8")"
    -$ fruta_encoded = fruta.encode("utf-8")
    Agora podemos verificar o código hexadecimal no terminal 
    -$ print(fruta_encoded)
    Para amostrar a imagem depois de transformar em hexadecimal usamos a seguinte função ".decode()"
    -$ fruta_encoded.decode()

    INTERPOLAÇÃO DE TEXTO
    Exemplo:
    -$ template = "O saldo do %s o total de %f" --> temos o formato de %s para string, $d para números inteiros, %f para números float
    Outro exemplo
    -$ "Olá %s" % "Romullo" --> Dessa forma ele irá retornar "Olá Romullo"

    Site para buscar mais expecificações é
    https://pyformat.info/

    

"""

print('Hello World!!!')