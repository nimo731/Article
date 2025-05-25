import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def test_magazine_creation():
    magazine = Magazine("Test Magazine", "Test Category")
    assert magazine.name == "Test Magazine"
    assert magazine.category == "Test Category"
    assert magazine.id is None

def test_magazine_save():
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    assert magazine.id is not None

def test_magazine_find_by_id():
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    
    found_magazine = Magazine.find_by_id(magazine.id)
    assert found_magazine is not None
    assert found_magazine.name == "Test Magazine"
    assert found_magazine.category == "Test Category"

def test_magazine_find_by_name():
    unique_name = "Unique Test Magazine 123"
    magazine = Magazine(unique_name, "Test Category")
    magazine.save()
    
    found_magazine = Magazine.find_by_name(unique_name)
    assert found_magazine is not None
    assert found_magazine.name == unique_name

def test_magazine_find_by_category():
    unique_category = "Unique Test Category 123"
    magazine = Magazine("Test Magazine", unique_category)
    magazine.save()
    
    magazines = Magazine.find_by_category(unique_category)
    assert len(magazines) == 1
    assert magazines[0].category == unique_category

def test_magazine_articles():
    author = Author("Test Author")
    author.save()
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    
    # Create multiple articles for this magazine
    article1 = Article("Test Article 1", author.id, magazine.id)
    article1.save()
    article2 = Article("Test Article 2", author.id, magazine.id)
    article2.save()
    
    articles = magazine.articles()
    assert len(articles) == 2
    assert any(article['title'] == "Test Article 1" for article in articles)
    assert any(article['title'] == "Test Article 2" for article in articles)

def test_magazine_authors():
    author1 = Author("Test Author 1")
    author1.save()
    author2 = Author("Test Author 2")
    author2.save()
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    
    # Create articles with different authors
    article1 = Article("Test Article 1", author1.id, magazine.id)
    article1.save()
    article2 = Article("Test Article 2", author2.id, magazine.id)
    article2.save()
    
    authors = magazine.contributors()
    assert len(authors) == 2
    assert any(a['name'] == "Test Author 1" for a in authors)
    assert any(a['name'] == "Test Author 2" for a in authors)

def test_magazine_contributors():
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    author = Author("Test Author")
    author.save()
    article = Article("Test Article", author.id, magazine.id)
    article.save()
    
    contributors = magazine.contributors()
    assert len(contributors) == 1
    assert contributors[0]['name'] == "Test Author"

def test_magazine_article_titles():
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    author = Author("Test Author")
    author.save()
    article = Article("Test Article", author.id, magazine.id)
    article.save()
    
    titles = magazine.article_titles()
    assert len(titles) == 1
    assert titles[0] == "Test Article"

def test_magazine_contributing_authors():
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    author = Author("Test Author")
    author.save()
    
    # Create 3 articles for the same author
    for i in range(3):
        article = Article(f"Test Article {i}", author.id, magazine.id)
        article.save()
    
    contributing_authors = magazine.contributing_authors()
    assert len(contributing_authors) == 1
    assert contributing_authors[0]['name'] == "Test Author"

def test_magazine_top_publisher():
    # Create two magazines
    magazine1 = Magazine("Test Magazine 1", "Test Category")
    magazine2 = Magazine("Test Magazine 2", "Test Category")
    magazine1.save()
    magazine2.save()
    
    author = Author("Test Author")
    author.save()
    
    # Add more articles to magazine1
    for i in range(3):
        article = Article(f"Test Article {i}", author.id, magazine1.id)
        article.save()
    
    # Add one article to magazine2
    article = Article("Test Article", author.id, magazine2.id)
    article.save()
    
    top_magazine = Magazine.top_publisher()
    assert top_magazine is not None
    assert top_magazine.name == "Test Magazine 1" 