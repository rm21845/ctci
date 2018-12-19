"""Solution to 2.7: Intersection."""


def intersect(list_one, list_two):
    length_one = len(list_one)
    length_two = len(list_two)
    diff = abs(length_one - length_two)
    head_one = list_one.head
    head_two = list_two.head
    
    while range(max(length_one, length_two)):
        if diff > 0:
            diff -= 1
            if length_one > length_two:
                head_one = head_one.next_node
            else:
                head_two = head_two.next_node
        else:
            if head_one is head_two:
                return head_one
            head_one = head_one.next_node
            head_two = head_two.next_node