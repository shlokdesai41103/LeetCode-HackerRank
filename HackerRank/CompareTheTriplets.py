def compareTriplets(a, b):
    # Write your code here
    alice = 0
    bob = 0
    comparision = []
    for i in range (len(a)):
        if a[i] > b[i]:
            alice+=1
        elif b[i] > a[i]:
            bob+=1
    comparision.insert(0, alice)
    comparision.insert(1, bob)
    return comparision