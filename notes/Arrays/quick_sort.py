
def partition(arr,low,high)->int:
    """
    return correct idx of pivot item and 
    """
    pivot = arr[high] 
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    
    i+=1
    arr[high],arr[i]=arr[i],arr[high]
    return i


def quick_sort(arr,low,high):
    if low>high:
        return
    pidx = partition(arr,low,high)
    quick_sort(arr,low,pidx-1)
    quick_sort(arr,low,pidx+1)



if __name__=="__main__":
    arr = [1,43,21,5,1]
    print(f"Arr: {arr}")
    low,high = 0, len(arr)-1
    quick_sort(arr,low,high)
    print(f"Sorted arr: {arr}")