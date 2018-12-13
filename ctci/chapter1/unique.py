"""Solution to 1.1 Is Unique."""


def is_unique(string):
    """Determines if a string is unique.
    
    Args:
        string: any string of characters.

    Returns:
        a Boolean value dependant on the uniqueness

    Raises:
        ValueError: Empty string value given as an argument
    """
    temp = list()
    if string:
        for character in string:
            if character in temp:
                return False
            temp.append(character)
        return True
    raise ValueError('string: value is empty')