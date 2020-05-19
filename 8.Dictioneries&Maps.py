import os
import math
import re

n = int(input())
phonebook = {}
for i in range(n):
    key_value = input().split()
    phonebook[key_value[0]] = key_value[1]
for j in range(n):
    x= input()
    if(x in phonebook):
        print(x,"=",phonebook[x], sep="")
    else:
        print("Not found")
