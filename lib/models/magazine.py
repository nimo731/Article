from lib.db.connection import get_connection

class Magazine:
    def __init__(self, name, category, id=None):
        self.name = name
        self.category = category
        self.id = id

    def save(self):
        """Save the magazine to the database"""
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute(
                "UPDATE magazines SET name = ?, category = ? WHERE id = ?",
                (self.name, self.category, self.id)
            )
        else:
            cursor.execute(
                "INSERT INTO magazines (name, category) VALUES (?, ?)",
                (self.name, self.category)
            )
            self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        """Find a magazine by ID"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        magazine_data = cursor.fetchone()
        conn.close()
        return cls(magazine_data['name'], magazine_data['category'], magazine_data['id']) if magazine_data else None

    @classmethod
    def find_by_name(cls, name):
        """Find a magazine by name"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        magazine_data = cursor.fetchone()
        conn.close()
        return cls(magazine_data['name'], magazine_data['category'], magazine_data['id']) if magazine_data else None

    @classmethod
    def find_by_category(cls, category):
        """Find magazines by category"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE category = ?", (category,))
        magazines = [cls(row['name'], row['category'], row['id']) for row in cursor.fetchall()]
        conn.close()
        return magazines

    def articles(self):
        """Get all articles published in this magazine"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM articles 
            WHERE magazine_id = ?
        """, (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def contributors(self):
        """Get all authors who have written for this magazine"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT a.* FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
        """, (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return authors

    def article_titles(self):
        """Get all article titles in this magazine"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT title FROM articles 
            WHERE magazine_id = ?
        """, (self.id,))
        titles = [row['title'] for row in cursor.fetchall()]
        conn.close()
        return titles

    def contributing_authors(self):
        """Get authors with more than 2 articles in this magazine"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.*, COUNT(ar.id) as article_count
            FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
            GROUP BY a.id
            HAVING article_count > 2
        """, (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return authors

    @classmethod
    def top_publisher(cls):
        """Find the magazine with the most articles"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.*, COUNT(a.id) as article_count
            FROM magazines m
            LEFT JOIN articles a ON m.id = a.magazine_id
            GROUP BY m.id
            ORDER BY article_count DESC
            LIMIT 1
        """)
        magazine_data = cursor.fetchone()
        conn.close()
        return cls(magazine_data['name'], magazine_data['category'], magazine_data['id']) if magazine_data else None 