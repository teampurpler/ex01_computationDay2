# ## Sorting algorithm
# # Bubble sort / Time C: O(n^2) Space C:O(1)
def bubble_sort(list):
    for n in range(len(list)-1,0,-1):
        print('level: ',n)
        for j in range(n):
            print('compare: ',j)
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
                print('after swap: ', list)

print(bubble_sort([9,5,3,7,1]))
#
# #solution 2
def bubble_sort(list):
    for n in range(0,len(list)):
        print('level: ',n)
        for j in range(len(list)-1-n):
            print('compare: ',j)
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                print('after swap: ', list)


print(bubble_sort([9, 5, 3, 7, 1]))
#
# #solution 3
print('Solution3: ')
def bubble_sort(list):
    for n in range(len(list)):
        print('level: ',n)
        for j in range(len(list)-1,n,-1):
            print('compare: ',j)
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
                print('after swap: ', list)

print(bubble_sort([10,8,6,4,2]))


# SELECTION SORT - thoughts: Find the MAX # , swap with the lst number
# step 1: find the max #

def find_max(list):
    max_index = 0
    for i in range(len(list)):
        if list[i]>list[max_index]:
            max_index = i
    print(list[max_index])

(find_max([6,9,3,5]))

#Solution1 - swap max
def selection_sort(list):
    for i in range(len(list)-1,0,-1):
        max_index = 0
        for j in range(i+1):
            if list[j]>list[max_index]:
                max_index = j
        list[i],list[max_index] = list[max_index],list[i]
    return list
print(selection_sort([10,8,6,4,2]))
#
# #Solution2- swap min
def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i, len(list)):
            if list[j]<list[min_index]:
                min_index = j
        list[i],list[min_index] = list[min_index],list[i]
    return list
print(selection_sort([7,3,8,1,10]))

#Insersion sort

def insert_num(array,num):
    idx = len(array)-1
    array.append(num)
    while idx >= 0:
        if array[idx]>array[idx+1]:
            array[idx+1],array[idx] = array[idx],array[idx+1]
        else:
            break
        idx = idx -1
    print(array)

def insertion_sort(array):
    new_arr= []
    for i in range(len(array)):
        insert_num(new_arr,array[i])
    return new_arr

print(insertion_sort([5,6,3,2]))

# better insertion sort
def insertion_sort(list):
    for i in range(1,len(list)):
        cur_value = list[i]
        k = i
        while k > 0 and cur_value< list[k-1]:
            list[k] = list[k-1]
            k -= 1
        list[k] = cur_value
    return list

print(insertion_sort([6,4,3,8,2,7]))

# i is a cutting board, before this board, the nums are ordered
# O(n^2) O(1)


