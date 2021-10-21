def bubble_sort(arr):
    size = len(arr)
    for j in range(size-1):
        swapped = False
        for i in range(size-1-j):
            if arr[i]>arr[i+1]:
                temp = arr[i+1]
                arr[i+1]=arr[i]
                arr[i] = temp
                print(arr)
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    bubble_sort([13,4,5,1,19])

