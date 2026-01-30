import pytest
from models import User, UserDatabase


def test_insert_first_user():
    db = UserDatabase()
    user = User("ahmed", "Ahmed Fakhar", "ahmed@gmail.com")

    db.insert(user)

    assert len(db.users) == 1
    assert db.users[0].username == "ahmed"


def test_sorted_insertion():
    db = UserDatabase()

    db.insert(User("zara", "Zara Khan", "zara@gmail.com"))
    db.insert(User("bilal", "Bilal Ali", "bilal@gmail.com"))
    db.insert(User("ahmed", "Ahmed Fakhar", "ahmed@gmail.com"))

    usernames = [u.username for u in db.users]
    assert usernames == ["ahmed", "bilal", "zara"]


def test_username_uniqueness_case_insensitive():
    db = UserDatabase()

    db.insert(User("ahmed", "Ahmed", "ahmed@gmail.com"))
    db.insert(User("Ahmed", "Ahmed Clone", "ahmed2@gmail.com"))

    assert len(db.users) == 1


def test_email_uniqueness_case_insensitive():
    db = UserDatabase()

    db.insert(User("ahmed", "Ahmed", "ahmed@gmail.com"))
    db.insert(User("ahmed2", "Ahmed Two", "AHMED@gmail.com"))

    assert len(db.users) == 1


def test_same_name_allowed():
    db = UserDatabase()

    db.insert(User("ahmed", "Ahmed", "ahmed@gmail.com"))
    db.insert(User("ahmed2", "Ahmed", "ahmed2@gmail.com"))

    assert len(db.users) == 2


def test_same_username_blocked():
    db = UserDatabase()

    db.insert(User("zara", "Zara Khan", "zara@gmail.com"))
    db.insert(User("zara", "Zara New", "zara2@gmail.com"))

    assert len(db.users) == 1


def test_same_email_blocked():
    db = UserDatabase()

    db.insert(User("zara", "Zara Khan", "zara@gmail.com"))
    db.insert(User("zara2", "Zara New", "zara@gmail.com"))

    assert len(db.users) == 1


def test_find_username():
    db = UserDatabase()
    db.insert(User("bilal", "Bilal Ali", "bilal@gmail.com"))

    assert db._find_user_by_username("BILAL") is True
    assert db._find_user_by_username("ghost") is False


def test_find_email():
    db = UserDatabase()
    db.insert(User("zara", "Zara Khan", "zara@gmail.com"))

    assert db._find_user_by_email("ZARA@GMAIL.COM") is True
    assert db._find_user_by_email("ghost@gmail.com") is False


def test_empty_database():
    db = UserDatabase()

    assert db._find_user_by_username("nope") is False
    assert db._find_user_by_email("nope@gmail.com") is False