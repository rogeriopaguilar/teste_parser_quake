from fastapi import FastAPI
import parserquake

app = FastAPI()
json_jogos=None

@app.get("/")
def listar_todos():
    if parserquake.json_jogos is None:
        parserquake.lista_jogos = []
        parserquake.lerArquivo()
        json_jogos = "[";
        for i in parserquake.lista_jogos:
            json_jogos += i.toJSON() + ",";
        json_jogos = json_jogos[0: len(json_jogos) - 1];
        json_jogos += "]";
        parserquake.json_jogos = json_jogos
        print(json_jogos);
    else:
        print('Arquivo já carregado em memória.');
        json_jogos = parserquake.json_jogos;

    return json_jogos;


@app.get("/jogos/{jogo_id}")
def listar_jogo(jogo_id: int):
    if parserquake.json_jogos is None:
        parserquake.lista_jogos = []
        parserquake.lerArquivo()
    return parserquake.lista_jogos[jogo_id].toJSON();