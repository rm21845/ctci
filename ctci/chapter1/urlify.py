"""Solution to 1.3: URLify."""

def count_space(string):
    """Counts the number of whitespaces to replace with '%20'.
    
    Args:
        string: non-url compliant string

    Returns:
        The number of whitespaces that need replacement
    """  
    space_count = 0
    for index in range(len(string)):
        character = string[-(index+1)]
        if character.isspace():
            space_count += 1
        else:
            break 
    return space_count / 3

def to_url(string):
    """Replace non-trailing whitespace with '%20'. 
    
    Args:
        string: non-url compliant string

    Returns:
        A url compliant string where %20 fills in whitespace

    Raises:
        ValueError: string value evaluates to empty
    """    
    if string:
        spaces = count_space(string)
        return string.replace(' ', '%20', int(spaces)).rstrip()

    raise ValueError('string: value is empty')