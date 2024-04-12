import sqlite3
from customtkinter import *

class GUI:
    def __init__(self, master):
        # Set theme
        set_appearance_mode("dark")

        # Set title
        self.master = master
        self.master.title("Football Player Data Management")

        # Set window
        self.master.geometry("800x600")
        self.master.resizable(False, False)

        # Connect to the database
        self.conn = sqlite3.connect('Players.db')
        self.cursor = self.conn.cursor()

        # Read queries from file
        with open('queries.sql', 'r', encoding='utf-8') as file:
            queries = file.read()

        # Execute queries
        self.cursor.executescript(queries)
        self.conn.commit()

        # Create widgets
        self.label = CTkLabel(master, text="Football Player Management")
        self.label.pack()

        # Create dictionary with each button and corresponding value (text & command)
        self.buttons = {
            "List Players": self.list_players,
            "Players over 30": self.query_1,
            "Youngest Player": self.query_2,
            "Catalog Players by Nationality": self.query_3,
            "Average Ages by Club": self.query_4,
            "Club with Most Non-National Players": self.query_5,
            "Add New Player": self.add_player,
            "Edit Player": self.edit_player,
            "Delete Player": self.delete_player,
            "Advanced Search": self.advanced_search
        }

        # Create buttons dynamically using the previous dictionary
        for text, command in self.buttons.items():
            btn = CTkButton(master, text=text, command=command)
            btn.pack()
        
        # Create textbox
        self.textbox = CTkTextbox(master, width=600)
        self.textbox.pack()

    # Function serving as a base to execute ".execute('query')"
    def execute_query(self, query):
        self.textbox.delete(1.0, END)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            formatted_row = " | ".join(map(str, row)) + "\n"
            self.textbox.insert(END, formatted_row)

    # Query: All players
    def list_players(self):
        self.execute_query('SELECT * FROM Players')

    # Query: List players over 30 years old
    def query_1(self):
        self.execute_query('SELECT * FROM Players WHERE Age > 30')

    # Query: Identify the youngest player
    def query_2(self):
        self.execute_query('SELECT * FROM Players ORDER BY Age ASC LIMIT 1')

    # Query: Catalog players by nationality
    def query_3(self):
        self.execute_query('SELECT Nationality, COUNT(*) FROM Players GROUP BY Nationality')

    # Query: Calculate the average age of players by club
    def query_4(self):
        self.execute_query('SELECT CurrentClub, ROUND(AVG(Age)) as AvgAge FROM Players GROUP BY CurrentClub')

    # Query: Determine the club with the highest number of non-national players
    def query_5(self):
        query_max_not_national = '''
        SELECT CurrentClub, COUNT(*) as NumNonNationalPlayers
        FROM Players
        WHERE Nationality != 'Portugal'
        GROUP BY CurrentClub
        ORDER BY NumNonNationalPlayers DESC
        LIMIT 1
        '''
        self.execute_query(query_max_not_national)

    # Add a new player
    def add_player(self):
        # Create new window
        new_window = CTkToplevel(self.master)
        new_window.title("Add Player")

        # Create inputs
        CTkLabel(new_window, text="Name:").pack()
        name_entry = CTkEntry(new_window)
        name_entry.pack()

        CTkLabel(new_window, text="Nationality:").pack()
        nationality_entry = CTkEntry(new_window)
        nationality_entry.pack()

        CTkLabel(new_window, text="Age:").pack()
        age_entry = CTkEntry(new_window)
        age_entry.pack()

        CTkLabel(new_window, text="Position:").pack()
        position_entry = CTkEntry(new_window)
        position_entry.pack()

        CTkLabel(new_window, text="Current Club:").pack()
        current_club_entry = CTkEntry(new_window)
        current_club_entry.pack()

        # Create button to submit data
        submit_button = CTkButton(new_window, text="Add Player", command=lambda: self.insert_player(
            name_entry.get(), age_entry.get(), position_entry.get(), nationality_entry.get(), current_club_entry.get()))
        submit_button.pack()

   # Edit player information
    def edit_player(self):
        # Create new window
        new_window = CTkToplevel(self.master)
        new_window.title("Edit Player")

        # Create inputs
        CTkLabel(new_window, text="Player ID:").pack()
        id_entry = CTkEntry(new_window)
        id_entry.pack()

        CTkLabel(new_window, text="Attribute to modify (Name, Age, Nationality, Current Club):").pack()
        attribute_entry = CTkEntry(new_window)
        attribute_entry.pack()

        CTkLabel(new_window, text="New value:").pack()
        value_entry = CTkEntry(new_window)
        value_entry.pack()

        # Create button to submit data
        submit_button = CTkButton(new_window, text="Edit Player", 
                                command=lambda: self.update_player(id_entry.get(), attribute_entry.get(), value_entry.get(), new_window))
        submit_button.pack()

    def update_player(self, player_id, attribute, value, window):
        if player_id and attribute and value:
            player_id = int(player_id)
            update_query = f"UPDATE Players SET {attribute}='{value}' WHERE ID={player_id}"
            self.execute_query(update_query)
            window.destroy()

    # Delete a player
    def delete_player(self):
        # Create new window
        new_window = CTkToplevel(self.master)
        new_window.title("Delete Player")

        # Create inputs
        CTkLabel(new_window, text="Player ID:").pack()
        id_entry = CTkEntry(new_window)
        id_entry.pack()

        # Create button to submit data
        submit_button = CTkButton(new_window, text="Delete Player", 
                                command=lambda: (
                                    self.execute_query(f"DELETE FROM Players WHERE ID={int(id_entry.get())}"),
                                    new_window.destroy()
                                ))
        submit_button.pack()

    # Query for advanced search
    def execute_advanced_search(self, age, nationality, current_club):
        advanced_search_query = f'''
        SELECT * FROM Players
        WHERE Age LIKE '%{age}%'
        AND CurrentClub LIKE '%{current_club}%'
        AND Nationality LIKE '%{nationality}%'
        '''
        self.execute_query(advanced_search_query)

    # Advanced search
    def advanced_search(self):
        # Create new window
        new_window = CTkToplevel(self.master)
        new_window.title("Advanced Search")

        # Create inputs
        CTkLabel(new_window, text="Age:").pack()
        age_entry = CTkEntry(new_window)
        age_entry.pack()

        CTkLabel(new_window, text="Nationality:").pack()
        nationality_entry = CTkEntry(new_window)
        nationality_entry.pack()

        CTkLabel(new_window, text="Current Club:").pack()
        current_club_entry = CTkEntry(new_window)
        current_club_entry.pack()

        # Create button to submit data
        submit_button = CTkButton(new_window, text="Search", command=lambda: 
            self.execute_advanced_search(age_entry.get(), nationality_entry.get(), current_club_entry.get()))
        submit_button.pack()

    # Insert player into database
    def insert_player(self, name, age, position, nationality, current_club):
        if name and age and position and nationality and current_club:
            query = f"INSERT INTO Players (Name, Age, Position, Nationality, CurrentClub) VALUES ('{name}', {age}, '{position}', '{nationality}', '{current_club}')"
            self.execute_query(query)

    # Update player list
    def update_list(self):
        self.list.delete(0, END)
        
        players = self.execute_query("SELECT * FROM Players")

        for player in players:
            self.list.insert(END, player)

if __name__ == "__main__":
    root = CTk()
    app = GUI(root)
    root.mainloop()
