class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #4 6 8 9 10 20 24 30
        #31
        # Base case
        
        # if len(arr) == k:
        #     return arr
        
#         #Approach 1 -- BS to find left and right closest bounds of x
#         # Following you increment or decrement the pointers to whichever side is closer to x (calculated in terms of the distance between each pointer's value and x)
#         left = 0
#         right = len(arr)-1
#         mid = 0
#         while left<right:
#             mid = left + (right-left)//2
#             if arr[mid]>=x:
#                 right = mid
#             else:
#                 left = mid+1
#         left-=1
#         right = left+1        
#         # left = bisect_left(arr, x) - 1
#         # right = left + 1

#         # While the window size is less than k
#         while right - left - 1 < k:
#             # Be careful to not go out of bounds
#             if left == -1:
#                 right += 1
#                 continue
            
#             # Expand the window towards the side with the closer number
#             # Be careful to not go out of bounds with the pointers
#             if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
#                 left -= 1
#             else:
#                 right += 1
        
#         # Return the window
#         return arr[left + 1:right]

        #Approach 2
        #1 2 3 4 5 6 7 8
        left = 0
        right = len(arr)-k
        while(left<right):
            mid = left + (right-left)//2
            if x - arr[mid] > arr[mid + k] - x:
            # if(abs(arr[mid]-x)>abs(arr[mid+k]-x)):
                left = mid+1
            else:
                right = mid
        return arr[left:left+k]
                
