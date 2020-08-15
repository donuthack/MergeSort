'''merge sort'''
'''14.08.20'''


def mergeSort(value):
    if len(value) > 1:
        middle = len(value) // 2  # mediana of our array
        left_side = value[:middle]  # write after mid in right side
        right_side = value[middle:]  # write before mid in left side
        left = mergeSort(left_side)
        right = mergeSort(right_side)

        i = 0  # first part of array
        j = 0  # second part of array
        value = []  # empty list

        '''we will write our indexes in left and right lists'''
        '''and go through array until we reach end of list, or left or right, we will take the largest left or right 
        among elements '''

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                value.append(left[i])
                left.pop(0)
            else:
                value.append(right[j])
                right.pop(0)

        for i in left:
            value.append(i)

        for j in right:
            value.append(j)

    return value


array = [7, 635, 535, 98, 36, 9, 63]
array = mergeSort(array)

print(array)
