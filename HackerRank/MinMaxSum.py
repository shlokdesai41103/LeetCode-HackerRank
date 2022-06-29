def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min = arr[0]+arr[1]+arr[2]+arr[3]
    max = arr[1]+arr[2]+arr[3]+arr[4]
    print(min, max)