musicas = [ #[Música, Artista, Gênero]
    ["Tokyo Ghetto", "Eve", "J-pop"], 
    ["Outsider", "Eve", "J-pop"],
    ["Last Dance", "Eve", "J-pop"],
    ["Raison Detre", "Eve", "J-pop"],
    ["Inochi No Tabekata", "Eve", "J-pop"],
    ["Baumkuchen End", "Eve", "J-pop"],
    ["bedroom community", "glass beach", "Indie"],
    ["cold weather", "glass beach", "Indie"],
    ["calico", "glass beach", "Indie"],
    ["Touch-Tone Telephone", "Lemon Demon", "Indie"],
    ["Soft Fuzzy Man", "Lemon Demon", "Indie"],
    ["Modify", "Lemon Demon", "Indie"],
    ["Hot Milk", "Snail's House", "Future Bass"],
    ["MeteorGirl", "Snail's House", "Future Bass"],
    ["Pixel Galaxy", "Snail's House", "Future Bass"]
]

curtidas = []
descurtidas = []
playlist = []

import time
import os
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
from termcolor import colored
def colorir(texto, cor):
    text = colored(texto, cor)
    print(text)
entrada = False

limpar()
colorir("  █████████  ███████████     ███████    ███████████ █████ ███████████ ██████████ █████", "yellow")
colorir(" ███░░░░░███░░███░░░░░███  ███░░░░░███ ░█░░░███░░░█░░███ ░░███░░░░░░█░░███░░░░░█░░███ ", "yellow")
colorir("░███    ░░░  ░███    ░███ ███     ░░███░   ░███  ░  ░███  ░███   █ ░  ░███  █ ░  ░███ ", "yellow")
colorir("░░█████████  ░██████████ ░███      ░███    ░███     ░███  ░███████    ░██████    ░███ ", "green")
colorir(" ░░░░░░░░███ ░███░░░░░░  ░███      ░███    ░███     ░███  ░███░░░█    ░███░░█    ░███ ", "green")
colorir(" ███    ░███ ░███        ░░███     ███     ░███     ░███  ░███  ░     ░███ ░   █ ░███ ", "green")
colorir("░░█████████  █████        ░░░███████░      █████    █████ █████       ██████████ █████", "green")
colorir(" ░░░░░░░░░  ░░░░░           ░░░░░░░       ░░░░░    ░░░░░ ░░░░░       ░░░░░░░░░░ ░░░░░ ", "green")
time.sleep(3)

while True:
    # limpar()
    colorir("============", "yellow")
    colorir("[C] Cadastro", "yellow")
    colorir("[L] Login", "yellow")
    colorir("============", "yellow")
    reply_entrada = input("Resposta: ")
    if reply_entrada == "C":
        limpar()
        arquivo = open("arquivo.txt", "a")
        colorir("Cadastro", "yellow")
        nome = input("Nome: ")
        login = input("Login: ")
        senha = input("Senha: ")
        if nome.strip() == "" or login.strip() == "" or senha.strip() == "":
            colorir("Faltou preencher o nome, login e/ou a senha", "red")
            time.sleep(3)
        else:
            arquivo.write(f"{nome}/{login}/{senha}/{playlist}/{curtidas}/{descurtidas}\n")
            arquivo.close()
    elif reply_entrada == "L":
        limpar()
        login = open("arquivo.txt", "r")
        colorir("Login", "yellow")
        nome_check = input("Nome: ")
        login_check = input("Login: ")
        senha_check = input("Senha: ")
        with open("arquivo.txt", "r") as usuarios:
            conteudo = login.readlines()
        for linha in conteudo:
            nome, login, senha, playlist_txt, curtidas_txt, descurtidas_txt = linha.split("/")
            if nome_check == nome and login_check == login and senha_check == senha:
                entrada = True
                playlist = list(playlist_txt)
                curtidas = list(curtidas_txt)
                descurtidas = list(descurtidas_txt)
        if entrada == True:
            limpar()
            time.sleep(1)
            print("Olá %s" % nome_check)
            print(playlist)
            print(curtidas)
            print(playlist)
            time.sleep(5)
            usuarios.close()
            break
        if entrada == False:
            colorir("Nome, login e/ou senha estão incorreto(s) e/ou ausente(s)", "red")
            time.sleep(3)
        


while True:
    limpar()
    colorir("==========Menu==========", "yellow")
    colorir("[M] Buscar músicas", "yellow")
    colorir("[P] Gerenciar playlists", "yellow")
    colorir("[H] Visualizar histórico", "yellow")
    colorir("[S] Salvar", "green")
    colorir("========================", "yellow")
    reply = input("Resposta: ")
    if reply == "S":
        usuarios = open("arquivo.txt", "w")
        for i, linha in enumerate(conteudo):
            nome, login, senha, playlist_txt, curtidas_txt, descurtidas_txt = linha.split('/')
            if nome_check == nome and login_check == login and senha_check == senha:
                conteudo[i] = (f"{nome}/{login}/{senha}/{playlist}/{curtidas}/{descurtidas}\n")
                usuarios.write(conteudo[i])
    if reply == "M":
        while True:
            limpar()
            colorir("Digite o nome de uma música", "green")
            colorir("[S] Sair", "red")
            search_musica = input("Resposta: ")
            if search_musica == "S":
                break
            else:
                for linha in range(len(musicas)):
                    if search_musica == (musicas[linha][0]):
                        limpar()
                        print("Música:", musicas[linha][0])
                        print("Artista:", musicas[linha][1])
                        print("Gênero:", musicas[linha][2])
                        colorir("--------------", "yellow")
                        colorir("[S] Sim", "yellow")
                        colorir("[Qualquer] Não", "red")
                        colorir("--------------", "yellow")
                        colorir("Gostaria de deixar de curtir ou descurtir essa música?", "green")
                        reply = input("Resposta: ")
                        if reply == "S":
                            for i in range(len(descurtidas)):
                                if search_musica == (descurtidas[i][0]):
                                    descurtidas.remove(descurtidas[i])
                            for i in range(len(curtidas)):
                                if search_musica == (curtidas[i][0]):
                                    curtidas.remove(curtidas[i])
                        limpar()
                        print("Música:", musicas[linha][0])
                        print("Artista:", musicas[linha][1])
                        print("Gênero:", musicas[linha][2])
                        colorir("--------------", "yellow")
                        colorir("[S] Sim", "yellow")
                        colorir("[Qualquer] Não", "red")
                        colorir("--------------", "yellow")
                        colorir("Gostaria de curtir essa música?", "green")
                        reply = input("Resposta: ")
                        if reply == "S":
                            curtidas.append(musicas[linha])
                            for i in range(len(descurtidas)):
                                if search_musica == (descurtidas[i][0]):
                                    descurtidas.remove(descurtidas[i])
                        limpar()
                        print("Música:", musicas[linha][0])
                        print("Artista:", musicas[linha][1])
                        print("Gênero:", musicas[linha][2])
                        colorir("--------------", "yellow")
                        colorir("[S] Sim", "yellow")
                        colorir("[Qualquer] Não", "red")
                        colorir("--------------", "yellow")
                        colorir("Gostaria de descurtir essa música?", "green")
                        reply = input("Resposta: ")
                        if reply == "S":
                            descurtidas.append(musicas[linha])
                            for i in range(len(curtidas)):
                                if search_musica == (curtidas[i][0]):
                                    curtidas.remove(curtidas[i])
                        limpar()
                        print("Música:", musicas[linha][0])
                        print("Artista:", musicas[linha][1])
                        print("Gênero:", musicas[linha][2])
                        colorir("--------------", "yellow")
                        colorir("[S] Sim", "yellow")
                        colorir("[Qualquer] Não", "red")
                        colorir("--------------", "yellow")
                        colorir("Gostaria de adicionar em uma playlist?", "green")
                        reply = input("Resposta: ")
                        if reply == "S":
                            limpar()
                            colorir("Digite o nome da playlist que quer inserir", "green")
                            search_playlist = input("Resposta: ")
                            for i in range(len(playlist)):
                                if search_playlist == (playlist[i][0]):
                                    (playlist[i]).append(musicas[linha])
                                    break
    elif reply == "P":
        while True:
            limpar()
            colorir("=======Histórico=======", "yellow")
            colorir("[V] Visualizar playlist", "yellow")
            colorir("[C] Criar playlist", "yellow")
            colorir("[E] Editar playlist", "yellow")
            colorir("[D] Deletar playlist", "yellow")
            colorir("[S] Sair", "red")
            colorir("=======================", "yellow")
            reply = input("Resposta: ")
            if reply == "V":
                limpar()
                print(playlist)
                colorir("[Qualquer] Sair", "red")
                reply = input("Resposta: ")
            if reply == "C":
                limpar()
                colorir("Digite o nome da nova playlist", "green")
                nova_playlist = input("Resposta: ")
                playlist.append([nova_playlist])
            if reply == "E":
                limpar()
                colorir("Digite o nome da playlist", "green")
                search_playlist = input("Resposta: ")
                for i in range(len(playlist)):
                    if search_playlist == (playlist[i][0]):
                        limpar()
                        print(playlist[i])
                        colorir("Digite o nome da música que quer remover da playlist", "green")
                        search_musica = input("Resposta: ")
                        for j in range(len(playlist[i])):
                            if search_musica == (playlist[i][j][0]):
                                playlist.remove(playlist[i][j])
                        else:
                            print("ooo")
                            time.sleep(2)
            if reply == "D":
                limpar()
                colorir("Digite o nome da playlist que quer deletar", "green")
                search_playlist = input("Resposta: ")
                for i in range (len(playlist)):
                    if search_playlist == (playlist[i][0]):
                        playlist.remove(playlist[i])
            if reply == "S":
                break
    elif reply == "H":
        while True:
            limpar()
            colorir("=============Histórico==============", "yellow")
            colorir("[C] Músicas curtidas recentemente", "yellow")
            colorir("[D] Músicas descurtidas recentemente", "yellow")
            colorir("[S] Sair", "red")
            colorir("====================================", "yellow")
            reply = input("Resposta: ")
            if reply == "C":
                limpar()
                print(curtidas)
                colorir("[Qualquer] Sair", "red")
                reply = input("Resposta: ")
                reply = 0
            if reply == "D":
                limpar()
                print(descurtidas)
                colorir("[Qualquer] Sair", "red")
                reply = input("Resposta: ")
                reply = 0
            if reply == "S":
                break