from fractions import Fraction
import numpy as np
import math

calc = input("integration or diff or binomial: ")

if calc == "binomial":
    #variable inputs
    a = int(input("please enter the A variable"))
    b = float(fraction(input("please enter the B variable")))
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

elif calc == "integration":
    type = input("normal,sub")
    if type == "normal":
    
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
    elif type == "sub":
        #user inputs 2x^4,9x^3,7x^2,8x,2 
        u = input("please enter the value of u with , seperating them")
        uvar = int(input("please enter the number of variables in u"))
        uarr = u.split(",", uvar)
        #print(uarr)
        uvarinit = 0
        du = []
        while uvarinit <= uvar:
            #creating inital u variables
            var = uarr[uvarinit]
            base = var.split("x")
            baselen = len(base)
            power = var.split("^")
            base = base[0]
            #checking if there is a symbol
            if baselen == 2:
                powerlen = len(power)
                #check if a power is present
                if powerlen < 2:
                    power = 1
                else:
                    power = power[1]
                #string to integer conversion
                base = int(base)
                power = int(power)
                #integration
                integration = base*power
                power = power - 1
                dudx = []
                if power == 0:
                    print(integration)
                    dudx.append(integration)
                    du.append(dudx)
                    uvarinit = uvarinit +1
                    if uvarinit == uvar:
                        break
                else:
                    #test output 
                    ##print(integration,"x^",power)
                    #adding result to array
                    powersym = "x^"
                    dudx.append(integration)
                    dudx.append(powersym)
                    dudx.append(power)
                    #adding array to master array
                    du.append(dudx)
                    #restarting loop
                    uvarinit = uvarinit + 1
                    if uvarinit == uvar:
                        break
            elif baselen == 1:                 
                dudx = []
                base = int(base)
                base = 0
                integration = 0
                dudx.append(integration)
                du.append(dudx)
                uvarinit = uvarinit + 1
                if uvarinit == uvar:
                    break
        #prints master array
        print(du)
        

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

elif calc == "logs":
    var = int(input("please enter a value"))
    base = int(input("please enter the base value"))
    log = math.log(var,base)
    print(log)
    print("log",base,"^",var)
