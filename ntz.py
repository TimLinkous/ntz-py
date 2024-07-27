# add your code in this file
import os
import sys
import sqlite3
from pathlib import Path

DB_FILE = Path.home() / '.ntz.db'

def initialize_db():
  conn = sqlite3.conect(DB_FILE)
  c = conn.cursor()
  c.execute('''
      CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
            )
  ''')
  conn.commit()
  conn.close()

def remember(category, content):
  conn = sqlite3.connect(DB_FILE)
  c = conn.cursor()
  c.execute('INSERT INTO notes (category, content) VALUES (?,?)', (category, content))
  conn.commit()
  conn.close()


def list_notes():
  conn = sqlite3.connect(DB_FILE)
  c = conn.cursor()
  c.execute('SELECT id, category, content FROM notes')
  notes = c.fetchall()
  conn.close()
  return notes

def forget_note(note_id):
  conn = sqlite3.connect(DB_FILE)
  c = conn.cursor()
  c.execute('DELETE FROM notes WHERE id = ?', (note_id,))
  conn.commit()
  conn.close()

def edit_note(note_id, new_content):
  conn = sqlite3.connect(DB_FILE)
  c = conn.cursor
  c.execute('UPDATE notes SET content = ? WHERE id = ?', (new_content, note_id))
  conn.commit()
  conn.close()

def clear_notes():
  conn = sqlite3.connect(DB_FILE)
  c = conn.cursor
  c.execute("DELETE from notes")
  conn.commit()
  conn.close()


# main function
def cli():
  if len(sys.argv) < 2:
    print("Usage: ntz <command> [<args>]")
    print("Commands:")
    print(" r <category> <note>   Remember a new note in a category")
    print(" -c <category> <note>  Create or append to a category")
    print(" f <id>                Forget a note by id")
    print(" e <id> <new note>     Edit note by id")
    print(" clear                 Clear all notes")
    print(" list                  List all notes")
    sys.exit(1)

  command = sys.argv[1]
  if command == 'r':
    if len(sys.argv) < 4:
      print("Usage: ntz r <category> <note>")
      sys.exit(1)
    category = sys.argv[2]
    content = ' '.join(sys.argv[3:])
    remember(category, content)
    print(f"Note added in category '{category}': {content}")
  elif command == '-c':
    if len(sys.argv) < 4:
      print("Usage: ntz -c <category> <note>")
      sys.exit(1)
    category = sys.argv[2]
    content = ' '.join(sys.argv[3:])
    remember(category, content)
    print(f"Note added in category '{category}': {content}")
  elif command == 'f':
    if len(sys.argv) < 3:
      print("Usage: ntz f <id>")
      sys.exit(1)
    note_id = int(sys.argv[2])
    forget_note(note_id)
    print(f"Note deleted: {note_id}")
  elif command == 'e':
    if len(sys.argv) < 4:
      print("Usage: ntz e <id> <new note>")
      sys.exit[1]
    note_id = int(sys.argv[2])
    new_content = ' '.join(sys.argv[3:])
    edit_note(note_id, new_content)
    print(f"Note edited: {note_id} to '{new_content}'")
  elif command == 'clear':
    clear_notes()
    print("All notes cleared")
  elif command == 'list':
    notes = list_notes()
    for note in notes:
      print(f"{note[0]}L [{note[1]}] {note[2]}")
  else:
    print("Unknown command: {command}")
    sys.exit(1)

def get_args():
  return os.sys.argv
  
# run the main function
if __name__ == '__main__':
  initialize_db()
  cli()
