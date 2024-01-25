import sqlite3
from customtkinter import *

class GUI:
    def __init__(self, master):
        # Definir tema
        set_appearance_mode("dark")

        # Definir título
        self.master = master
        self.master.title("Gestão de Dados de Jogadores de Futebol")

        # Definir janela
        self.master.geometry("800x600")
        self.master.resizable(False, False)

        # Conectar à base de dados
        self.conn = sqlite3.connect('Jogadores.db')
        self.cursor = self.conn.cursor()

        # Ler as queries do arquivo
        with open('queries.sql', 'r', encoding='utf-8') as file:
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
            "Clube com o maior nº de jogadores não nacionais": self.consulta_5,
            "Adicionar Novo Jogador": self.adicionar_jogador,
            "Editar Jogador": self.editar_jogador,
            "Eliminar Jogador": self.eliminar_jogador,
            "Pesquisa Avançada": self.pesquisa_avancada
        }

        # Criar buttons de forma dinâmica, utilizando o dicionário anterior
        for text, command in self.buttons.items():
            btn = CTkButton(master, text=text, command=command)
            btn.pack()
        
        # Criar textbox
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

    # Adicionar um novo jogador
    def adicionar_jogador(self):
        # Criar nova janela
        new_window = CTkToplevel(self.master)
        new_window.title("Adicionar Jogador")

        # Criar inputs
        CTkLabel(new_window, text="Nome:").pack()
        nome_entry = CTkEntry(new_window)
        nome_entry.pack()

        CTkLabel(new_window, text="Nacionalidade:").pack()
        nacionalidade_entry = CTkEntry(new_window)
        nacionalidade_entry.pack()

        CTkLabel(new_window, text="Idade:").pack()
        idade_entry = CTkEntry(new_window)
        idade_entry.pack()

        CTkLabel(new_window, text="Posição:").pack()
        pos_entry = CTkEntry(new_window)
        pos_entry.pack()

        CTkLabel(new_window, text="Clube Atual:").pack()
        clube_atual_entry = CTkEntry(new_window)
        clube_atual_entry.pack()

        # Criar botão para submeter os dados
        submit_button = CTkButton(new_window, text="Adicionar Jogador", command=lambda: self.insert_jogador(
            nome_entry.get(), idade_entry.get(), pos_entry.get(), nacionalidade_entry.get(), clube_atual_entry.get()))
        submit_button.pack()

   # Editar informações de um jogador
    def editar_jogador(self):
        # Criar nova janela
        new_window = CTkToplevel(self.master)
        new_window.title("Editar Jogador")

        # Criar inputs
        CTkLabel(new_window, text="ID do Jogador:").pack()
        id_entry = CTkEntry(new_window)
        id_entry.pack()

        CTkLabel(new_window, text="Atributo a modificar (Nome, Idade, Nacionalidade, Clube Atual):").pack()
        atributo_entry = CTkEntry(new_window)
        atributo_entry.pack()

        CTkLabel(new_window, text="Novo valor:").pack()
        valor_entry = CTkEntry(new_window)
        valor_entry.pack()

        # Criar botão para submeter os dados
        submit_button = CTkButton(new_window, text="Editar Jogador", 
                                command=lambda: self.update_jogador(id_entry.get(), atributo_entry.get(), valor_entry.get(), new_window))
        submit_button.pack()

    def update_jogador(self, jogador_id, atributo, valor, window):
        if jogador_id and atributo and valor:
            jogador_id = int(jogador_id)
            update_query = f"UPDATE Jogadores SET {atributo}='{valor}' WHERE ID={jogador_id}"
            self.execute_query(update_query)
            window.destroy()

    # Eliminar um jogador
    def eliminar_jogador(self):
        # Criar nova janela
        new_window = CTkToplevel(self.master)
        new_window.title("Eliminar Jogador")

        # Criar inputs
        CTkLabel(new_window, text="ID do Jogador:").pack()
        id_entry = CTkEntry(new_window)
        id_entry.pack()

        # Criar botão para submeter os dados
        submit_button = CTkButton(new_window, text="Eliminar Jogador", 
                                command=lambda: (
                                    self.execute_query(f"DELETE FROM Jogadores WHERE ID={int(id_entry.get())}"),
                                    new_window.destroy()
                                ))
        submit_button.pack()

    # Query para pesquisa avançada
    def execute_pesquisa_avancada(self, idade, nacionalidade, clube_atual):
        pesquisa_avancada_query = f'''
        SELECT * FROM Jogadores
        WHERE Idade LIKE '%{idade}%'
        AND ClubeAtual LIKE '%{clube_atual}%'
        AND Nacionalidade LIKE '%{nacionalidade}%'
        '''
        self.execute_query(pesquisa_avancada_query)

    # Pesquisa avançada
    def pesquisa_avancada(self):
        # Criar nova janela
        new_window = CTkToplevel(self.master)
        new_window.title("Pesquisa Avançada")

        # Criar inputs
        CTkLabel(new_window, text="Idade:").pack()
        idade_entry = CTkEntry(new_window)
        idade_entry.pack()

        CTkLabel(new_window, text="Nacionalidade:").pack()
        nacionalidade_entry = CTkEntry(new_window)
        nacionalidade_entry.pack()

        CTkLabel(new_window, text="Clube Atual:").pack()
        clube_atual_entry = CTkEntry(new_window)
        clube_atual_entry.pack()

        # Criar botão para submeter os dados
        submit_button = CTkButton(new_window, text="Pesquisar", command=lambda: 
            self.execute_pesquisa_avancada(idade_entry.get(), nacionalidade_entry.get(), clube_atual_entry.get()))
        submit_button.pack()

    # Inserir jogador na base de dados
    def insert_jogador(self, nome, idade, posicao, nacionalidade, clube_atual):
        if nome and idade and posicao and nacionalidade and clube_atual:
            query = f"INSERT INTO Jogadores (Nome, Idade, Posicao, Nacionalidade, ClubeAtual) VALUES ('{nome}', {idade}, '{posicao}', '{nacionalidade}', '{clube_atual}')"
            self.execute_query(query)

    # Atualizar lista de jogadores
    def atualizar_lista(self):
        self.lista.delete(0, END)
        
        jogadores = self.execute_query("SELECT * FROM Jogadores")

        for jogador in jogadores:
            self.lista.insert(END, jogador)

if __name__ == "__main__":
    root = CTk()
    app = GUI(root)
    root.mainloop()
