# Q: find target num in a sorted int array, return index if found it.

def binary_search(nums, target):
    if not nums:
        return None
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] > target:
           right = mid -1
        elif nums[mid] < target:
           left = mid + 1
        else:
            return mid
    return None

print(binary_search([2,5,6,7,8,9,10], 10))

# tc : O(logN) sc: O(1)

# 2D space search
def binary_search_2D_(matrix, target):
    if not matrix:
        return None
    N,M = len(matrix),len(matrix[0])
    left, right = 0, N*M - 1
    while left <= right:
        mid = (left+right)//2
        row_num = mid//M
        col_num = mid % M
        if matrix[row_num][col_num] > target:
            right = mid -1
        elif matrix[row_num][col_num] < target:
            left = mid +1
        else:
            return(row_num,col_num)
    return None

print(binary_search_2D_([[1,2,3,4],[5,6,7,8],[9,10,11,12]],2))
# tc = O(logN*M)


# find an element in the array that is closest to the target
def find_closest_num(nums, target):
    if not nums:
        return None
    left = 0
    right = len(nums) - 1
    while left < right -1:
        mid = (left+right)//2
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid
        else:
            return mid
    return left if abs(nums[left]-target) < abs(nums[right]-target) else right

print(find_closest_num([1,2,5,7,9,10],11))

# find the first occurence(nums, target)

def find_first_occurrence(nums, target):
    if not nums:
        return None
    left = 0
    right = len(nums)-1
    while left < right -1:
        mid = (left+right)//2
        if nums[mid] > target:
            right = mid -1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return None

print(find_first_occurrence([1,3,3,3,5,7,3,5],5))
