from fractions import Fraction
import numpy as np
import math
import re

calc = input("integration or differentiation or binomial: ")

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
    type = input("normal,substitution")
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
    elif type == "substitution":
        form = input("please enter the formula without the power")
        formpower = float(Fraction(input("please enter the power")))
        #user inputs 2x^4,9x^3,7x^2,8x,2 
        u = input("please enter the value of u with , seperating them")
        uvar = int(input("please enter the number of variables in u"))
        uarr = u.split(",", uvar)
        #print(uarr)
        uvarinit = 0
        dx = []
        while uvarinit <= uvar:
            #creating inital u variables
            var = uarr[uvarinit]
            base = var.split("x")
            baselen = len(base)
            ##print(base)
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
                if base == '':
                    base = 1
                else:
                    base = int(base)
                power = int(power)
                #differentiation
                integration = base*power
                power = power - 1
                dudx = []
                if power == 0:
                    #adding result to array
                    dudx.append(integration)
                    dx.append(dudx)
                    uvarinit = uvarinit +1
                    if uvarinit == uvar:
                        break
                else:
                    powersym = "x^"
                    #adding dudx to an array
                    dudx.append(integration)
                    dudx.append(powersym)
                    dudx.append(power)
                    #adding dudxarray to master array
                    dx.append(dudx)
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
                dx.append(dudx)
                uvarinit = uvarinit + 1
                if uvarinit == uvar:
                    break
        #prints master array
        du = ("1/",dx[0])
        ulen = len(u)
        ulen = ulen - 1
        intformpower = formpower+1 
        #combining u variables into one
        u = (u[0],"+",u[ulen],"^",intformpower,"/",intformpower)
        integral = (u,"*",du,"*",dx,"+C")
        #outputs final integral udx
        print(integral)

elif calc == "differentiation":
    typex = input("normal,chain")
    if typex == "normal":
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
    elif typex == "chain":
        y = input("please enter the equation")
        u = input("please enter the value of u, with each var seperated by a ,")
        #splitting values
        uarr = u.split(",")
        uar = np.array([])
        #splitting all x values from u
        for xpos, value in enumerate(uarr):
            if "x" in value:
                uar = np.append(uar,value)
        uarlen = uar.size
        uarinit = 0
        udiff = np.array([])
        #starts du/dx 
        while uarinit < uarlen:
            uval = uar[uarinit]
            #seperating values from x to convert to integers
            uval = uval.split("x")
            #assigning base value
            uvalbase = uval[0]
            #finding power value
            for pos, i in enumerate(uval):
                if "^" in i:
                    pos = pos
            uvalpower = uval[pos]
            #splitting power from ^
            uvalpower = uvalpower.split("^")
            uvalpwrlen = len(uvalpower)
            #assiging power
            uvalpwrlen = uvalpwrlen - 1
            #checking if power is there
            if uvalpwrlen == 0:
                uvalpower = 1
            else:
                uvalpower = uvalpower[uvalpwrlen]
            #coverting strings to integers for calculation
            uvalbase = int(uvalbase)
            uvalpower = int(uvalpower)
            #differential calculation
            ubase = uvalbase*uvalpower
            upower = uvalpower - 1
            #checking if there is a power,if power = 1 then there is a x, if power = 0 then no x, if power > or < 1 then x^power
            if upower == 1:
                #creating symbol based on value
                if ubase > 0:
                    sym = "+"
                elif ubase < 0:
                    sym = "-"
                #converting integers back to strings for simplification
                ubase = str(ubase)
                differential = sym,ubase,"x"
                differential = ''.join(differential)
            elif upower == 0:
                #creating symbol based on value
                if ubase > 0:
                    sym = "+"
                elif ubase < 0:
                    sym = "-"
                #converting integers back to strings for simplification
                ubase = str(ubase)
                differential = sym,ubase
                differential = ''.join(differential)
            elif upower != 1:
                #creating symbol based on value
                if ubase > 0:
                    sym = "+"
                elif ubase < 0:
                    sym = "-"
                if upower > 0:
                    sympwr = "+"
                elif upower < 0:
                    synpwr = "-"
                #converting integers back to strings for simplification
                ubase = str(ubase)
                upower = str(upower)
                differential = sym,ubase,"x^",sympwr,upower
                differential = ''.join(differential)
            #Adding du/dx to array for use
            udiff = np.append(udiff,differential)
            #Restarting loop
            uarinit = uarinit + 1
            if uarinit == uarlen:
                break
        print(udiff)
        #print(equationarr)
        
elif calc == "logs":
    var = int(input("please enter a value"))
    base = int(input("please enter the base value"))
    log = math.log(var,base)
    print(log)
    print("log",base,"^",var)
