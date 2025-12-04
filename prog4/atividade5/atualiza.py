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
import app

class Atualizar:
  def __init__(self, parent):
      self.win = tk.Toplevel(parent)
      self.win.title("Atualizar Título")
      self.win.geometry("400x400")

      ttk.Label(self.win, text="ID do Título a atualizar:").pack(pady=5)
      self.id_entry = ttk.Entry(self.win)
      self.id_entry.pack()

      ttk.Label(self.win, text="Novo Título do Livro:").pack(pady=5)
      self.titulo_entry = ttk.Entry(self.win)
      self.titulo_entry.pack()

      ttk.Label(self.win, text="Novo Preço:").pack(pady=5)
      self.preco_entry = ttk.Entry(self.win)
      self.preco_entry.pack()

      ttk.Button(self.win, text="Atualizar", command=self.atualizar).pack(pady=10)

  def atualizar(self):
      conn = app.conectar()
      if conn:
            cursor = conn.cursor()
            sql = "UPDATE titulos SET TITULO_LIVRO=%s, PRECO=%s WHERE ID_TITULO=%s"
            dados = (self.titulo_entry.get(), self.preco_entry.get(), self.id_entry.get())
            cursor.execute(sql, dados)
            conn.commit()
            messagebox.showinfo("Sucesso", "Título atualizado com sucesso!")
            self.win.destroy()
            cursor.close()
            conn.close()