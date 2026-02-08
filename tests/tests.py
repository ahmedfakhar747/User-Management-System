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

def test_large_database_search():
    """Test search performance with many users"""
    db = UserDatabase()

    for i in range(100):
        db.insert(User(f"user{i:03d}", f"Name {i}", f"user{i}@gmail.com"))

    assert db._find_user_by_username("user050") is not None
    assert db._find_user_by_username("user999") is None

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
