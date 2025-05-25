import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def test_author_creation():
    author = Author("Test Author")
    assert author.name == "Test Author"
    assert author.id is None

def test_author_save():
    author = Author("Test Author")
    author.save()
    assert author.id is not None

def test_author_find_by_id():
    author = Author("Test Author")
    author.save()
    found_author = Author.find_by_id(author.id)
    assert found_author is not None
    assert found_author.name == "Test Author"

def test_author_find_by_name():
    author = Author("Test Author")
    author.save()
    found_author = Author.find_by_name("Test Author")
    assert found_author is not None
    assert found_author.id == author.id

def test_author_articles():
    author = Author("Test Author")
    author.save()
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    article = Article("Test Article", author.id, magazine.id)
    article.save()
    
    articles = author.articles()
    assert len(articles) == 1
    assert articles[0]['title'] == "Test Article"

def test_author_magazines():
    author = Author("Test Author")
    author.save()
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    article = Article("Test Article", author.id, magazine.id)
    article.save()
    
    magazines = author.magazines()
    assert len(magazines) == 1
    assert magazines[0]['name'] == "Test Magazine"

def test_author_topic_areas():
    author = Author("Test Author")
    author.save()
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    article = Article("Test Article", author.id, magazine.id)
    article.save()
    
    categories = author.topic_areas()
    assert len(categories) == 1
    assert categories[0] == "Test Category" 