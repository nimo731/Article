import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def test_article_creation():
    author = Author("Test Author")
    author.save()
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    article = Article("Test Article", author.id, magazine.id)
    assert article.title == "Test Article"
    assert article.author_id == author.id
    assert article.magazine_id == magazine.id
    assert article.id is None

def test_article_save():
    author = Author("Test Author")
    author.save()
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    article = Article("Test Article", author.id, magazine.id)
    article.save()
    assert article.id is not None

def test_article_find_by_id():
    author = Author("Test Author")
    author.save()
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    article = Article("Test Article", author.id, magazine.id)
    article.save()
    
    found_article = Article.find_by_id(article.id)
    assert found_article is not None
    assert found_article.title == "Test Article"
    assert found_article.author_id == author.id
    assert found_article.magazine_id == magazine.id

def test_article_find_by_title():
    # Create a unique title for this test
    unique_title = "Unique Test Article 123"
    author = Author("Test Author")
    author.save()
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    article = Article(unique_title, author.id, magazine.id)
    article.save()
    
    articles = Article.find_by_title(unique_title)
    assert len(articles) == 1
    assert articles[0].title == unique_title

def test_article_find_by_author():
    author = Author("Test Author")
    author.save()
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    article = Article("Test Article", author.id, magazine.id)
    article.save()
    
    articles = Article.find_by_author(author.id)
    assert len(articles) == 1
    assert articles[0].title == "Test Article"

def test_article_find_by_magazine():
    author = Author("Test Author")
    author.save()
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    article = Article("Test Article", author.id, magazine.id)
    article.save()
    
    articles = Article.find_by_magazine(magazine.id)
    assert len(articles) == 1
    assert articles[0].title == "Test Article"

def test_article_author():
    author = Author("Test Author")
    author.save()
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    article = Article("Test Article", author.id, magazine.id)
    article.save()
    
    found_author = article.author()
    assert found_author is not None
    assert found_author.name == "Test Author"

def test_article_magazine():
    author = Author("Test Author")
    author.save()
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    article = Article("Test Article", author.id, magazine.id)
    article.save()
    
    found_magazine = article.magazine()
    assert found_magazine is not None
    assert found_magazine.name == "Test Magazine"
    assert found_magazine.category == "Test Category" 