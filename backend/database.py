import sqlite3

def save_chat(user_message, bot_response):

    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT,
            bot_response TEXT
        )
        """
    )

    cursor.execute(
        "INSERT INTO chats (user_message, bot_response) VALUES (?, ?)",
        (user_message, bot_response)
    )

    conn.commit()
    conn.close()


def get_chats():

    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM chats"
    )

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "id": row[0],
            "user_message": row[1],
            "bot_response": row[2]
        }
        for row in rows
    ]