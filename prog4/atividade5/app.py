'''
    Grupo:
        Soul Society
    Integrantes:
        Guilherme Cordeiro Costa
        Fillipy Costa da Silva
        Pablo Nistal Lazaro Santos
'''

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import insere
import atualiza
import exclui
import consulta

def conectar():
    bd = mysql.connector.connect(
            host="localhost",
            user="root",
            password="serra",
            database="publicacao"
        )
    return bd

class ChildWindow:
    def __init__(self, parent, title, content=None):
        self.window = tk.Toplevel(parent)
        self.window.title(title)
        self.window.geometry("450x350")

        main_frame = ttk.Frame(self.window, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)

        if content:
            label = ttk.Label(main_frame, text=content, font=('Arial', 12))
            label.pack(pady=20)

        ttk.Button(main_frame, text="Fechar", command=self.window.destroy).pack(pady=10)

class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Títulos - Banco Publicacao")
        self.root.geometry("800x600")

        self.criar_menu()
        self.criar_layout_principal()

    def criar_layout_principal(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(
            main_frame,
            text="Sistema de Gerenciamento de Títulos",
            font=('Arial', 20, 'bold')
        ).pack(pady=15)

        ttk.Label(
            main_frame,
            text="Use o menu acima para acessar as funções do sistema.",
            font=('Arial', 12)
        ).pack(pady=10)

        ttk.Label(
            main_frame,
            text="Desenvolvido com Python, Tkinter e MySQL",
            font=('Arial', 10)
        ).pack(side=tk.BOTTOM, pady=10)

    def criar_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        menu_titulo = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Títulos", menu=menu_titulo)

        menu_titulo.add_command(
            label="Inserir",
            command=lambda: insere.InserirTitulo(self.root)
        )
        menu_titulo.add_separator()

        menu_titulo.add_command(
            label="Atualizar",
            command=lambda: atualiza.AtualizarTitulo(self.root)
        )
        menu_titulo.add_separator()

        menu_titulo.add_command(
            label="Excluir",
            command=lambda: exclui.DeletarTitulo(self.root)
        )
        menu_titulo.add_separator()

        menu_titulo.add_command(
            label="Consultar",
            command=lambda: consulta.ConsultarTitulos(self.root)
        )
        menu_titulo.add_separator()

        menu_titulo.add_command(label="Sair", command=self.root.quit)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ajuda", menu=help_menu)

        help_menu.add_command(
            label="Socorro...",
            command=lambda: ChildWindow(self.root, "Ajuda", "Respire fundo. Você consegue terminar!")
        )

        help_menu.add_command(label="Sobre", command=self.sobre)

    def sobre(self):
        about = tk.Toplevel(self.root)
        about.title("Sobre")
        about.geometry("300x200")

        ttk.Label(about, text="Gerenciador de Títulos", font=('Arial', 14)).pack(pady=10)
        ttk.Label(about, text="Versão 1.67").pack()
        ttk.Label(about, text="Desenvolvido pelo grupo Soul Society").pack(pady=10)

        ttk.Button(about, text="OK", command=about.destroy).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()
