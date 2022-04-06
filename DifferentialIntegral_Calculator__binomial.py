from fractions import Fraction
import numpy as np

calc = input("integration or diff")
if calc == "integration":
    num = int(input("how many variables")) #input number of variables
    arr = np.array([])
    while num > 0: #loop for number of variables
        #variable inputs
        var = float(Fraction(input("enter the base")));
        letter = input("enter the letter");
        power = float(Fraction(input("enter the power")));
        #integration
        var = var/power
        power = power + 1
        #Simplication + cleanup
        if power == 1.0:
            var = str(var)
            varone = (var,letter)
            varone = ''.join(varone)
        else:
            var = str(var)
            power = str(power)
            varone = (var,letter,"^",power)
            varone = ''.join(varone)
        arr = np.append(arr,varone)
        num = num - 1
    print(arr) #prints the final array
    exit

elif calc == "diff":
    num = int(input("how many variables")) #input number of variables
    arr = np.array([])
    while num > 0: #loop for number of variables
        #variable inputs
        var = float(Fraction(input("enter the base")));
        letter = input("enter the letter");
        power = float(Fraction(input("enter the power")));
        #differentiation
        var = var*power
        power = power - 1
        #Simplication + cleanup
        if power == 1.0:
            var = str(var)
            varone = (var,letter)
            varone = ''.join(varone)
        else:
            var = str(var)
            power = str(power)
            varone = (var,letter,"^",power)
            varone = ''.join(varone)
        arr = np.append(arr,varone)
        num = num - 1
    print(arr) #prints the final array
    exit










