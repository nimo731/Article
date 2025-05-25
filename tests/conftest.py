import pytest
import sqlite3
import os

@pytest.fixture(autouse=True)
def clean_database():
    """Clean up the database before each test"""
    # Delete the database file if it exists
    if os.path.exists('articles.db'):
        os.remove('articles.db')
    
    # Create a new database with the schema
    conn = sqlite3.connect('articles.db')
    with open('lib/db/schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.close()
    
    yield  # This is where the test runs
    
    # Clean up after the test
    if os.path.exists('articles.db'):
        os.remove('articles.db') 