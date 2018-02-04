"""Bytes and Str in python3."""

def to_str(bytes_or_str):
    """Bytes to str."""
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

def to_bytes(bytes_or_str):
    """Str to bytes."""
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

def main():
    """Main func."""
    a = "test"
    a = to_bytes(a)
    print(a)
    a = to_str(a)
    print(a)

if __name__ == '__main__':
    main()
    