"""
    Como criar um ambiente de variável em um projeto

    Primeiros passos é acessar o terminal
    Como temos o python instalado em nosso sistema não podemos criar esse ambiente com o venv do sistema,
    então temos que fazer uma cópia do venv onde podemos acessar, no terminal na pasta do local do projeto
    rodamos o seguinte comando

    python3 -m venv .venv

    Explicando

    "python3" -> Acessando a versão do python instalado no sistema

    "-m" -> No contexto do Python é usado para executar módulos como scripts.
    Quando você executa um comando na linha de comando usando python -m <nome_do_modulo>
    (ou python3 -m <nome_do_modulo> dependendo de como o Python está instalado no seu sistema),
    o Python irá procurar por <nome_do_modulo> nos diretórios listados em sys.path,
    compilar o seu código se necessário, e então executar o módulo como um script.

    Isso é particularmente útil por várias razões:

    Executar módulos padrão como scripts: Alguns módulos padrão do Python são projetados para serem utilizados
    como scripts. Por exemplo, python -m http.server inicia um servidor HTTP simples que serve os arquivos
    do diretório atual.

    Evitar problemas de importação: Quando você executa um script diretamente,
    seu diretório é adicionado ao início do sys.path, o que pode causar problemas se houver outros módulos
    com o mesmo nome em seu caminho de pesquisa de módulos. Executar um módulo com -m garante que o comportamento
    de importação é o esperado.

    Facilitar a execução de pacotes: Se você tem um pacote com vários módulos e um ponto de entrada definido
    (por exemplo, um __main__.py), você pode executar o pacote como um script usando o -m.
    Isso diz ao Python para tratar o pacote como um script, executando o código no __main__.py.

    "venv" -> É um pacote de modulos que tem no sistema python

    ".venv" -> Esse nome pode ser qualquer nome mais como estamos cópiando do sistema um pacote do venv
    como padrão usamos .venv como no exemplo e esse "." significa que esse arquivo será criado em nosso projeto e
    ele ficará oculto na pasta do projeto.

    Usando os comandos abaixo no terminal:

    which pyhton -> ele irá mostrar o caminho onde estamos usando o python no caso se o ambiente virtual não estiver
    ativo ele irá mostrar o caminho da pasta do sistema e não do projeto

    Para ativar o ambiente virtual o .venv devemos usar o seguinte comando no terminal
    source .venv/bin/activate

    Devemos criar um arquivo chamado .gitignore para que o nosso repositório não precise levar todos os pacotes do
    python instalado na pasta do projeto .venv
    Para isso devemos ir no terminal e digitar o seguinte comando
    micro .gitignore
    com este comando ele já irá criar o arquivo e dentro dele devemos inserir o seguinte texto
    .venv
    salvar o arquivo em seguida podemos sair do editor micro
    Para salvar usamos ctrl + s
    Sair F4

"""

print("Olá Mundo!")



