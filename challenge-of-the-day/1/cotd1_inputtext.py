def alphabet(input):
    list1=input.split()
    length=len(list1)
    sort=sorted(list1)
    dupdrop=[]
    for i in range (0,length):
        if sort[i] not in dupdrop:
            dupdrop.append(sort[i])
    return dupdrop


print (alphabet(input("input text here: ")))