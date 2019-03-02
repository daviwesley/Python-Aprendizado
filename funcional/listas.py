list = range(1,12)

def search(lst, key):
    if not lst:         # base case: list is empty
        return False
    elif lst[0] == key: # base case: current element is searched element
        return True
    else:               # recursive case: advance to next element in list
        return search(lst[1:], key)
        
search(list, 3)
