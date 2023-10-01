import csv
import json
import numpy as np
from typing import Callable


books_file_path = 'files/books.csv'
users_file_path = 'files/users.json'

def get_books_json(path: str):
    books = []
    with open(path, 'r') as file:
        books_file = csv.DictReader(file)
        for row in books_file:
            books.append(row)

    books_dct = []
    for book in books:
        d = {"title": book["Title"],
             "author": book["Author"],
             "pages": book["Pages"],
             "genre": book["Genre"]}

        books_dct.append(d)

    return books_dct


def get_users_json(path: str):
    users = []
    with open(path, "r") as file:
        users_file = json.loads(file.read())

    for user in users_file:
        d = {"name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"]}

        users.append(d)

    return users


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


def get_result_json(books: Callable[[...], dict], users: Callable[[...], dict]):
    splitted_books = list(split(books, len(users)))

    for i, part in enumerate(splitted_books):
        users[i]['books'] = part

    return users


result = get_result_json(get_books_json(books_file_path), get_users_json(users_file_path))
json_result = json.dumps(result, indent=4)

print(json_result)
