import mysql.connector

def create_database():
    # Connect to MySQL server
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Execute SQL to create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS lelemove_system")

    # Use the database
    cursor.execute("USE lelemove_system")

    # Execute SQL to create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS shipments (
                        item_id VARCHAR(10) PRIMARY KEY,
                        item_height VARCHAR(5),
                        item_width VARCHAR(5),
                        item_length VARCHAR(5),
                        item_volume VARCHAR(10),
                        item_price VARCHAR(5)
                    )''')

    # Commit changes and close cursor
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
