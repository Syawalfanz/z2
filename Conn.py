import mysql.connector

def connect_to_mysql():
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="lelemove_system"
        )
        
        if conn.is_connected():
            print("Connected to MySQL server")
            return conn
        else:
            print("Failed to connect to MySQL server")
            return None
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL server: {e}")
        return None
