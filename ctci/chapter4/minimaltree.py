"""Solution to 3.2: Minimal Tree."""


def min_height(unique):
    root = unique[int(len(unique)/2)]
    
    min_bst = dict()
    root = unique[int(len(unique)/2)]
    left = unique[:int(len(unique)/2)] 
    right = unique[int(len(unique)/2)+1:]

    min_bst[root] = [left, right]
    print(min_bst)
    