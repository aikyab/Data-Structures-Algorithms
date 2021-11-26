arr = [5,8,3,6,7,4,2]
binary = []
for num in arr:
    binary.append(bin(num)[2:].count('1'))

def merge_sort(arr,binary):

    if len(arr)>1:

        mid = len(arr)//2
        left_arr = arr[:mid]
        left_binary =binary[:mid]
        right_arr = arr[mid:]
        right_binary = binary[mid:]
        merge_sort(left_arr,left_binary)
        merge_sort(right_arr,right_binary)

        i = j = k= 0

        while(i<len(left_arr) and j<len(right_arr)):
            if left_binary[i]<right_binary[j]:
                binary[k] = left_binary[i]
                arr[k] = left_arr[i]
                i+=1
            elif left_binary[i]==right_binary[j]:
                if left_arr[i]<=right_arr[j]:
                    arr[k] = left_arr[i]
                    binary[k] = left_binary[i]
                    i+=1
                else:
                    arr[k] = right_arr[j]
                    binary[k] = right_binary[j]
                    j+=1
            else:
                binary[k] = right_binary[j]
                arr[k] = right_arr[j]
                j+=1
            k+=1
        while(i<len(left_arr)):
            arr[k] = left_arr[i]
            binary[k] = left_binary[i]
            i+=1
            k+=1
        while(j<len(right_arr)):
            arr[k] = right_arr[j]
            binary[k] = right_binary[j]
            j+=1
            k+=1

merge_sort(arr,binary)
print(arr)
