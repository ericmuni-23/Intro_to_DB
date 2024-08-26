#!/usr/bin/env python3
import mysql.connector

def create_database():
    try:
        # Establish a connection to the MySQL server
        db = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password"
        )
        print("Connected to the MySQL server successfully!")

        # Create a cursor object
        cursor = db.cursor()

        # Create the database
        cursor.execute("CREATE DATABASE alx_book_store")

        # Commit the changes
        db.commit()

        # Close the cursor and the database connection
        cursor.close()
        db.close()

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Failed to create the database: {err}")

if __name__ == "__main__":
    create_database()
