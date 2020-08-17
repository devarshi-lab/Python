
def factors(x):
    j=0
    for i in range(1,int((x/2)+1)):
        if(x % i == 0):
            j = int(j+i)
    return j






