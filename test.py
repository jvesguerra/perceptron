arr1 = [0,0,0]

print(arr1)


def change_arr(arr):
    for i in range(0, len(arr)):
        arr[i] = 1
    return arr

arr1 = change_arr(arr1)

print(arr1)