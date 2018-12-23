"""Solution 4.4: Check Balanced."""


def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

def is_balanced(node):
    if not node:
        return True
    return is_balanced(node.left) and is_balanced(node.right) and \
        abs(height(node.left) - height(node.right)) <= 1