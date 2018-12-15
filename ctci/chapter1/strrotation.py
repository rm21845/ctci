"""Solution to 1.9: String Rotation."""


def rotate(string_one, string_two):
    """Determines if one string is a rotation of the other.
    
    Args:
        string_one: any string of characters.
        string_two: any string of characters.

    Returns:
        True: if string_one is a rotation of string_two
        False: if string_one is not a rotation of string_two
    """
    if len(string_one) == len(string_two):
        string_two += string_two
        if string_one in string_two: return True
    return False