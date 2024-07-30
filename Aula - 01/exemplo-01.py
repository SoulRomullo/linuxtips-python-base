#!/usr/bin/env python3
# Este comando acima e referente ao Shebang link para saber mais
# https://pt.stackoverflow.com/questions/57702/diferen%C3%A7a-do-na-primeira-linha-de-um-script-python

"""
    Essas três aspas significa adicionar comentário em multi-linhas
    Para a deixar o código mais completo com mais informações do programas devemos
    Sempre informar todos os conceitos do programa desde nome do programa ao ambiente de variável
    Para um conceito universal de desenvolvimento devemos sempre comentar o código em liguagem em English.
    No link abaixo temos uma documentação para melhor entender
    https://peps.python.org/pep-0008/

    Devidamente o recomendado para o total de linhas de comentários para o programa é de 20 linhas
    Acima disso deve ser criado um documento externo para a informação numa documentação

"""

"""
import export as export
"""

"""
Hello world Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem correspondente,
neste caso ele está configurando em PT_BR para saber o tipo de linguagem
que está configurado no seu ambiente digite o seguinte comando no terminal
$ env | grep LANG

Como usar:
    Tenha a variável LANG devidamente configurado ex:

        export LANG=pt-BR

    Execução:

        python3 hello.py
        ou
        ./hello.py
        
"""
__version__ = "0.0.1"
__author__ = "Romullo Alves"
__license__ = "Unlicense"

# Dunder -> Significa que é um identificador ou uma palavra onde significa o uso da fala dos dois anderline __ sendo
# substituido por Dunder

"""
    Neste exemplo abaixo significa que quando for ser feito a execução do programa ele irá fazer essa validação, 
    se name for igual a main o programa será executado  
    
if __name__ == "__main__":
    print("Hello World!")

"""

lang = "pt_BR.utf8"

"""
    O exemplo abaixo podemos usar os dois modos para pagar informações dentro de uma variável usando o
    length ou split 
"""
# lang = lang[:5]

# ou passando o split e quando for encontrado o ponto "." ele irá dividir a string

lang = lang.split(".")[0]

# ou

# lang = lang.split(".")[1]

print(lang)

print("------------------")

import os

current_language = os.getenv("LANG", "en_US")[:5]

# current_language = "en.US"

# current_language = "it_IT"
# Este padrão de declarar variável se chama snake case
"""
    Outro Exemplo de como pode ser declarado uma variável principalmente em POO Orientação a Objeto 
    CurrentLanguage
    Este padrão de declarar variável se chama Pascal Case
"""

msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde"

print(msg)

# print("Hello World!")
