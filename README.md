# Article Management System

A Python-based system for managing relationships between Authors, Articles, and Magazines using SQLite database.

## Features

- Manage Authors, Articles, and Magazines
- Track relationships between entities
- Query articles by author or magazine
- Find contributing authors and their works
- Analyze magazine publishing statistics

## Setup

1. Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

2. Install dependencies:
```bash
pip install pytest
```

3. Set up the database:
```bash
python scripts/setup_db.py
```

4. Seed the database with sample data:
```bash
python lib/db/seed.py
```

## Usage

### Interactive Debug Console

Run the debug console to interact with the system:
```bash
python lib/debug.py
```

Available commands:
1. List all authors
2. List all magazines
3. List all articles
4. Find author by name
5. Find magazine by name
6. Find articles by author
7. Find articles by magazine
8. Get magazine contributors
9. Get author's magazines
10. Get top publisher

### Running Tests

Run the test suite:
```bash
pytest
```

## Project Structure

```
code-challenge/
├── lib/                    # Main code directory
│   ├── models/            # Model classes
│   │   ├── author.py      # Author class
│   │   ├── article.py     # Article class
│   │   └── magazine.py    # Magazine class
│   ├── db/               # Database components
│   │   ├── connection.py  # Database connection
│   │   ├── seed.py       # Seed data
│   │   └── schema.sql    # Database schema
│   └── debug.py          # Interactive console
├── scripts/              # Helper scripts
│   └── setup_db.py       # Database setup
└── tests/               # Test directory
```

## Database Schema

The system uses SQLite with the following schema:

- `authors`: Stores author information
- `magazines`: Stores magazine information
- `articles`: Links authors and magazines with articles

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 