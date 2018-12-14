"""Solution to 1.2: Check Permutation."""

def check_perm(string_one, string_two):
    """Determines if one string is a permutation of another.
    
    Args:
        string_one: any string of characters.
        string_two: any string of characters.

    Returns:
        True: the strings are permutations.
        False: the strings are not permutations.

    Raises:
        ValueError: one or all of the strings are empty.
    """    
    if string_one and string_two:
        if len(string_one) != len(string_two): return False
        
        for character in string_one:
            if character not in string_two:
                return False
        return True 
    raise ValueError('empty string input given')
    