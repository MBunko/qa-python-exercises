i1= str(input("input first word: "))
i2= str(input("input second word: "))

a= len(i1)
b=len(i2)
c=0

if a!=b+1:
    print ("false")
else:
    for i in range (a):
        i3=i1[:i] +i1[(i+1):]
        if i3==i2:
            c=c+1
            
        else:
            continue
    if c==1:
        print ("true")
    else:
        print ("false")
