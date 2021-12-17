# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:47:46 2021

@author: AURO
"""

def f(a,k,low,high):
    mid =int(low + ( (high-low)/2))
    
    if(a[mid]==k):
        return mid
    elif(k>a[mid]):
        return f(a,k,mid+1,high)
    else:
        return f(a,k,low,mid-1)

a=[2,4,6,7,8,10]

print(f(a,7,0,len(a)-1))
