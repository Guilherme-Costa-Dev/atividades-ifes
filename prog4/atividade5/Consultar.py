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
import app

class ConsultarTitulos:
    def __init__(self, parent):
        self.win = tk.Toplevel(parent)
        self.win.title("Consultar Títulos")
        self.win.geometry("900x400")

        cols = ("ID_TITULO", "TITULO_LIVRO", "TIPO_LIVRO", "PRECO", "DATA_PUBLICACAO")
        self.tree = ttk.Treeview(self.win, columns=cols, show="headings")

        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        ttk.Button(self.win, text="Carregar dados", command=self.carregar_dados).pack(pady=5)

    def carregar_dados(self):
        conn = app.conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT ID_TITULO, TITULO_LIVRO, TIPO_LIVRO, PRECO, DATA_PUBLICACAO FROM titulos")
            registros = cursor.fetchall()

            for i in self.tree.get_children():
                self.tree.delete(i)
            for reg in registros:
                self.tree.insert("", tk.END, values=reg)

            cursor.close()
            conn.close()