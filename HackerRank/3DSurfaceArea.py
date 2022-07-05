def surfaceArea(A):
    # Write your code here
    SA = 0
    #SA of top and bottom
    SA += 2*(len(A)*len(A[0]))
    #SA of front and back
    SA += sum(A[0])
    SA += sum(A[len(A)-1])
    #SA of left and right
    for i in range(len(A)):
        SA += A[i][0]
        SA += A[i][len(A[0])-1]
    #SA of area between object
    for i in range(len(A)):
        for j in range(len(A[0])-1):
            if(A[i][j]-A[i][j+1]):
                SA += abs(A[i][j]-A[i][j+1])
                
    for j in range(len(A[0])):
        for i in range(len(A)-1):
            if(A[i][j]-A[i+1][j] != 0):
                SA += abs(A[i][j]-A[i+1][j])
             
    return SA