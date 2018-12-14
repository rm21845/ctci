"""Solution to 1.5: One Away."""

def replace_case(string_one, string_two):
    """Determines if two strings can be made equal with one replace edit.
    
    Args:
        string_one: a string of characters equal in length to string_two
        string_two: a string of characters equal in length to string_one

    Returns:
        False: the strings are not one or less replace edits away
    """  
    edits = False
    for index in range(len(string_one)):
        if string_one[index] != string_two[index]:
            if edits: return False
            edits = True 

def ins_del_case(string_one, string_two):
    """Determines if two strings can be made equal with one insert/delete edit.
    
    Args:
        string_one: a string of characters with difference in 
            length by one with string_two.
        string_two: a string of characters with difference in 
            length by one with string_one.

    Returns:
        False: the strings are not one or less edits away
    """
    index_one = 0
    index_two = 0

    edits = False
    while index_one != len(string_one) and index_two != len(string_two):
        if string_one[index_one] != string_two[index_two]:
            if edits: return False
            edits = True                 
            if string_one[index_one+1] == string_two[index_two]:
                index_one += 1
            else:
                index_two += 1
        else:
            index_one += 1
            index_two += 1

def is_one_away(string_one, string_two):
    """Determines a string is one edit away from another.
    
    Args:
        string_one: any string of characters.
        string_two: any string of characters.

    Returns:
        True: the strings are one or less edits away
        False: the strings are not one or less edits away

    Raises:
        ValueError: one or all of the strings are empty.
    """    
    if string_one and string_two:
        if string_one == string_two: return True
        if len(string_one) == len(string_two):
            replace_case(string_one, string_two)
        if abs(len(string_one) - len(string_two)) == 1:
            ins_del_case(string_one, string_two)
        return True
    raise ValueError('empty string input given')
