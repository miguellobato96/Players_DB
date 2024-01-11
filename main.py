import sqlite3
from customtkinter import *

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestão de Dados de Jogadores de Futebol")

        # Conectar à base de dados
        self.conn = sqlite3.connect('Jogadores.db')
        self.cursor = self.conn.cursor()

        # Ler as queries do arquivo
        with open('queries.sql', 'r') as file:
            queries = file.read()

        # Executar as queries
        self.cursor.executescript(queries)
        self.conn.commit()

        # Criar widgets
        self.label = CTkLabel(master, text="Gestão de Jogadores de Futebol")
        self.label.pack()

        # Criar dicionário com cada button e valor correspondente (text & command)
        self.buttons = {
            "Listar Jogadores": self.listar_jogadores,
            "Jogadores com idade > 30": self.consulta_1,
            "Jogador mais jovem": self.consulta_2,
            "Catalogar por Nacionalidade": self.consulta_3,
            "Média de Idades por Clube": self.consulta_4,
            "Clube com o maior nº de jogadores não nacionais": self.consulta_5
        }

        # Criar buttons de forma dinâmica, utilizando o dicionário anterior
        for text, command in self.buttons.items():
            btn = CTkButton(master, text=text, command=command)
            btn.pack()

        self.textbox = CTkTextbox(master, width=600)
        self.textbox.pack()

    # Função que serve de base para fazer ".execute('query')"
    def execute_query(self, query):
        self.textbox.delete(1.0, END)
        self.cursor.execute(query)
        resultado = self.cursor.fetchall()
        for row in resultado:
            formatted_row = " | ".join(map(str, row)) + "\n"
            self.textbox.insert(END, formatted_row)

    # Consulta: Todos os jogadores
    def listar_jogadores(self):
        self.execute_query('SELECT * FROM Jogadores')

    # Consulta: Listar jogadores com idade superior a 30 anos
    def consulta_1(self):
        self.execute_query('SELECT * FROM Jogadores WHERE Idade > 30')

    # Consulta: Identificar o jogador mais jovem
    def consulta_2(self):
        self.execute_query('SELECT * FROM Jogadores ORDER BY Idade ASC LIMIT 1')

    # Consulta: Catalogar jogadores por nacionalidade
    def consulta_3(self):
        self.execute_query('SELECT Nacionalidade, COUNT(*) FROM Jogadores GROUP BY Nacionalidade')

    # Consulta: Calcular a média de idades dos jogadores por clube
    def consulta_4(self):
        self.execute_query('SELECT ClubeAtual, ROUND(AVG(Idade)) as MediaIdade FROM Jogadores GROUP BY ClubeAtual')

    # Consulta: Determinar o clube com o maior número de jogadores não nacionais
    def consulta_5(self):
        query_max_not_national = '''
        SELECT ClubeAtual, COUNT(*) as NumJogadoresNaoNacionais
        FROM Jogadores
        WHERE Nacionalidade != 'Portugal'
        GROUP BY ClubeAtual
        ORDER BY NumJogadoresNaoNacionais DESC
        LIMIT 1
        '''
        self.execute_query(query_max_not_national)

if __name__ == "__main__":
    root = CTk()
    app = GUI(root)
    root.mainloop()
