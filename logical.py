#Logical operator = Evaluate multiple condition (or,and not )
#or = at least one condition must br True
#and = both condition must be True
#Not = inverts the condition (not  False,not true)


#OR
temp = 45
is_raining = False
if temp > 35 or temp <0 or is_raining:
    print("The outdoor event is cancelled ")
else:
    print("The outdoor event is still scheduled")

    #and

temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is Hot Outside🥵🥵")
    print("It is sunny☀️")

elif temp <=0 and is_sunny:
    print("Its is Cold")
    print("it is SUNNY")

elif temp < 28 and temp >0 and is_sunny:
    print("Its is WARM outside")
    print("it is SUNNY")


# not
temp = 298
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is Hot Outside🥵🥵")
    print("It is sunny☀️")

elif temp >= 28 and is_sunny:
    print("It is cold Outside🥵🥵")
    print("It is sunny☀️")
elif temp >= 28 and is_sunny:
    print("It is WARM Outside🥵🥵")
    print("It is sunny☀️")
elif temp >= 28 and not is_sunny:
    print("It is Hot Outside🥵🥵")
    print("It is CLOUDY☀️")
elif temp >= 28 and  not is_sunny:
    print("It is Hot Outside🥵🥵")
    print("It is  CLOUDY ")
