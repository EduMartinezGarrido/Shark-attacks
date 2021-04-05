def fatal(x):
    if x == " N" or x == "N " or x == "N":
        return "NO"
    elif x == "y" or x == "Y":
        return "YES"
    elif x == "M" or  x == "2017":
        return "UNKNOWN"
    else:
        return x

def sex(x):
    if x == "M " or x == "M":
        return "MALE"
    elif x == "F":
        return "FEMALE"
    elif x == "lli" or  x == "N" or x == ".":
        return "UNKNOWN"
    else:
        return x