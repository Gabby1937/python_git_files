
Temp = int(input("What is your body temperature: "))
if Temp > 40:
    print("Your Temp is too high")
    print('Please consult your doctor')
elif Temp < 37:
    print("Your Temp is too low")
    print('Please consult your doctor')
else:
    print("You are perfectly fine.")



normal_Temp = range(37,41)
Temp = input("what's your body temperature:  ")
if Temp == normal_Temp:
    print("You are fine.")

elif  Temp < normal_Temp:
    print("Your Temp is too low")
    print('Please consult your doctor')
elif Temp > normal_Temp:
    print("Your Temp is too high")
    print('Please consult your doctor')