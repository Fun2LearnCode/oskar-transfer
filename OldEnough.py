drivingAge = eval(input("At what age can you drive where you live?"))
age = eval(input("How old are you?"))
if age>=drivngAge:
    print("You are old enough to drive!")
if age < drivingAge:
    print("Sorry you have to wait ",drivingAge - age,"years to drive")
