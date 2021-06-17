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
    mid = len(seq)//2
    new_seq = sum(zip(seq[:mid], reversed(seq[mid:])), ())

    # Zip doesn't account for Odd length
    if len(seq) % 2 != 0: 
        new_seq += (seq[mid],)

    return int("".join(new_seq))
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
