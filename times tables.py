n= int(input("input number"))

for i in range (1,n+1):
    row= format("")
    for j in range (1,n+1):
        row+= "{0:8}  ".format(i*j)
    print (row)
