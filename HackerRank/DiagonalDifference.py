def diagonalDifference(arr):
    # Write your code here
    d1Sum = 0
    d2Sum = 0
    j = 0
    k = 0
    
    for i in range(len(arr)):
        d1Sum += arr[i][k]
        k+=1
    
    j = 0
    k = len(arr[0])-1
    
    for i in range(len(arr)):
        d2Sum += arr[i][k]
        k-=1
        
    return abs(d1Sum-d2Sum)