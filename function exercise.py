def it(hw,ass,exam):
    grade=((hw+ass+exam)/175)*100
    if hw>25:
        return "Error: homework maximum grade 25"
    elif ass>50:
        return "Error: assessment maximum grade 50"
    elif exam>100:
        return "Error: exam maximum grade 100"
    else:
        if grade<40:
            lg="Fail"
        elif grade<50:
            lg="D"
        elif grade<60:
            lg="C"
        elif grade<70:
            lg="B"
        else:
            lg="A"
        return grade, lg

name=str(input("input your name: "))

print(name,":",it(float(input("input homework grade out of 25: ")),float(input("input assessment grade out of 50: ")),float(input("input exam grade out of 100: "))))
