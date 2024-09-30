import random
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1

    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quickselct(arr,low,high,k):
    if low<=high:
        pivot_index=partition(arr,low,high)

        if pivot_index==k:
            return arr[pivot_index]
        elif pivot_index>k:
            return quickselct(arr,low,pivot_index-1,k)
        else:
            return quickselct(arr,pivot_index+1,high,k)
        
def kth_smallest(arr,k):
    return quickselct(arr,0,len(arr)-1,k-1)
arr=[7,10,4,3,20,15]
k=3
print(f"The {k}-th smallest element is {kth_smallest(arr,k)}")
