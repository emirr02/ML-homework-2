import pytest
from feature_engineering import hash_feature

def test_hash_feature_string():
    """Test hashing a string."""
    val = "test_value"
    hashed = hash_feature(val)
    assert isinstance(hashed, int)
    # Ensure determinism within the same run (Python's hash randomization might affect cross-run)
    assert hash_feature(val) == hashed

def test_hash_feature_int():
    """Test hashing an integer."""
    val = 123
    hashed = hash_feature(val)
    assert isinstance(hashed, int)
    assert hash_feature(val) == hashed
