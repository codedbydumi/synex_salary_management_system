# connection to database
import mysql.connector
import sys
import os
from start import Login
from user_menu import User

# Set UTF-8 encoding for Windows console to handle Unicode characters
if os.name == 'nt':  # Windows
    try:
        os.system('chcp 65001 > nul')
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass  # Fallback if UTF-8 setup fails

print(
    "      !----------<<<<<<<<<<<>>>>>>>  |Synex   Industry|^  <<<<<<<<<>>>>>>>>>>>---------!         \n\nTo EXIT   :-  'exit'")

class DBconnection:
    def __init__(self):
        self.name = 'root'
        self.passwd = ''
        self.host = "localhost"
        self.database = 'synex_industries'
        self.connection = None
        self.con()

    def con(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.name,
                passwd=self.passwd,
                database=self.database
            )
            print("Database connection established successfully!")
        except mysql.connector.Error as err:
            print(f"Database connection failed: {err}")
            print("Please check your database configuration and make sure MySQL is running.")
            sys.exit(1)

    def cursor(self):
        if self.connection and self.connection.is_connected():
            cur = self.connection.cursor()
            return cur
        else:
            print("No active database connection!")
            return None

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")

def main():
    try:
        # Database connection using object
        database = DBconnection()
        cur = database.cursor()
        
        if cur is None:
            print("Failed to create database cursor. Exiting...")
            return
        
        # Login connection
        start_interface = Login(cur)
        
        # if login Success - add your logic here
        
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except ImportError as e:
        print(f"Import error: {e}")
        print("Please make sure all required modules (start.py, user_menu.py) are in the same directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Clean up database connection
        try:
            if 'database' in locals():
                database.close_connection()
        except:
            pass

if __name__ == "__main__":
    main()

    