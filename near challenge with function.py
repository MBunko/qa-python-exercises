def near (i1,i2):
    a= len(i1)
    b=len(i2)
    
    if a!=b+1:
        return "false"
    else:
        for i in range (a):
            i3=i1[:i] +i1[(i+1):]
            if i3==i2:
                return "true"
            
            else:
                continue
        return "false"

print (near(str(input("input first word: ")), str(input("input second word: "))))
