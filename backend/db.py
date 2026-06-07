from sqlalchemy import create_engine, text

# Creates metadata.db file
engine = create_engine("sqlite:///metadata.db")

with engine.connect() as conn:

    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT
        )
    """))

    conn.execute(text("""
        INSERT INTO employees (name, department)
        VALUES
        ('Soumyjit', 'AI'),
        ('Rahul', 'Backend')
    """))

    conn.commit()

print("Database and table created successfully")