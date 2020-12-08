def case(input):
    return "UPPER " + str(sum([int(i.isupper()) for i in input])) + "\nLOWER " + str(sum([int(i.islower()) for i in input]))

