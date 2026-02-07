import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
from ums.core.models import User, UserDatabase

# ===== DATABASE ERROR HANDLING TESTS =====


def test_duplicate_username_case_variations():
    """Test all case variations of duplicate username"""
    db = UserDatabase()
    db.insert(User("testuser", "Test", "test@gmail.com"))

    variations = ["TESTUSER", "TestUser", "testUSER", "tEsTuSeR"]
    for variant in variations:
        result = db.insert(User(variant, "Test2", f"test{variant}@gmail.com"))
        assert result == False, f"Should reject '{variant}'"


def test_duplicate_email_case_variations():
    """Test all case variations of duplicate email"""
    db = UserDatabase()
    db.insert(User("user1", "Test", "Test@Gmail.Com"))

    variations = ["test@gmail.com", "TEST@GMAIL.COM", "TeSt@GmAiL.cOm"]
    for variant in variations:
        result = db.insert(User(f"user_{variant[0]}", "Test2", variant))
        assert result == False, f"Should reject '{variant}'"


# ===== BOUNDARY TESTS =====


def test_max_length_username():
    """Test very long username is accepted"""
    long_username = "a" * 100
    db = UserDatabase()
    user = User(long_username, "Name", "test@gmail.com")
    assert db.insert(user) == True


# ===== SEARCH EDGE CASES =====


def test_find_with_extra_spaces():
    """Test find works with trimmed input"""
    db = UserDatabase()
    db.insert(User("testuser", "Test", "test@gmail.com"))

    assert db._find_user_by_username("  testuser  ") is None  # Not trimmed by search
    assert db._find_user_by_email("  test@gmail.com  ") is None


def test_find_partial_match():
    """Test that partial username/email don't match"""
    db = UserDatabase()
    db.insert(User("testuser", "Test", "test@gmail.com"))

    assert db._find_user_by_username("test") is None
    assert db._find_user_by_email("test@") is None


# ===== STRESS TESTS =====


def test_large_database_insert():
    """Test inserting many users maintains sort order"""
    db = UserDatabase()
    usernames = ["zara", "bilal", "ahmed", "malik", "farah", "hassan"]

    for username in usernames:
        db.insert(User(username, "Name", f"{username}@gmail.com"))

    stored = [u.username for u in db.users]
    assert stored == sorted(usernames)


def test_large_database_search():
    """Test search performance with many users"""
    db = UserDatabase()

    for i in range(100):
        db.insert(User(f"user{i:03d}", f"Name {i}", f"user{i}@gmail.com"))

    assert db._find_user_by_username("user050") is not None
    assert db._find_user_by_username("user999") is None


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

    assert db._find_user_by_username("BILAL") is not None
    assert db._find_user_by_username("ghost") is None


def test_find_email():
    db = UserDatabase()
    db.insert(User("zara", "Zara Khan", "zara@gmail.com"))

    assert db._find_user_by_email("ZARA@GMAIL.COM") is not None
    assert db._find_user_by_email("ghost@gmail.com") is None


def test_empty_database():
    db = UserDatabase()

    assert db._find_user_by_username("nope") is None
    assert db._find_user_by_email("nope@gmail.com") is None
