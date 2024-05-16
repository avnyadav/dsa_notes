from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

def fibonacci(n,fibo_result ):
    for i in range(2,n+1):
        fibo_result.append(fibo_result[i-1]+fibo_result[i-2]) 
    return fibo_result[-1]

#fibonacci_with_space_optimization

#fibonacci_with_space_optimization
#fibonacci_with_space_optimization
def fibonacci(n):
    prev_1=0
    prev_2=1
    for i in range(2,n+1):
        current=prev_1+prev_2
        prev_1,prev_2=prev_2,current
    return prev_2

if __name__=="__main__":
    n=int(input())
    fibo_result=[0,1] #dp array
    print(fibonacci(n))
  

