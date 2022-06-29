def turnStr(h):
    if h == 1:
        return "one"
    elif h == 2:
        return "two"
    elif h == 3:
        return "three"
    elif h == 4:
        return "four"
    elif h == 5:
        return "five"
    elif h == 6:
        return "six"
    elif h == 7:
        return "seven"
    elif h == 8:
        return "eight"
    elif h == 9:
        return "nine"
    elif h == 10:
        return "ten"
    elif h == 11:
        return "eleven"
    elif h == 12:
        return "twelve"
    elif h == 13:
        return "thirteen"
    elif h == 14:
        return "fourteen"
    elif h == 15:
        return "fifteen"
    elif h == 16:
        return "sixteen"
    elif h == 17:
        return "seventeen"
    elif h == 18:
        return "eighteen"
    elif h == 19:
        return "nineteen"
    elif h == 20:
        return "twenty"
    elif h == 21:
        return "twenty one"
    elif h == 22:
        return "twenty two"
    elif h == 23:
        return "twenty three"
    elif h == 24:
        return "twenty four"
    elif h == 25:
        return "twenty five"
    elif h == 26:
        return "twenty six"
    elif h == 27:
        return "twenty seven"
    elif h == 28:
        return "twenty eight"
    elif h == 29:
        return "twenty nine"

def timeInWords(h, m):
    # Write your code here
    finalStr = ""
    
    mid = ""
    minutes = ""
    minOrMins = ""
    if m <= 30:
        hours = turnStr(h)
        mid = "past"
        if m%15 == 0:
            if m == 15:
                minutes = "quarter"
                return (minutes + " " + mid + " " + hours)
            elif m == 30:
                minutes = "half"
                return (minutes + " " + mid + " " + hours)
            elif m == 0:
                minutes = "o' clock"
                return (hours + " " + minutes)
            
        else:
            minutes = turnStr(m)
            if m > 1:
                minOrMins = "minutes"
            else:
                minOrMins = "minute"
        return (minutes + " " + minOrMins + " " + mid + " " + hours)
        
    elif m > 30:
        hours = turnStr(h+1)
        mid = "to"
        if m%15 ==0:
            if m == 45:
                minutes = "quarter"
                return (minutes + " " + mid + " " + hours)
        else:
            minutes = turnStr(60-m)
            if m > 1:
                minOrMins = "minutes"
            else:
                minOrMins = "minute"
        return (minutes+" "+minOrMins+" "+mid+" "+hours)