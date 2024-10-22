import sqlite3

def create_tables():
    conn = sqlite3.connect('bowling.db')
    c = conn.cursor()

    # Create the players table
    c.execute('''
        CREATE TABLE IF NOT EXISTS players (
            player_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            skill_level TEXT NOT NULL
        );
    ''')

    # Create the game_settings table
    c.execute('''
        CREATE TABLE IF NOT EXISTS game_settings (
            settings_id INTEGER PRIMARY KEY AUTOINCREMENT,
            frames INTEGER NOT NULL,
            format TEXT NOT NULL
        );
    ''')

    # Create the games table
    c.execute('''
        CREATE TABLE IF NOT EXISTS games (
            game_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            game_type TEXT NOT NULL,
            lane_number INTEGER NOT NULL,
            settings_id INTEGER,
            FOREIGN KEY (settings_id) REFERENCES game_settings(settings_id)
        );
    ''')

    # Create the game_players table
    c.execute('''
        CREATE TABLE IF NOT EXISTS game_players (
            game_id INTEGER,
            player_id INTEGER,
            FOREIGN KEY (game_id) REFERENCES games(game_id),
            FOREIGN KEY (player_id) REFERENCES players(player_id),
            PRIMARY KEY (game_id, player_id)
        );
    ''')

    # Create the rolls table
    c.execute('''
        CREATE TABLE IF NOT EXISTS rolls (
            roll_id INTEGER PRIMARY KEY AUTOINCREMENT,
            game_id INTEGER,
            player_id INTEGER,
            frame_number INTEGER,
            roll_number INTEGER,
            pins_knocked_down INTEGER,
            FOREIGN KEY (game_id) REFERENCES games(game_id),
            FOREIGN KEY (player_id) REFERENCES players(player_id)
        );
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
