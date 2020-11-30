n0= int(input("Please enter first digit: "))
while n0>9 or n0<0:
    n0= int(input("Input must be single digit, Try again: "))

n1= int(input("Please enter second digit: "))
while n1>9 or n1<0:
    n1= int(input("Input must be single digit, Try again: "))

n2= int(input("Please enter third digit: "))
while n2>9 or n2<0:
    n2= int(input("Input must be single digit, Try again: "))

n3= int(input("Please enter fourth digit: "))
while n3>9 or n3<0:
    n3= int(input("Input must be single digit, Try again: "))

n4= int(input("Please enter fifth digit: "))
while n4>9 or n4<0:
    n4= int(input("Input must be single digit, Try again: "))

n5= int(input("Please enter sixth digit: "))
while n5>9 or n5<0:
    n5= int(input("Input must be single digit, Try again: "))

n6= int(input("Please enter seventh digit: "))
while n6>9 or n6<0:
    n6= int(input("Input must be single digit, Try again: "))

n7= int(input("Please enter eigth digit: "))
while n7>9 or n7<0:
    n7= int(input("Input must be single digit, Try again: "))

n8= int(input("Please enter ninth digit: "))
while n8>9 or n8<0:
    n8= int(input("Input must be single digit, Try again: "))

n9= int(input("Please enter tenth digit: "))
while n9>9 or n9<0:
    n9= int(input("Input must be single digit, Try again: "))

n10= int(input("Please enter eleventh digit: "))
while n10>9 or n10<0:
    n10= int(input("Input must be single digit, Try again: "))

n11= int(input("Please enter twelth digit: "))
while n11>9 or n11<0:
    n11= int(input("Input must be single digit, Try again: "))

n12 = 10-(( n0 + (3 * n1) + n2 + (3 * n3) + n4 + (3 * n5) + n6 + (3 * n7) + n8 + (3 * n9) + n10 + (3 * n11) ) % 10)

print (n0,n1,n2,"-",n3,"-",n4,n5,n6,"-",n7,n8,n9,n10,n11,"-",n12)
