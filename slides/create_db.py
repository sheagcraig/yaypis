conn = sqlite3.connect('nes_games.db')
c = conn.cursor()
c.execute('''CREATE TABLE games (id INTEGER PRIMARY KEY, title text, release_date text, publisher text)''')
c.execute("INSERT INTO games(title, release_date, publisher) VALUES (?, ?, ?)", (game['title'], game['release date'], game['publisher']))
