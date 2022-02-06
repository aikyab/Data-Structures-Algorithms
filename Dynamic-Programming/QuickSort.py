1 2 4 3 5
k = 2

def quick_select(arr,start,end,ind):
    if start < end:
        pIndex = partition(arr,start,end)
        if pIndex == ind:
            return
        quick_select(arr,start,pIndex-1,ind)
        quick_select(arr,pIndex+1,end,ind)

def partition(arr,start,end):
    pivot = arr[end]
    pIndex = start
    for i in range(start,end):
        if arr[i]>=pivot:
            arr[pIndex],arr[i] = arr[i],arr[pIndex]
            pIndex+=1
    arr[pIndex],arr[end] = arr[end],arr[pIndex]
    return pIndex
n = len(arr)-1
quick_select(arr,0,n,1)
print(arr[:2])
