"""
Este é o programa principal que irá importar funções de outras bibliotecas, para execução corretamente
do jogo da velha.
"""
from time import sleep

from jogodavelha.lib.dados import *

c, r = 1, 0
arq = 'listadejogadores.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
carregarArquivo(arq)
while r != 4:
    r = menuprincipal(['Criar Jogador', 'Carregar Jogadores já Criado', 'Ranking', 'Sair do Jogo'], 'MENU PRINCIPAL')
    if r == 1:
        titulo('CRIANDO JOGADORES')
        nome = str(input(f'Nome do Jogador: ')).strip()
        cadastrar(arq, nome, 0)
        carregarArquivo(arq)
    elif r == 2:
        if len(jogadores) < 2:
            print('Você precisa criar mais Jogador')
        else:
            pronto = escolhadeJogadores()
            if pronto:
                op = menuprincipal(['Continuar?', 'Voltar?'], 'Começar a Partida')
                if op == 1:
                    while True:
                        name, name1 = sorteio(c)
                        m = construimatriz3x3()
                        mostrajogo(m)
                        while not finalizando(m, name, name1):
                            jogando(m)
                            print('==' * 15)
                            sleep(0.3)
                            mostrajogo(m)
                        print(f'FINALIZANDO A {c}ª PARTIDA!')
                        sleep(1)
                        print('°°' * 20)
                        c += 1
                        resp = str(input('Quer Continuar? [S/N]')).strip()[0]
                        if resp in 'Nn':
                            break
                    atualizaarquivo(arq)
    elif r == 3:
        ranking()
    elif r == 4:
        titulo('JOGO FINALIZADO')
    else:
        print('\033[31mDigite um valor entre 1 e 4\033[m')
lerarquivo(arq)
