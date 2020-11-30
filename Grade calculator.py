Physics= float(input("Enter Physics grade: "))
Maths= float(input("Enter Maths grade: "))
Chemistry= float(input("Enter Chemistry grade: "))

P= (Physics+Maths+Chemistry)/3

G="A"
if P<40:
    G= "You failed"
elif P<50:
    G= "D"
elif P<60:
    G="C"
elif P<70:
    G="B"


print ("Your percentage score is: ",P,"%")
print ("You scored a grade of: ",G)
