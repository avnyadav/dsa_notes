import copy

def solve_using_bit(numbers):
    n = len(numbers)
    total_subsets = 1<<n  #2^n using bit wise operation
    ans = []
    for ith_subset in range(1,total_subsets):
        output = []
        for i in range(n):
            if ith_subset & (1<<i):
                output.append(numbers[i])
        ans.append(output)
    return ans


def solve(numbers,idx,output,ans):
    if idx>=len(numbers):
        if len(output)>0:
            ans.append(output)
        return
    
    solve(numbers,idx+1,copy.deepcopy(output),ans)
    output.append(numbers[idx])
    solve(numbers,idx+1,copy.deepcopy(output),ans)


if __name__=="__main__":
    arr = [1,2,3]
    ans=[]
    output=[]
    #solve(arr,0,output,ans)
    print(solve_using_bit(arr))