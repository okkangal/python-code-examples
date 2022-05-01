def double(a):
    """
    >>> double(2)
    4
    >>> double(3)
    6
    """
    return a*2


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


