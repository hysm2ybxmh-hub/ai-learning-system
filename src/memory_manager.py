import sqlite3

class MemoryManager:
    def __init__(self, db_name='memory.sqlite'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY,
            content TEXT NOT NULL
        )''')
        self.connection.commit()

    def add_memory(self, content):
        self.cursor.execute('INSERT INTO memories (content) VALUES (?)', (content,))
        self.connection.commit()

    def get_memories(self):
        self.cursor.execute('SELECT content FROM memories')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
