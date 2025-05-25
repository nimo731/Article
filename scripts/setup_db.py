import sqlite3
import os

def setup_database():
    # Create the database directory if it doesn't exist
    os.makedirs('lib/db', exist_ok=True)
    
    # Read the schema file
    with open('lib/db/schema.sql', 'r') as f:
        schema = f.read()
    
    # Connect to the database and create tables
    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()
    
    # Execute the schema
    cursor.executescript(schema)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print("Database setup completed successfully!")

if __name__ == "__main__":
    setup_database() 