# APS - Processamento de Imagem

## Descrição

    O projeto procura aplicar um filtro no ambiente, de maneira com que pela detecção das bordas,
o fundo seja removido e assim adicionado a uma imagem temática.

## Procedimento

Deve-se criar um virtual environment

    $ python3 -m venv venv

Deve-se ativar o environment

Linux:
    $ source venv/bin/activate

Windows:
    $ /venv/scripts/activate.bat

Antes de executar o projeto deve-se baixar as dependencias no virtual environment

    $ pip install -r requirements.txt

O projeto deve ser inicializado no main.py

    $ python main.py

será gerado 2 imagens no result (fauna-result e flora-result) 