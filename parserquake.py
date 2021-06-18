import json
from jogo import Jogo

lista_jogos = [];
json_jogos = None;

def verificar_inicio_jogo(linha,jogo_atual):
    if linha.find('InitGame') != -1:
        print('----------Novo Jogo----------');
        if jogo_atual is not None:
           # print("Novo jogoLINHA:" + str(indice_jogo_atual));
            lista_jogos.append(jogo_atual);
        return True;
    return False;

def verificar_fim_de_jogo(linha, jogo_atual):
    if linha.find('ShutdownGame:') != -1:
        # print(jogo_atual._nome_jogo);
        # print(jogo_atual._total_mortes);
        # print(jogo_atual._lista_jogadores);
        # print(jogo_atual._mapa_mortes);
        # print(jogo_atual.toJSON());
        print("NRO JOGADORES: " + str(jogo_atual.numero_de_jogadores()));
        print('Final do Jogo');
        return True;
    return False;

def verificar_morte_jogador(linha, jogo_atual):
    if linha.find('Kill:') != -1:
        jogo_atual.somar_morte();
        # sprint(linha);
        linha_morto_por = linha[linha.find('killed') + 6:];
        # print("linha_morto_por:" + linha_morto_por);

        jogador_assassino = linha.split(':')[-1];
        jogador_assassino = jogador_assassino.split(':')[-1];
        jogador_assassino = jogador_assassino[0: jogador_assassino.find("killed")];
        jogador_assassino = jogador_assassino.strip();
        print("Jogador assassino: " + jogador_assassino);

        nome_jogador_assassinado = linha[linha.find('killed') + 6:linha.find('by')];
        nome_jogador_assassinado = nome_jogador_assassinado.strip();

        if '<world>' == jogador_assassino:
            jogo_atual.subtrair_morte_ao_jogador(nome_jogador_assassinado)
        elif jogador_assassino != nome_jogador_assassinado:
            jogo_atual.somar_morte_ao_jogador(nome_jogador_assassinado);
        return True;
    return False;

def verificar_novo_jogador(linha, jogo_atual,indice_linha_atual):
    if linha.find('ClientUserinfoChanged:') != -1:
        print("Jogadore encontrado linha: " + str(indice_linha_atual));

        nome_jogador = linha[linha.index('n\\') + 2:linha.index('\\t')];
        nome_jogador = nome_jogador.strip();
        print("Adicionando nome_jogador:" + nome_jogador);

        if not jogo_atual.jogador_existente(nome_jogador):
            jogo_atual.adicionar_jogador(nome_jogador);
        return True;
    return False;

def lerArquivo():
    jogo_atual = None
    arquivo = open('games.log')
    indice_jogo_atual = 1
    indice_linha_atual = 0

    for linha in arquivo:
        indice_linha_atual += 1;
        if verificar_inicio_jogo(linha, jogo_atual):
            jogo_atual = Jogo("game_" + str(indice_jogo_atual));
            indice_jogo_atual += 1;

        verificar_fim_de_jogo(linha, jogo_atual);
        verificar_morte_jogador(linha, jogo_atual);
        verificar_novo_jogador(linha, jogo_atual,indice_linha_atual);

    arquivo.close();

if __name__ == '__main__':
    lerArquivo();
    json_jogos = "[";
    for i in lista_jogos:
        json_jogos += i.toJSON() + ",";
    json_jogos = json_jogos[0: len(json_jogos) - 1];
    json_jogos += "]";
    print(json_jogos);