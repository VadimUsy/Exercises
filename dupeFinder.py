
def dupeFinder(arr):
    j = 0
    
    if (len(arr) > 1):
        for i in range(len(arr)):
            j = i+1
            while (j < len(arr)):
                if (arr[i] == arr[j]):
                    return i
                j+=1

    else:
        return -1


arr = [1,6,4,7,34, 8, 23, 2, 37, 55, 20, 23]
print(dupeFinder(arr))