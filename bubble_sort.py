def bubble_sort(arr):
    size = len(arr)
    for j in range(size-1):
        swapped = False
        for i in range(size-1-j):
            if arr[i]['transaction_amount']>arr[i+1]['transaction_amount']:
                temp = arr[i+1]
                arr[i+1]=arr[i]
                arr[i] = temp
                print(arr)
                swapped =True
        if not swapped:
            break


if __name__ == "__main__":
    bubble_sort([
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ])

