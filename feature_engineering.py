
def hash_feature(feature_value):
    """
    A simple mock hashing function for data preprocessing.
    """
    if not isinstance(feature_value, str):
        feature_value = str(feature_value)
    
    # Using python's built-in hash for simplicity in this mock
    return hash(feature_value)
