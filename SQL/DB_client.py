# PYTHON SQL

import psycopg2

def create_server_connection():

    PGHOST='ep-sweet-sound-a2m88zrk.eu-central-1.aws.neon.tech'
    PGDATABASE='datafundamentamentals'
    PGUSER='datafundamentamentals_owner'
    PGPASSWORD='QhJH3pb0gDfv'
    conn = None
    try:
        conn = psycopg2.connect(database=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=5432)
        print("Database conn successful")
    except Error as err:
        print(f"Error: '{err}'")

    return conn

connection = create_server_connection()
connection.close()



# Crear tabla
conn = create_server_connection()

# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a command: create datafund_students table
try:
    cur.execute("""CREATE TABLE datafund_students(
                student_id SERIAL PRIMARY KEY,
                student_name VARCHAR (50) UNIQUE NOT NULL,
                student_email VARCHAR (100) NOT NULL,
                student_age INT NOT NULL);
                """)
    # Make the changes to the database persistent
    conn.commit()
except Error as err:
        print(f"Error: '{err}'")
        conn.rollback()

# Close cursor and communication with the database
cur.close()
conn.close()
