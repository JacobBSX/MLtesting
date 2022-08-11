# J Ellwood - 10/08/2022 - Sorting Algorithms for data

#InsertionSort
def InsertSort(array):
    for i in range(1,len(array)):
        index = array[i]
        j = i-1
        while j >= 0 and index < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = index
    return array

#BogoSort

#MergeSort
def MergeSort(array):
    if len(array) > 1:
        middle = len(array)//2
        left = array[:middle]
        right = array[middle:]
        MergeSort(left)
        MergeSort(right)
        newArray = Merge(array, left, right)
        #print(newArray)
        return newArray
    return

        

def Merge(array, left, right):
    print("Implement me!")
    i = 0
    j = 0
    k = 0 # Iterator for main list

    print("Merge, ",left," ", right)

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            # The value from the left half has been used
            array[k] = left[i]
            # Move the iterator forward
            i += 1
        else:
            array[k] = right[j]
            j += 1
        # Move to the next slot
        k += 1

        # For all the remaining values
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k]=right[j]
            j += 1
            k += 1
    print(array)
    return array




if __name__ == "__main__":
    # Load test data
    print("Insertion Sort Test:")
    insertionList = [10,5,2,4,9,6,7,1,8,3]
    print("List: ", insertionList)
    print("Sorted List: ", InsertSort(insertionList))

    print("\n\nMerge Sort Test:")
    mergeList = [100, 45, 60, 2]
    print("List: ", mergeList)
    print("Sorted List:", MergeSort(mergeList))
    # TestData.Load yadayada
    # Run Tests
    print("\n######## Testing Complete ########")

