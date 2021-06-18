import json

class Jogo:


    def __init__(self, nome_jogo):
        self._nome_jogo = nome_jogo
        self._total_mortes = 0
        self._lista_jogadores = []
        self._mapa_mortes = {}


    def get_nome_jogo(self):
        return self._nome_jogo

    def jogador_existente(self, nome_jogador):
        print(len(self._lista_jogadores));
        return nome_jogador in self._lista_jogadores;

    def adicionar_jogador(self, nome_jogador):
        self._lista_jogadores.append(nome_jogador);
        self._mapa_mortes[nome_jogador] = 0;

    def numero_de_jogadores(self):
        return len(self._lista_jogadores);

    def somar_morte(self):
        self._total_mortes += 1;

    def get_total_mortes(self):
        return self._total_mortes

    def somar_morte_ao_jogador(self, nome_jogador):
        qtde = self._mapa_mortes[nome_jogador];
        qtde+=1
        self._mapa_mortes[nome_jogador] =qtde;

    def subtrair_morte_ao_jogador(self, nome_jogador):
        qtde = self._mapa_mortes[nome_jogador];
        qtde-=1
        self._mapa_mortes[nome_jogador] =qtde;

    def get_total_morte_jogador(self, nome_jogador):
        return self._mapa_mortes[nome_jogador]

    def toJSON(self):
        strJSON = '"' + self._nome_jogo + '":{';
        strJSON += '"total_kills":' + str(self._total_mortes) + ',';
        strJSON += '"players":' + json.dumps(self._lista_jogadores) + ',';
        strJSON += '"kills":' + json.dumps(self._mapa_mortes) + '}';
        return strJSON
