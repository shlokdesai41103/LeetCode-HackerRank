def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zer = 0
    ratio = []
    for i in range (len(arr)):
        if(arr[i] > 0):
            pos+=1
        elif(arr[i] < 0):
            neg+=1
        else:
            zer+=1
    print("%.6f"%(pos/len(arr)))
    print("%.6f"%(neg/len(arr)))
    print("%.6f"%(zer/len(arr)))