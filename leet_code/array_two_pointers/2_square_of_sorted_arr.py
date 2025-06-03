arr = [-4, -1, 0, 3, 10]

import collections
def square_of_sorted_arr(arr):
    l, r = 0, len(arr)-1

    res = collections.deque()
    while l<=r:
        left, right = abs(arr[l]), abs(arr[r])
        if left> right:
            res.appendleft(left*left)
            l+=1
        else:
            res.appendleft(right*right)
            r-=1


    return res


print(square_of_sorted_arr(arr))