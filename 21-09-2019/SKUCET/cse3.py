def natnut(l):
    for i in range(1,l+1):
        print(i,end=" ")
    return

def EvnOdd(li):
    k=[]
    m=[]
    for i in li:
        if i%2==0:
            k.append(i)
        else:
            m.append(i)
    print("Given numbers in list is: {}".format(li))
    print("Even numbers in list is: {}".format(k))
    print("Odd numbers in list is: {}".format(m))
    return 
            