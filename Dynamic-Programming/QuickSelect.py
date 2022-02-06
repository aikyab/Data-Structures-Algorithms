nums = [1,1,1,2,2,3]
count = Counter(nums)
nums = list(count.keys())
k=2
def quickSelect(start,end,stopIndex):
    if start<end:
        index = partition(start,end)
        if stopIndex==index:
            return
        elif stopIndex<index:
            quickSelect(start,index-1,stopIndex)
        else:
            quickSelect(index+1,end,stopIndex)
            
    
def partition(start,end):
    pivot = nums[end]
    pIndex = start
    for i in range(start,end):
        if count[nums[i]]>=count[pivot]:
            nums[i],nums[pIndex] = nums[pIndex],nums[i]
            pIndex+=1
    nums[pIndex],nums[end] = nums[end],nums[pIndex]
    return pIndex

quickSelect(0,len(nums)-1,k-1)
print(nums[:k])
