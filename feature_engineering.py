import hashlib

def hash_feature(feature_value):
    """
    A simple mock hashing function for data preprocessing.
    Uses md5 for determinism.
    """
    if not isinstance(feature_value, str):
        feature_value = str(feature_value)
    
    # Deterministic hash
    encoded = feature_value.encode('utf-8')
    return int(hashlib.md5(encoded).hexdigest(), 16)
