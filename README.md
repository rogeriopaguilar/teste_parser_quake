

# Ambiente

Foi utilizada a linguagem python versão 3.8.6
É necessário instalar a biblioteca [fastapi](https://fastapi.tiangolo.com/)
O arquivo de log deve estar no mesmo diretório da aplicação

## Execução
Para verificar no browser, subir o servidor com o comando uvicorn main:app --reload no diretório da aplicação. As instruções para execução deste servidor podem ser vista no site da fastapi. Após subir o servidor existem duas urls:

http://localhost:8000/ mostrará o json criado após ler o arquivo de log do jogo no browser
http://localhost:8000/{indice} irá consultar um jogo pelo índice e exibir o json correspondente. Ex:
http://localhost:8000/0  exibirá o json do primeiro jogo 


A url de documentação da apié a seguinte:
http://localhost:8000/docs

Para verificar a saída no console, executar o comando no diretório do projeto:

python parserquake.py

# Testes
Para executar os testes unitários, posicionar o console no diretório do projeto e executar o seguinte comando:

python -m unittest testes.py

Para executar os testes unitários dos controles rest, executar o comando no diretório do projeto:

pyton testerest.py
