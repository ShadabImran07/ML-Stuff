def linear_search(lst, target):
    """
    RETURN THE INDEX POSTION OF THE TARGET IF FOUND, ELSE RETURN NONE
    """

    for i in range(0, len(lst)):
        if lst[i] == target:
            return i
    else:
        return None

#Enumerate function return object means a key value pair think like a ditcnoray.

# def linear_search(lst, target):
#     for index, value in enumerate(lst):
#         if value == target:
#             return index
#     return -1

def verify(index):
    if index is not None:
        print(f"Target found at {index}")

    else:
        print("target not found in list")




numbers = [1,2,3,4,5,6,7,8,9,10]


result = linear_search(numbers, 8)
verify(result)