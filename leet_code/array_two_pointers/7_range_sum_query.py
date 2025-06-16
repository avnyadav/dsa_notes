arr =[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]




def range_sum(arr):
    num = arr[0][0]

    sum_arr = [0]

    total = 0
    for n in num:
        total+=n
        sum_arr.append(total)
    
    ans = []
    print(sum_arr)
    for idx in range(1,len(arr)):
        l,r = arr[idx]
    
        ans.append(sum_arr[r+1]-sum_arr[l])
    return ans


res = range_sum(arr)
print(res)