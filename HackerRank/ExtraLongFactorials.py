def extraLongFactorials(n):
    # Write your code here
    factorial = 1
    
    while(n >= 1):
        factorial *= n
        n -= 1
        
    print(factorial)