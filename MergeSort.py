# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 13:33:56 2021

@author: AUROBINDA
"""

def mergeSortFinal(arr, aux, low, high):
    mid = int((low+high)/2)
    if(low==high):
        return
    else:
        mergeSortFinal(arr,aux,low,mid)
        mergeSortFinal(arr,aux,mid+1,high)
        merge(arr,aux,low,mid,high)
    return aux

def merge(arr,aux,low,mid,high):
    k = low
    i = low
    j = mid+1
    while(i<=mid and j<=high):
        if(arr[i]<arr[j]):
            aux[k] = arr[i]
            i=i+1
            k=k+1
        else:
            aux[k] = arr[j]
            j=j+1
            k=k+1
    
    while(i<=mid):
        aux[k] = arr[i]
        k = k+1
        i = i+1
    while(j<=high):
        aux[k] = arr[j]
        j = j+1
        k = k+1
    for m in range (low,high+1,1):
        arr[m] = aux[m]
        

	
arr = [8,4,3,12,25,6,13,10]
aux = arr.copy()
actual = mergeSortFinal(arr, aux, 0, len(arr) - 1)
print(actual)

