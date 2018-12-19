"""Solution to 2.6: Palindrome."""

def check_with_stack(to_check):
    stack = list()

    [stack.append(node.value) for node in to_check]
    for node in to_check:
        if node.value != stack.pop():
            return False
    return True

def recurse(current, previous=None):
    if not current:
        return previous
    temp = current.next_node
    current.next_node = previous
    previous = current 
    current = temp 
    return recurse(current, previous)

def check_with_recur(to_check):
    runner = to_check.head
    rlist = None

    for node in to_check:
        runner = runner.next_node.next_node
        if not runner:
            rlist = node.next_node  
            node.next_node = None
            break
        elif not runner.next_node:
            rlist = node.next_node.next_node
            node.next_node = None
            break        

    #Reverse list
    to_check.head = recurse(to_check.head)

    for node in to_check:
        if node.value != rlist.value:
            return False
        rlist = rlist.next_node
    return True
