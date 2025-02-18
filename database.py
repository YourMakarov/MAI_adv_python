import sqlite3
from config import DB_NAME

def create_db():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Events (
        id TEXT PRIMARY KEY,
        event_text TEXT
    )
    ''')
    connection.commit()
    connection.close()

def db_insert(data):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.executemany('INSERT INTO Events VALUES(?,?);', data)
    connection.commit()
    connection.close()

def db_find_by_ids(ids):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    query = "SELECT event_text FROM Events WHERE id IN ({})".format(','.join(['?']*len(ids)))
    cursor.execute(query, ids)
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return [row[0] for row in rows]