import copy


    
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
    solve(arr,0,output,ans)
    print(ans)