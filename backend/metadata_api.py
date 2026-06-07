from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///metadata.db")

def get_tables():

    try:

        with engine.connect() as conn:

            result = conn.execute(text(
                "SELECT name FROM sqlite_master WHERE type='table';"
            ))

            tables = [row[0] for row in result]

            return tables

    except Exception as e:

        return {
            "error": str(e)
        }