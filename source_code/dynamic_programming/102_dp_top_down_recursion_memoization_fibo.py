from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

fibo_result=dict()
def fibonacci(n):
    if n==1 or n==0:
        return n

    if fibo_result.get(n,None):
        return fibo_result[n]
    
    fibo_result[n]=fibonacci(n-1)+fibonacci(n-2)
    return fibo_result[n]
    


if __name__=="__main__":
    n=int(input())

    print(fibonacci(n))
  

