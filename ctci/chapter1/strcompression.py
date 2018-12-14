"""Solution to 1.6: String Compression."""


def compress(string):
    """Creates a compressed strong using repeat characters
    
    Args:
        string_one: any string to be compressed.

    Returns:
        A compressed version of the input based on repeat occurences

    Raises:
        ValueError: string input is empty.
    """    
    if string:
        current = ''
        count = 0
        temp = list()

        for character in string:
            if count == 0:
                current = character
                count += 1
            elif character == current:
                count += 1
            elif character != current:
                temp.append(current + str(count))
                current = character
                count = 1
        temp.append(current + str(count))
        return ''.join(temp)
    raise ValueError('empty string input given')