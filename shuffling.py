def shuffle(seq):
    """
    >>> shuffle(123456)
    162534
    >>> shuffle(130)
    103
    >>> shuffle(0)
    0
    >>> shuffle(10)
    10
    """
    seq = str(seq)
    new_seq = [
        seq[i // 2] if i % 2 == 0 else seq[-(i // 2 + 1)]
        for i in range(len(seq))
    ]
    return int("".join(new_seq))
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
