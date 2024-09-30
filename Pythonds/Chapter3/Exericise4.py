def kth_smallest(arr,k):
    arr.sort()

    return arr[k-1]

arr=[7,10,4,3,20,15]

k=3
print(f"The {k}-th smallest element is {kth_smallest(arr,k)}")