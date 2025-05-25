import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def main():
    print("Welcome to the Article Management System Debug Console!")
    print("\nAvailable commands:")
    print("1. List all authors")
    print("2. List all magazines")
    print("3. List all articles")
    print("4. Find author by name")
    print("5. Find magazine by name")
    print("6. Find articles by author")
    print("7. Find articles by magazine")
    print("8. Get magazine contributors")
    print("9. Get author's magazines")
    print("10. Get top publisher")
    print("q. Quit")

    while True:
        choice = input("\nEnter your choice (1-10, or q to quit): ")

        if choice == 'q':
            break
        elif choice == '1':
            # List all authors
            authors = Author.find_all()
            for author in authors:
                print(f"ID: {author.id}, Name: {author.name}")
        elif choice == '2':
            # List all magazines
            magazines = Magazine.find_all()
            for magazine in magazines:
                print(f"ID: {magazine.id}, Name: {magazine.name}, Category: {magazine.category}")
        elif choice == '3':
            # List all articles
            articles = Article.find_all()
            for article in articles:
                print(f"ID: {article.id}, Title: {article.title}")
        elif choice == '4':
            name = input("Enter author name: ")
            author = Author.find_by_name(name)
            if author:
                print(f"Found author: ID: {author.id}, Name: {author.name}")
            else:
                print("Author not found")
        elif choice == '5':
            name = input("Enter magazine name: ")
            magazine = Magazine.find_by_name(name)
            if magazine:
                print(f"Found magazine: ID: {magazine.id}, Name: {magazine.name}, Category: {magazine.category}")
            else:
                print("Magazine not found")
        elif choice == '6':
            name = input("Enter author name: ")
            author = Author.find_by_name(name)
            if author:
                articles = author.articles()
                print(f"Articles by {author.name}:")
                for article in articles:
                    print(f"- {article['title']}")
            else:
                print("Author not found")
        elif choice == '7':
            name = input("Enter magazine name: ")
            magazine = Magazine.find_by_name(name)
            if magazine:
                articles = magazine.articles()
                print(f"Articles in {magazine.name}:")
                for article in articles:
                    print(f"- {article['title']}")
            else:
                print("Magazine not found")
        elif choice == '8':
            name = input("Enter magazine name: ")
            magazine = Magazine.find_by_name(name)
            if magazine:
                contributors = magazine.contributors()
                print(f"Contributors to {magazine.name}:")
                for author in contributors:
                    print(f"- {author['name']}")
            else:
                print("Magazine not found")
        elif choice == '9':
            name = input("Enter author name: ")
            author = Author.find_by_name(name)
            if author:
                magazines = author.magazines()
                print(f"Magazines {author.name} has contributed to:")
                for magazine in magazines:
                    print(f"- {magazine['name']} ({magazine['category']})")
            else:
                print("Author not found")
        elif choice == '10':
            top_magazine = Magazine.top_publisher()
            if top_magazine:
                print(f"Top publisher: {top_magazine.name} ({top_magazine.category})")
            else:
                print("No magazines found")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 