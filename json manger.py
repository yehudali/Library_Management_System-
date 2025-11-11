import json
books = [
    {"title": "1984", "author": "George Orwell", "isbn": 9780451524935},
    {"title": "Brave New World", "author": "Aldous Huxley", "isbn": 9780060850524},
    {"title": "The Stranger", "author": "Albert Camus", "isbn": 9780679720201},
    {"title": "Man's Search for Meaning", "author": "Viktor E. Frankl", "isbn": 9780807014295},
    {"title": "Meditations", "author": "Marcus Aurelius", "isbn": 9780140449334},
    {"title": "Atomic Habits", "author": "James Clear", "isbn": 9780735211292},
    {"title": "The 7 Habits of Highly Effective People", "author": "Stephen R. Covey", "isbn": 9780743269513},
    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "isbn": 9781585424337},
    {"title": "The Power of Now", "author": "Eckhart Tolle", "isbn": 9781577314806},
    {"title": "Deep Work", "author": "Cal Newport", "isbn": 9781455586691}
]


with open("sfarim.json", "w")as file:
    loaded_data = json.dumps(books, indent=4)
    file.write(loaded_data)
print(loaded_data)
