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

class DeletarTitulo:
    def __init__(self, parent):
        self.win = tk.Toplevel(parent)
        self.win.title("Deletar Título")
        self.win.geometry("300x200")

        ttk.Label(self.win, text="ID do Título a deletar:").pack(pady=10)
        self.id_entry = ttk.Entry(self.win)
        self.id_entry.pack()

        ttk.Button(self.win, text="Deletar", command=self.deletar).pack(pady=10)

    def deletar(self):
        conn = app.conectar()
        if conn:
            cursor = conn.cursor()
            id_titulo = self.id_entry.get()
            try:
                cursor.execute("DELETE FROM autoria WHERE ID_TITULO = %s", (id_titulo,))
                cursor.execute("DELETE FROM titulos WHERE ID_TITULO = %s", (id_titulo,))
                conn.commit()
                messagebox.showinfo("Sucesso", "Título deletado com sucesso!")
                self.win.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Falha ao deletar: {err}")
            finally:
                cursor.close()
                conn.close()