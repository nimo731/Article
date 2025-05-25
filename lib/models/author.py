from lib.db.connection import get_connection

class Author:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def save(self):
        """Save the author to the database"""
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute(
                "UPDATE authors SET name = ? WHERE id = ?",
                (self.name, self.id)
            )
        else:
            cursor.execute(
                "INSERT INTO authors (name) VALUES (?)",
                (self.name,)
            )
            self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        """Find an author by ID"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
        author_data = cursor.fetchone()
        conn.close()
        return cls(author_data['name'], author_data['id']) if author_data else None

    @classmethod
    def find_by_name(cls, name):
        """Find an author by name"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
        author_data = cursor.fetchone()
        conn.close()
        return cls(author_data['name'], author_data['id']) if author_data else None

    @classmethod
    def find_all(cls):
        """Find all authors"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors")
        authors = [cls(row['name'], row['id']) for row in cursor.fetchall()]
        conn.close()
        return authors

    def articles(self):
        """Get all articles written by this author"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM articles 
            WHERE author_id = ?
        """, (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def magazines(self):
        """Get all magazines this author has contributed to"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines

    def topic_areas(self):
        """Get unique categories of magazines this author has contributed to"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.category FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        categories = [row['category'] for row in cursor.fetchall()]
        conn.close()
        return categories

    def add_article(self, magazine, title):
        """Create and save a new article for this author"""
        from lib.models.article import Article
        article = Article(title, self.id, magazine.id)
        article.save()
        return article 