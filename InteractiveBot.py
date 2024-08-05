import tkinter as tk
from tkinter import *
import os
from openNavegators import AbrindoRCO

class InteractiveBot:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplicativo automotivo para RCO e classroom")
        self.master.geometry("1920x1080")
        
        if os.path.exists("login.txt") and os.path.getsize("login.txt") >= 18:
            with open("login.txt", "r") as arq:
                self.iniciar_navegador
        else:
            self.create_login(master)

    def create_login(self, master):

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 210
        self.primeiroContainer.pack()

        self.containerUsuario = Frame(master)
        self.containerUsuario.pack()

        self.containerSenha = Frame(master)
        self.containerSenha.pack()

        self.botaoContainer = Frame(master)
        self.botaoContainer["pady"] = 20
        self.botaoContainer.pack()

        self.autenticado = Frame(master)
        self.autenticado["pady"] = 0
        self.autenticado.pack()

        self.titulo = Label(self.primeiroContainer, text="Professor bem vindo(a) ao aplicativo que simplificará sua vida!!!")
        self.titulo["font"] = ("Arial", "30", "bold")
        self.titulo.pack()

        self.usuarioLabel = Label(self.containerUsuario, text="Digite seu CPF: ")
        self.usuarioLabel["font"] = ("Arial", "15")
        self.usuarioLabel.pack(side=LEFT)
        
        self.usuario = Entry(self.containerUsuario)
        self.usuario["width"] = 30
        self.usuario["font"] = ("Arial", "15")
        self.usuario.pack(side=LEFT)

        self.senhaLabel = Label(self.containerSenha, text="Senha: ")
        self.senhaLabel["font"] = ("Arial", "15")
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.containerSenha)
        self.senha["width"] = 30
        self.senha["font"] = ("Arial", "15")
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.entrar = Button(self.botaoContainer)
        self.entrar["text"] = "Entrar"
        self.entrar["font"] = ("Calibri", "10")
        self.entrar["width"] = 15
        self.entrar["command"] = self.logar
        self.entrar.pack()

    def logar(self):
        usuario = self.usuario.get()
        senha = self.senha.get()
        
        with open("login.txt", "w") as dados:
            if len(usuario) == 11  and len(senha) >= 8:
                dados.write(usuario)
                dados.write("\n")
                dados.write(senha)
                self.mensagem_autenticacao = Label(self.autenticado, text="Cadastrado com sucesso!", font=("Arial", "10"))
                self.mensagem_autenticacao.pack()

                self.master.after(1000, self.iniciar_navegador)
                    
            else:
                self.mensagem_autenticacao = Label(self.autenticado, text="Usuário ou senha incorreto, tente novamente", font=("Arial", 10))
                self.mensagem_autenticacao.pack()

    def iniciar_navegador(self):
        self.master.destroy()
        startNavegador = AbrindoRCO()
        startNavegador.acessar_site()
        startNavegador.fazer_login()
        startNavegador.selecionar_livro()
