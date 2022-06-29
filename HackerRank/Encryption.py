def encryption(s):
    # Write your code here
    l = len(s)
    sqrtL = float (math.sqrt(l))
    if(sqrtL-(int(sqrtL)) == 0):
        lower = upper = int (sqrtL)
    else:  
        lower = int (sqrtL)
        print(lower)
        upper = lower+1
        print(upper)
    
    while((lower*upper < l)):
        print("enter")
        if(lower*lower >= l):
            upper = lower
        elif(upper*upper >= l):
            lower = upper
    
    
    encrypted = []
    encryptedpart = []
    count = 0
    row = 0
    length = 0
    for letter in s:
        encryptedpart.append(letter)
        print(encryptedpart)
        count += 1
        length += 1
        if(count%upper == 0 or length == l):
            print("entered")
            count = 0
            encrypted.append(encryptedpart)
            print(encrypted)
            encryptedpart = []
    print(encrypted)

    line = ""
    for j in range(len(encrypted[0])):
        for i in range(len(encrypted)):
            if(j < len(encrypted[i])):
                line += encrypted[i][j]
        # print(line, end=" ")
        line += " "
            
    return line    