import sqlite3

def create_tables():
    conn = sqlite3.connect("canteen.db")
    c = conn.cursor()

    # Students table
    c.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT UNIQUE,
        name TEXT,
        department TEXT,
        allowed INTEGER DEFAULT 1
    )''')

    # Attendance table
    c.execute('''CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT,
        date TEXT,
        status TEXT
    )''')

    conn.commit()
    conn.close()

# Run this once to initialize the database
if __name__ == "__main__":
    create_tables()
    print("Database setup complete ✅")
