def array_check(lst):
    """
    Function to check whether 1,2,3 exists in given array
    """
    for i in range(len(lst)-2):
        if lst[i] == 1 and lst[i+1] == 2 and lst[i+2] == 3:

            return True
    return False


arr = [1, 2, 6, 1, 2, 3, 4]
print(array_check(arr))

arr = [1, 2, 6, 1, 22, 3, 4]
print(array_check(arr))