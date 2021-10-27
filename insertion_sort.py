def insertion_sort(arr):
    new = list()
    compare_element = arr [i]
    new[i] = compare_element
    for i in range(1,len(arr)):
        if arr[i] < compare_element:
            for j in new:
                while new[j]!=[]:
                    new[j-1]=new[j]







if __name__ == "__main__":
   arr = [21,38,29,17,4,25,11,32,9]
   print(insertion_sort(arr))