from hashlib import sha1
from base64 import b32encode


def git_hash(blob):
    """Return git-hash compatible SHA-1 hexdigits for a blob of data."""
    head = str("blob " + str(len(blob)) + "\0").encode("utf-8")
    return sha1(head + blob).hexdigest()


def encode_hash(hexdigest):
    """Return SHA-1 hexdigits as RFC 3548 base 32 encoding."""
    return b32encode(bytes.fromhex(hexdigest)).decode('utf-8').lower()


def hash(data):
    return encode_hash(git_hash(data))
