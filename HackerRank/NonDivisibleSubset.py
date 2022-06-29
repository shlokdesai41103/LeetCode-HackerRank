def nonDivisibleSubset(k, s):
    # Write your code here
    c = Counter((i%k for i in s))
    count =0
    blacklist= set()
    
    for x,y in c.most_common():
        print(x)
        print(y)
        if x == k/2 or x == 0:
            count+=1
        elif k-x not in blacklist:
            count+=y
            blacklist.add(x)
    return count