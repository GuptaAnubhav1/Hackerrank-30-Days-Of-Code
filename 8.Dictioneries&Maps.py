import os
import math
import re

n = int(input())
phonebook = {}
for i in range(n):
    key_value = input().strip().split(" ")
    phonebook[key_value[0]] = key_value[1]
for j in range(n):    
                
    while True:
        try:
            x= input()
            if(x in phonebook):
                print("{}={}".format(x,phonebook[x]))
            else:
                print("Not found")
        except: quit()
