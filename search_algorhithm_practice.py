# naive seach is going through every index of a list and check if the value is equal to the target
# if yes then return the index
# if no then return -1

def naive_search(list, target):
    for item in list:
        if list[item] == target:
            return item
    return -1


# binary search uses divide and conquer
# it splits the list in two until it finds the target value in the list

def binary_search(list, target, low = None, high = None):
    midpoint = len(list) // 2
    if low is None:
        low = 0
    if high is None:
        high = len(list)-1
        
    
    if list[midpoint] == target:
        return midpoint
    elif target < list[midpoint]:
        return binary_search(list, target, low, midpoint-1)
    else:
        # target  > l[midpoint]
        return binary_search(list, target, midpoint+1, low)