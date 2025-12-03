"""
Grupo: As Branquelas
Membros: 
    Danilo Amorim 
    Yan Ishiyama
    Davi Belz
05/11/2025
"""

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime 
import Atividade5app

class InserirTitulo:
    def __init__(self, parent):
        self.win = tk.Toplevel(parent)
        self.win.title("Inserir Título")
        self.win.geometry("500x600")

        campos = [
            ("Título do Livro", "titulo"),
            ("Tipo do Livro", "tipo"),
            ("ID da Editora", "editora"),
            ("Preço", "preco"),
            ("Total Venda", "total"),
            ("Royalty", "royalty"),
            ("Média de Vendas", "media"),
            ("Observações", "obs"),
            ("Data de Publicação (AAAA-MM-DD)", "data")
        ]
        self.entries = {}

        for texto, chave in campos:
            ttk.Label(self.win, text=texto + ":").pack(pady=3)
            entrada = ttk.Entry(self.win, width=40)
            entrada.pack()
            self.entries[chave] = entrada

        ttk.Button(self.win, text="Salvar", command=self.salvar).pack(pady=20)

    def salvar(self):
        dados = (
            self.entries["titulo"].get(),
            self.entries["tipo"].get(),
            self.entries["editora"].get() or None,
            self.entries["preco"].get() or None,
            self.entries["total"].get() or None,
            self.entries["royalty"].get() or None,
            self.entries["media"].get() or None,
            self.entries["obs"].get(),
            self.entries["data"].get()
        )

        conn = Atividade5app.conectar()
        if conn:
            cursor = conn.cursor()
            sql = """INSERT INTO titulos
                    (TITULO_LIVRO, TIPO_LIVRO, ID_EDITORA, PRECO, TOTAL_VENDA, ROYALTY,
                    MEDIA_QUANT_VENDAS, OBSERVACOES, DATA_PUBLICACAO)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            try:
                cursor.execute(sql, dados)
                conn.commit()
                messagebox.showinfo("Sucesso", "Título inserido com sucesso!")
                self.win.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Falha ao inserir: {err}")
            finally:
                cursor.close()
                conn.close()