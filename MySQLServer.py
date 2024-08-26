#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establishing a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',        # Change this if your MySQL server is on a different host
            user='your_username',    # Replace with your MySQL username
            password='your_password' # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Creating the database if it does not already exist
            cursor.execute("except mysql.connector.Error")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Closing the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
    