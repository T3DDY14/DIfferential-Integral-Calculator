from fractions import Fraction
import numpy as np
import math

calc = input("integration or diff or binomial: ")

if calc == "binomial":
    #variable inputs
    a = int(input("please enter the A variable"))
    b = int(input("please enter the B variabel"))
    power = float(Fraction(input("enter the power")))
    powercheck = (power).is_integer()
    if powercheck == True:
        if power == 0:
            print("1")
        elif power == 1:
            print(a,"+",b)
        elif power >= 2:
            num = int(input("please enter how many variables you want"))
            num2 = 0
            print(a,"^",power)
            while num2 <= num: #binomial expansion
                num2 = num2 + 1
                ncr = math.factorial(num)/math.factorial(num2)*math.factorial(num-num2)
                print(ncr,"x",a,"^",power-1,"x",b,"^",num2)
                print(ncr*(a**(power-1))*(b**num2))
                power = power - 1
                if num2 == num:
                    break
    elif powercheck == False:
        num = int(input("please enter how many variables you want"))
        num2 = 0
        print(a,"^",power)
        while num2 <= num: #binomial expansion
            num2 = num2 + 1
            ncr = math.factorial(num)/math.factorial(num2)*math.factorial(num-num2)
            print(ncr,"x",a,"^",power-1,"x",b,"^",num2)
            print(ncr*(a**(power-1))*(b**num2))
            power = power - 1
            if num2 == num:
                break
    else:
        print("error")
        exit

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










