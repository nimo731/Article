import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed_database():
    # Create authors
    authors = [
        Author("John Smith"),
        Author("Jane Doe"),
        Author("Bob Johnson")
    ]
    for author in authors:
        author.save()

    # Create magazines
    magazines = [
        Magazine("Tech Today", "Technology"),
        Magazine("Science Weekly", "Science"),
        Magazine("Business Insider", "Business")
    ]
    for magazine in magazines:
        magazine.save()

    # Create articles
    articles = [
        Article("The Future of AI", authors[0].id, magazines[0].id),
        Article("Quantum Computing Explained", authors[0].id, magazines[1].id),
        Article("Startup Success Stories", authors[1].id, magazines[2].id),
        Article("Machine Learning Basics", authors[1].id, magazines[0].id),
        Article("Market Analysis 2024", authors[2].id, magazines[2].id),
        Article("Climate Change Solutions", authors[2].id, magazines[1].id)
    ]
    for article in articles:
        article.save()

    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database() 