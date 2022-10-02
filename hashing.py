import hashlib


def hashing(personal_key: str, data: str) -> str:
    """Provide the hash 256 of the value you want to hashing.
    
    :param personal_key: (str) the key word to use for a very high hashing. 
    It's any word, not particular word to put. Example: You can put like personal_key = 'word'.
    :param data: (str) the data you want to hash.
    :return: (str) the hashing value. 
    """
    key = personal_key.encode("UTF8")
    data = data.encode("UTF8")
    hash_ = hashlib.sha256(key+data).hexdigest()
    return hash_


if __name__ == '__main__':
    p_k = input("Enter your personal key for the hashing: ")
    d = input("Enter data you want to hash: ")
    
    hash = hashing(p_k, d)
    print("\nThe hash :", hash)
    