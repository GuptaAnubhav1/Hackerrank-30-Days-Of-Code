#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swap=0
i=0
j=0
for j in range(len(a)-1):
    step_swap = 0
    for i in range(len(a)-1):
        if(a[i] > a[i + 1]):
            a[i], a[i + 1] = a[i+1], a[i]
            swap +=1
            step_swap +=1
            continue;
        if(step_swap==0):
            break;
print("Array is sorted in", swap, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[-1])
