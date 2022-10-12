def recursive(x):
    #print(x)

    if x >= 10:
        return x
    
    return recursive(x+1)

print(recursive(0))