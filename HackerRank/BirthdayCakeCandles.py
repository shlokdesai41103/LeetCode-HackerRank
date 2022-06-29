def birthdayCakeCandles(candles):
    # Write your code here
    max = 0
    count = 0
    for i in range(len(candles)):
        if(candles[i] >= max):
            max = candles[i]
            
    for i in range (len(candles)):
        if(candles[i] == max):
            count += 1
    return count