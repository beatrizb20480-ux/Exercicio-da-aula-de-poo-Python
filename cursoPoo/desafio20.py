from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = [] #list()


    def add_favoritos(self, add_favorito): #game
        self.jogos.append(add_favorito)
        #self.jogos.append(game)
        #self.jogos = sorted(self.jogos, key=str.lower())





    def ficha(self):
        jogo_formatado = '\n'.join(sorted(self.jogos))
        panel = Panel(f'Nome real: [black on white]{self.nome}[/]\n'
                      f'jogo favorito:\n[blue]{jogo_formatado}[/]\n', title='Jogador <detonador2026>', width=40)
        print(panel)
        #conteudo += f''
        # 'for game in enumerate(self.jogos):
        #       conteudo += f'\n:video_game: [blue] {game}[/]''
        #conteudo += f'jogos favoritos: '




j1 = Gamer('Benjamin', 'furia_da_noite')
j1.add_favoritos('Lies of P')
j1.add_favoritos('Elden ring')
j1.add_favoritos('BloodBorn')
j1.add_favoritos('DarkSoul')
j1.ficha()

j2 = Gamer('Henry', 'Senhor_Frodo')
j2.add_favoritos('Mortal kombat')
j2.add_favoritos('Efootball')
j2.ficha()