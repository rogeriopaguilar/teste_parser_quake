import unittest
from jogo import Jogo
import parserquake

class TestJogo(unittest.TestCase):

    def test_nome_jogo(self):
        jogo = Jogo("game_0");
        self.assertEqual(jogo.get_nome_jogo(), 'game_0');

    def test_jogadores_adicionados(self):
        jogo = Jogo("game_0");
        self.assertEqual(jogo.numero_de_jogadores(), 0);
        jogo.adicionar_jogador("jogadorum");
        self.assertEqual(jogo.numero_de_jogadores(), 1);
        jogo.adicionar_jogador("jogadordois");
        self.assertEqual(jogo.numero_de_jogadores(), 2);
        self.assertTrue(jogo.jogador_existente("jogadorum"));
        self.assertTrue(jogo.jogador_existente("jogadordois"));



    def test_total_mortes(self):
        jogo = Jogo("game_0");
        jogo.somar_morte();
        jogo.somar_morte();
        self.assertEqual(jogo.get_total_mortes(), 2);

    def test_total_mortes_jogador(self):
        jogo = Jogo("game_0");
        jogo.adicionar_jogador("jogador0");
        jogo.somar_morte_ao_jogador("jogador0");
        jogo.somar_morte_ao_jogador("jogador0");
        jogo.somar_morte_ao_jogador("jogador0");
        self.assertEqual(jogo.get_total_morte_jogador("jogador0"), 3);
        jogo.subtrair_morte_ao_jogador("jogador0");
        self.assertEqual(jogo.get_total_morte_jogador("jogador0"), 2);

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_parser_inicio_jogo(self):
        jogo = Jogo("game_0");
        linha = 'InitGame: \sv_floodProtect\1\sv_maxPing\0\sv_minPing\0\sv_maxRate\10000\sv_minRate\0\sv_hostname\Code';
        self.assertTrue(parserquake.verificar_inicio_jogo(linha,jogo));
        linha = 'itGame: \sv_floodProtect\1\sv_maxPing\0\sv_minPing\0\sv_maxRate\10000\sv_minRate\0\sv_hostname\Code';
        self.assertFalse(parserquake.verificar_inicio_jogo(linha,jogo));

    def test_parser_final_jogo(self):
        jogo = Jogo("game_0");
        linha =  '20:37 ShutdownGame:';
        self.assertTrue(parserquake.verificar_fim_de_jogo(linha,jogo));
        linha = '\Code';
        self.assertFalse(parserquake.verificar_fim_de_jogo(linha,jogo));

    def test_parser_novo_jogador(self):
        jogo = Jogo("game_0");
        linha='20: 38 ClientUserinfoChanged: 2 n\\Isgalamido\\t'; #\0\model\uriel / zael\hmodel\uriel / zael\g_redteam\\g_blueteam\\c1\5\c2\5\hc\100\w\0\l\0\tt\0\tl\0';
        indice_linha_atual = 1;
        self.assertTrue(parserquake.verificar_novo_jogador(linha, jogo, indice_linha_atual));
        self.assertTrue(jogo.jogador_existente("Isgalamido"))

    def test_parser_morte_jogador_morto_por_world(self):
        jogo = Jogo("game_0");
        linha='20: 38 ClientUserinfoChanged: 2 n\\Isgalamido\\t'; #\0\model\uriel / zael\hmodel\uriel / zael\g_redteam\\g_blueteam\\c1\5\c2\5\hc\100\w\0\l\0\tt\0\tl\0';
        indice_linha_atual = 1;
        self.assertTrue(parserquake.verificar_novo_jogador(linha, jogo, indice_linha_atual));
        self.assertTrue(jogo.jogador_existente("Isgalamido"))
        self.assertEqual(jogo.get_total_mortes(), 0);
        linha=' 20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT';
        self.assertTrue(parserquake.verificar_morte_jogador(linha, jogo));
        self.assertEqual(jogo.get_total_mortes(), 1);
        self.assertEqual(jogo.get_total_morte_jogador("Isgalamido"), -1);

    def test_parser_morte_jogador_morto_por_outro_jogador(self):
        jogo = Jogo("game_0");
        linha='20: 38 ClientUserinfoChanged: 2 n\\Isgalamido\\t'; #\0\model\uriel / zael\hmodel\uriel / zael\g_redteam\\g_blueteam\\c1\5\c2\5\hc\100\w\0\l\0\tt\0\tl\0';
        indice_linha_atual = 1;
        self.assertTrue(parserquake.verificar_novo_jogador(linha, jogo, indice_linha_atual));
        self.assertTrue(jogo.jogador_existente("Isgalamido"))
        self.assertEqual(jogo.get_total_mortes(), 0);
        linha = '21: 53 ClientUserinfoChanged: 3 n\\Mocinha\\t\0\model\sarge\hmodel\sarge\g_redteam\\g_blueteam\\c1\4\c2\5\hc\95\w\0\l\0\tt\0\tl\0';
        self.assertTrue(parserquake.verificar_novo_jogador(linha, jogo, indice_linha_atual));
        self.assertTrue(jogo.jogador_existente("Mocinha"));
        self.assertEqual(jogo.get_total_mortes(), 0);
        linha=' 22:06 Kill: 2 3 7: Isgalamido killed Mocinha by MOD_ROCKET_SPLASH';
        self.assertTrue(parserquake.verificar_morte_jogador(linha, jogo));
        self.assertEqual(jogo.get_total_mortes(), 1);
        self.assertEqual(jogo.get_total_morte_jogador("Mocinha"), 1);

    def test_parser_morte_jogador_morto_por_ele_mesmo(self):
        jogo = Jogo("game_0");
        linha='20: 38 ClientUserinfoChanged: 2 n\\Isgalamido\\t'; #\0\model\uriel / zael\hmodel\uriel / zael\g_redteam\\g_blueteam\\c1\5\c2\5\hc\100\w\0\l\0\tt\0\tl\0';
        indice_linha_atual = 1;
        self.assertTrue(parserquake.verificar_novo_jogador(linha, jogo, indice_linha_atual));
        self.assertTrue(jogo.jogador_existente("Isgalamido"))
        self.assertEqual(jogo.get_total_mortes(), 0);
        linha=' 22:06 Kill: 2 3 7: Isgalamido killed Isgalamido by MOD_ROCKET_SPLASH';
        self.assertTrue(parserquake.verificar_morte_jogador(linha, jogo));
        self.assertEqual(jogo.get_total_mortes(), 1);
        self.assertEqual(jogo.get_total_morte_jogador("Isgalamido"), 0);




if __name__ == '__main__':
    unittest.main()