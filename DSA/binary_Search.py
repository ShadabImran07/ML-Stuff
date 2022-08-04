from linear_Search import verify,numbers

def binary_search(lst, target):
    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = (first + last)//2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            first = mid + 1
        else:
            last = mid - 1

    return None

# def recursive_binary_search(list, target, start=0, end=None):
#     if end is None:
#         end = len(list) - 1
#     if start > end:
#         return -1
#
#     mid = (start + end) // 2
#
#     if target == list[mid]:
#         return mid
#     else:
#         if target < list[mid]:
#             return recursive_binary_search(list, target, start, mid-1)
#         else:
#             return recursive_binary_search(list, target, mid+1, end)

results = binary_search(numbers,15)
verify(results)






