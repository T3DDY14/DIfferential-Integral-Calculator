from fractions import Fraction
import numpy as np
import math
import re

def differential(equationsplit):
    print(equationsplit)
    trigfunction = ['sin','cos','tan','sec','cosec','cot']
    sctloclen = len(equationsplit)
    sctinit = 0
    dif = []
    while sctinit < sctloclen:
        var = equationsplit[sctinit] #puting variable from array into a string variable
        print(var)
        #checking if the variable is a trig function or a normal
        if "sin" in var:
            #splitting the variable at the trig function
            varsplit = var.split("sin")
            print(varsplit)
            #replacing the empty variable with the new trig function
            varsplit[0] = "cos"            
            #joining the array back together for another split
            varwhole = "".join(varsplit)           
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            print(varsplit)
            #saving the first variable for use later
            varone = varsplit[0]          
            #making the split variable one variable
            varsplit = varsplit[1]          
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            print(varsplit)
            #taking the new variable and storing it
            vartwo = varsplit[0]           
            vartwo = re.split('([y])',vartwo)
            print(vartwo)
            vartwolen = len(vartwo)
            print(vartwolen,"vartwolen")
            vartwoinit = 0
            while vartwoinit < vartwolen:
                print(vartwoinit,"vartwoinit")
                varthree = vartwo[vartwoinit]
                print(varthree,"varthree")
                print(vartwo,"newvartwo")
                if varthree == "y":
                    vartwo[vartwoinit] = "+"

                elif varthree == "u":
                    vartwo[vartwoinit] = "-"

                else:
                    #splitting the new variable at x to take the base and power
                    varthree = vartwo[vartwoinit]
                    vartwox = varthree.split("x")
                    print(vartwox)
                    #saving the x variable base
                    vartwobase = vartwox[0]
                    print(vartwobase)
                    #making the array one variable again
                    vartwox = vartwox[1]
                    print(vartwox)
                    #splitting the array at ^ to find the power
                    vartwox = vartwox.split("^")
                    print(vartwox)
                    #checking if there is a power present
                    vartwoxlen = len(vartwox)
                     #if there is no power then power = 1
                    if vartwolen == 1:
                        vartwopower = 1
                    #otherwise power is the power present
                    else:
                        vartwopower = vartwox[1]
                    #starting the differential
                    vartwobase = int(vartwobase)
                    vartwopower = int(vartwopower)
                    vartwobase = vartwobase*vartwopower
                    vartwopower = vartwopower - 1
                    #converting integers back to strings for manipulation
                    vartwobase = str(vartwobase)
                    #checking if there is still a power and if its its greater than 1 
                    if vartwopower > 1:
                        #joining both variables together
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase,"x^",vartwopower
                        vartwoactual = ''.join(vartwoactual)
                        vartwo[vartwoinit] = vartwoactual
                    #checking if the power == 1 then there is no need for a powe
                    elif vartwopower == 1:
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase,"x"
                        vartwoactual = ''.join(vartwoactual)
                        vartwo[vartwoinit] = vartwoactual
                    #checking if power == 0 then there is no need for a power or x variable
                    elif vartwopower == 0:
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase
                        vartwo[vartwoinit] = vartwoactual
                if vartwoinit == vartwolen:
                    break
            vartwo = ''.join(vartwo)
            dydx = varone,"(",vartwo,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx                     
        elif "cos" in var:
            varsplit = var.split("cos")
            print(varsplit)
            varsplit[0] = "-sin"
            varwhole = "".join(varsplit)
            varsplit = varwhole.split("(")
            print(varsplit)
            varone = varsplit[0]
            varsplit = varsplit[1]
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = varsplit[0]
            print(vartwo)
            vartwo = re.split('([+-])',vartwo)
            vartwolen = len(vartwolen)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                varthree = vartwo[vartwoinit]
                if varthree == "+":
                    vartwo[vartwoinit] = varthree
                elif varthree == "-":
                    vartwo[vartwoinit] = varthree
                else:
                    #splitting the new variable at x to take the base and power
                    vartwox = vartwo.split("x")
                    print(vartwox)
                    #saving the x variable base
                    vartwobase = vartwox[0]
                    print(vartwobase)
                    #making the array one variable again
                    vartwox = vartwox[1]
                    print(vartwox)
                    #splitting the array at ^ to find the power
                    vartwox = vartwox.split("^")
                    print(vartwox)
                    #checking if there is a power present
                    vartwoxlen = len(vartwox)
                     #if there is no power then power = 1
                    if vartwolen == 1:
                        vartwopower = 1
                    #otherwise power is the power present
                    else:
                        vartwopower = vartwox[1]
                    #starting the differential
                    vartwobase = int(vartwobase)
                    vartwopower = int(vartwopower)
                    vartwobase = vartwobase*vartwopower
                    vartwopower = vartwopower - 1
                    #converting integers back to strings for manipulation
                    vartwobase = str(vartwobase)
                    #checking if there is still a power and if its its greater than 1 
                    if vartwopower > 1:
                        #joining both variables together
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase,"x^",vartwopower
                        vartwoactual = ''.join(vartwoactual)
                        vartwo[vartwoinit] = vartwoactual
                    #checking if the power == 1 then there is no need for a powe
                    elif vartwopower == 1:
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase,"x"
                        vartwoactual = ''.join(vartwoactual)
                        vartwo[vartwoinit] = vartwoactual
                    #checking if power == 0 then there is no need for a power or x variable
                    elif vartwopower == 0:
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase
                        vartwo[vartwoinit] = vartwoactual                   
                vartwoinit = vartwoinit + 1
            vartwo = ''.join(vartwo)
            dydx = varone,"(",vartwo,")"
            equationsplit[sctinit] = dydx
        elif "tan" in var:
            varsplit = var.split("tan")
            print(varsplit)
            varsplit[0] = "sec^2"
            varwhole = "".join(varsplit)
            varsplit = varwhole.split("(")
            print(varsplit)
            varone = varsplit[0]
            varsplit = varsplit[1]
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = varsplit[0]
            print(vartwo)
            vartwo = re.split('([+-])',vartwo)
            vartwolen = len(vartwolen)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                varthree = vartwo[vartwoinit]
                if varthree == "+":
                    vartwo[vartwoinit] = varthree
                elif varthree == "-":
                    vartwo[vartwoinit] = varthree
                else:
                    #splitting the new variable at x to take the base and power
                    vartwox = vartwo.split("x")
                    print(vartwox)
                    #saving the x variable base
                    vartwobase = vartwox[0]
                    print(vartwobase)
                    #making the array one variable again
                    vartwox = vartwox[1]
                    print(vartwox)
                    #splitting the array at ^ to find the power
                    vartwox = vartwox.split("^")
                    print(vartwox)
                    #checking if there is a power present
                    vartwoxlen = len(vartwox)
                     #if there is no power then power = 1
                    if vartwolen == 1:
                        vartwopower = 1
                    #otherwise power is the power present
                    else:
                        vartwopower = vartwox[1]
                    #starting the differential
                    vartwobase = int(vartwobase)
                    vartwopower = int(vartwopower)
                    vartwobase = vartwobase*vartwopower
                    vartwopower = vartwopower - 1
                    #converting integers back to strings for manipulation
                    vartwobase = str(vartwobase)
                    #checking if there is still a power and if its its greater than 1 
                    if vartwopower > 1:
                        #joining both variables together
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase,"x^",vartwopower
                        vartwoactual = ''.join(vartwoactual)
                        vartwo[vartwoinit] = vartwoactual
                    #checking if the power == 1 then there is no need for a powe
                    elif vartwopower == 1:
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase,"x"
                        vartwoactual = ''.join(vartwoactual)
                        vartwo[vartwoinit] = vartwoactual
                    #checking if power == 0 then there is no need for a power or x variable
                    elif vartwopower == 0:
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase
                        vartwo[vartwoinit] = vartwoactual                   
                vartwoinit = vartwoinit + 1
            vartwo = ''.join(vartwo)
            dydx = varone,"(",vartwo,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
        elif "cot" in var:
            varsplit = var.split("cot")
            print(varsplit)
            varsplit[0] = "-cosec^2"
            varwhole = "".join(varsplit)
            varsplit = varwhole.split("(")
            print(varsplit)
            varone = varsplit[0]
            varsplit = varsplit[1]
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = varsplit[0]
            print(vartwo)
            vartwo = re.split('([+-])',vartwo)
            vartwolen = len(vartwolen)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                varthree = vartwo[vartwoinit]
                if varthree == "+":
                    vartwo[vartwoinit] = varthree
                elif varthree == "-":
                    vartwo[vartwoinit] = varthree
                else:
                    #splitting the new variable at x to take the base and power
                    vartwox = vartwo.split("x")
                    print(vartwox)
                    #saving the x variable base
                    vartwobase = vartwox[0]
                    print(vartwobase)
                    #making the array one variable again
                    vartwox = vartwox[1]
                    print(vartwox)
                    #splitting the array at ^ to find the power
                    vartwox = vartwox.split("^")
                    print(vartwox)
                    #checking if there is a power present
                    vartwoxlen = len(vartwox)
                     #if there is no power then power = 1
                    if vartwolen == 1:
                        vartwopower = 1
                    #otherwise power is the power present
                    else:
                        vartwopower = vartwox[1]
                    #starting the differential
                    vartwobase = int(vartwobase)
                    vartwopower = int(vartwopower)
                    vartwobase = vartwobase*vartwopower
                    vartwopower = vartwopower - 1
                    #converting integers back to strings for manipulation
                    vartwobase = str(vartwobase)
                    #checking if there is still a power and if its its greater than 1 
                    if vartwopower > 1:
                        #joining both variables together
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase,"x^",vartwopower
                        vartwoactual = ''.join(vartwoactual)
                        vartwo[vartwoinit] = vartwoactual
                    #checking if the power == 1 then there is no need for a powe
                    elif vartwopower == 1:
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase,"x"
                        vartwoactual = ''.join(vartwoactual)
                        vartwo[vartwoinit] = vartwoactual
                    #checking if power == 0 then there is no need for a power or x variable
                    elif vartwopower == 0:
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase
                        vartwo[vartwoinit] = vartwoactual                   
                vartwoinit = vartwoinit + 1
            vartwo = ''.join(vartwo)
            dydx = varone,"(",vartwo,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx 
        elif "sec" in var:
            varsplit = var.split("sec")
            print(varsplit)
            varsplit[0] = "sec,tan"
            varwhole = "".join(varsplit)
            varsplit = varwhole.split("(")
            print(varsplit)
            varone = varsplit[0]
            varone = varone.split(",")
            varsplit = varsplit[1]
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = varsplit[0]
            print(vartwo)
            vartwo = re.split('([+-])',vartwo)
            vartwolen = len(vartwolen)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                varthree = vartwo[vartwoinit]
                if varthree == "+":
                    vartwo[vartwoinit] = varthree
                elif varthree == "-":
                    vartwo[vartwoinit] = varthree
                else:
                    #splitting the new variable at x to take the base and power
                    vartwox = vartwo.split("x")
                    print(vartwox)
                    #saving the x variable base
                    vartwobase = vartwox[0]
                    print(vartwobase)
                    #making the array one variable again
                    vartwox = vartwox[1]
                    print(vartwox)
                    #splitting the array at ^ to find the power
                    vartwox = vartwox.split("^")
                    print(vartwox)
                    #checking if there is a power present
                    vartwoxlen = len(vartwox)
                     #if there is no power then power = 1
                    if vartwolen == 1:
                        vartwopower = 1
                    #otherwise power is the power present
                    else:
                        vartwopower = vartwox[1]
                    #starting the differential
                    vartwobase = int(vartwobase)
                    vartwopower = int(vartwopower)
                    vartwobase = vartwobase*vartwopower
                    vartwopower = vartwopower - 1
                    #converting integers back to strings for manipulation
                    vartwobase = str(vartwobase)
                    #checking if there is still a power and if its its greater than 1 
                    if vartwopower > 1:
                        #joining both variables together
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase,"x^",vartwopower
                        vartwoactual = ''.join(vartwoactual)
                        vartwo[vartwoinit] = vartwoactual
                    #checking if the power == 1 then there is no need for a powe
                    elif vartwopower == 1:
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase,"x"
                        vartwoactual = ''.join(vartwoactual)
                        vartwo[vartwoinit] = vartwoactual
                    #checking if power == 0 then there is no need for a power or x variable
                    elif vartwopower == 0:
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase
                        vartwo[vartwoinit] = vartwoactual                   
                vartwoinit = vartwoinit + 1
            vartwo = ''.join(vartwo)
            dydx = varone[0],"(",vartwo,")",varone[1],"(",vartwo,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx           
        elif "cosec" in var:
            varsplit = var.split("cosec")
            print(varsplit)
            varsplit[0] = "-cosec,cot"
            varwhole = "".join(varsplit)
            varsplit = varwhole.split("(")
            print(varsplit)
            varone = varsplit[0]
            varone = varone.split(",")
            varsplit = varsplit[1]
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = varsplit[0]
            print(vartwo)
            vartwo = re.split('([+-])',vartwo)
            vartwolen = len(vartwolen)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                varthree = vartwo[vartwoinit]
                if varthree == "+":
                    vartwo[vartwoinit] = varthree
                elif varthree == "-":
                    vartwo[vartwoinit] = varthree
                else:
                    #splitting the new variable at x to take the base and power
                    vartwox = vartwo.split("x")
                    print(vartwox)
                    #saving the x variable base
                    vartwobase = vartwox[0]
                    print(vartwobase)
                    #making the array one variable again
                    vartwox = vartwox[1]
                    print(vartwox)
                    #splitting the array at ^ to find the power
                    vartwox = vartwox.split("^")
                    print(vartwox)
                    #checking if there is a power present
                    vartwoxlen = len(vartwox)
                     #if there is no power then power = 1
                    if vartwolen == 1:
                        vartwopower = 1
                    #otherwise power is the power present
                    else:
                        vartwopower = vartwox[1]
                    #starting the differential
                    vartwobase = int(vartwobase)
                    vartwopower = int(vartwopower)
                    vartwobase = vartwobase*vartwopower
                    vartwopower = vartwopower - 1
                    #converting integers back to strings for manipulation
                    vartwobase = str(vartwobase)
                    #checking if there is still a power and if its its greater than 1 
                    if vartwopower > 1:
                        #joining both variables together
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase,"x^",vartwopower
                        vartwoactual = ''.join(vartwoactual)
                        vartwo[vartwoinit] = vartwoactual
                    #checking if the power == 1 then there is no need for a powe
                    elif vartwopower == 1:
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase,"x"
                        vartwoactual = ''.join(vartwoactual)
                        vartwo[vartwoinit] = vartwoactual
                    #checking if power == 0 then there is no need for a power or x variable
                    elif vartwopower == 0:
                        vartwopower = str(vartwopower)
                        vartwoactual = vartwobase
                        vartwo[vartwoinit] = vartwoactual                   
                vartwoinit = vartwoinit + 1
            vartwo = ''.join(vartwo)
            dydx = varone[0],"(",vartwo,")",varone[1],"(",vartwo,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx                            
        sctinit = sctinit + 1
        if sctinit == sctloclen:
            break
def integral(equationsplit):
    trigfunction = ['sin','cos','tan','sec','cosec','cot']
    sctloclen = len(equationsplit)
    sctinit = 0
    dif = []
    while sctinit < sctloclen:
        var = equationsplit[sctinit]
        if "sin" in var:
            varsplit = var.split("sin")
            print(varsplit)
            varsplit[0] = "-cos"
            varwhole = "".join(varsplit)
            varsplit = varwhole.split("(")
            print(varsplit)
            varone = varsplit[0]
            varsplit = varsplit[1]
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = varsplit[0]
            vartwo = vartwo.split("x")
            vartwobase = vartwo[0]
            vartwo = vartwo[1]
            vartwo = vartwo.split("^")
            vartwolen = len(vartwo)
            if vartwolen == 1:
                vartwopower = 1
            else:
                vartwopower = vartwo[1]
            #dydx
            vartwopower = vartwopower + 1
            vartwobase = vartwobase/vartwopower
            vartwobase = str(vartwobase)
            if vartwopower > 1:
                vartwopower = str(vartwopower)
                dydx = varone,"(",vartwobase,"x^",vartwopower,")","+C"
                dydx = ''.join(dydx)                
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")","+C"
                dydx = ''.join(dydx)               
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")","+C"
                dydx = ''.join(dydx)               
            equationsplit[sctinit] = dydx
        elif "cos" in var:
            varsplit = var.split("cos")
            print(varsplit)
            varsplit[0] = "sin"
            varwhole = "".join(varsplit)
            varsplit = varwhole.split("(")
            print(varsplit)
            varone = varsplit[0]
            varsplit = varsplit[1]
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = varsplit[0]
            vartwo = vartwo.split("x")
            vartwobase = vartwo[0]
            vartwo = vartwo[1]
            vartwo = vartwo.split("^")
            vartwolen = len(vartwo)
            if vartwolen == 1:
                vartwopower = 1
            else:
                vartwopower = vartwo[1]
            #dydx
            vartwopower = vartwopower + 1
            vartwobase = vartwobase/vartwopower
            vartwobase = str(vartwobase)
            if vartwopower > 1:
                vartwopower = str(vartwopower)
                dydx = varone,"(",vartwobase,"x^",vartwopower,")","+C"
                dydx = ''.join(dydx)               
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")","+C"
                dydx = ''.join(dydx)               
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")","+C"
                dydx = ''.join(dydx)               
            equationsplit[sctinit] = dydx
        elif "tan" in var:
            varsplit = var.split("tan")
            print(varsplit)
            varsplit[0] = "-ln|sec"
            varwhole = "".join(varsplit)
            varsplit = varwhole.split("(")
            print(varsplit)
            varone = varsplit[0]
            varsplit = varsplit[1]
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = varsplit[0]
            vartwo = vartwo.split("x")
            vartwobase = vartwo[0]
            vartwo = vartwo[1]
            vartwo = vartwo.split("^")
            vartwolen = len(vartwo)
            if vartwolen == 1:
                vartwopower = 1
            else:
                vartwopower = vartwo[1]
            #dydx
            vartwopower = vartwopower + 1
            vartwobase = vartwobase/vartwopower
            vartwobase = str(vartwobase)
            if vartwopower > 1:
                vartwopower = str(vartwopower)
                dydx = varone,"(",vartwobase,"x^",vartwopower,")","|","+C"
                dydx = ''.join(dydx)                
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")","|","+C"
                dydx = ''.join(dydx)               
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")","|","+C"
                dydx = ''.join(dydx)                
            equationsplit[sctinit] = dydx
        elif "cot" in var:
            varsplit = var.split("cot")
            print(varsplit)
            varsplit[0] = "ln|sin"
            varwhole = "".join(varsplit)
            varsplit = varwhole.split("(")
            print(varsplit)
            varone = varsplit[0]
            varsplit = varsplit[1]
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = varsplit[0]
            vartwo = vartwo.split("x")
            vartwobase = vartwo[0]
            vartwo = vartwo[1]
            vartwo = vartwo.split("^")
            vartwolen = len(vartwo)
            if vartwolen == 1:
                vartwopower = 1
            else:
                vartwopower = vartwo[1]
            #dydx
            vartwopower = vartwopower + 1
            vartwobase = vartwobase/vartwopower
            vartwobase = str(vartwobase)
            if vartwopower > 1:
                vartwopower = str(vartwopower)
                dydx = varone,"(",vartwobase,"x^",vartwopower,")","|","+C"
                dydx = ''.join(dydx)                
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")","|","+C"
                dydx = ''.join(dydx)                
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")","|","+C"
                dydx = ''.join(dydx)               
            equationsplit[sctinit] = dydx  
        elif "sec" in var:
            varsplit = var.split("sec")
            print(varsplit)
            varsplit[0] = "ln|sec,tan"
            varwhole = "".join(varsplit)
            varsplit = varwhole.split("(")
            print(varsplit)
            varone = varsplit[0]
            varone = varone.split(",")
            varsplit = varsplit[1]
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = varsplit[0]
            vartwo = vartwo.split("x")
            vartwobase = vartwo[0]
            vartwo = vartwo[1]
            vartwo = vartwo.split("^")
            vartwolen = len(vartwo)
            if vartwolen == 1:
                vartwopower = 1
            else:
                vartwopower = vartwo[1]
            #dydx
            vartwopower = vartwopower + 1
            vartwobase = vartwobase/vartwopower
            vartwobase = str(vartwobase)
            if vartwopower > 1:
                vartwopower = str(vartwopower)
                dydx = varone[0],"(",vartwobase,"x^",vartwopower,")","+",varone[1],"(",vartwobase,"x^",vartwopower,")",")","|","+C"
                dydx = ''.join(dydx)                
            elif vartwopower == 1:
                dydx = varone[0],"(",vartwobase,"x",")","+",varone[1],"(",vartwobase,"x",")",")","|","+C"
                dydx = ''.join(dydx)               
            elif vartwopower == 0:
                dydx = varone[0],"(",vartwobase,")","+",varone[1],"(",vartwobase,")",")","|","+C"
                dydx = ''.join(dydx)              
            equationsplit[sctinit] = dydx
        elif "cosec" in var:
            varsplit = var.split("cosec")
            print(varsplit)
            varsplit[0] = "ln|cosec,-cot"
            varwhole = "".join(varsplit)
            varsplit = varwhole.split("(")
            print(varsplit)
            varone = varsplit[0]
            varone = varone.split(",")
            varsplit = varsplit[1]
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = varsplit[0]
            vartwo = vartwo.split("x")
            vartwobase = vartwo[0]
            vartwo = vartwo[1]
            vartwo = vartwo.split("^")
            vartwolen = len(vartwo)
            if vartwolen == 1:
                vartwopower = 1
            else:
                vartwopower = vartwo[1]
            #dydx
            vartwopower = vartwopower + 1
            vartwobase = vartwobase/vartwopower
            vartwobase = str(vartwobase)
            if vartwopower > 1:
                vartwopower = str(vartwopower)
                dydx = varone[0],"(",vartwobase,"x^",vartwopower,")","-",varone[1],"(",vartwobase,"x^",vartwopower,")","|","+C"
                dydx = ''.join(dydx)              
            elif vartwopower == 1:
                dydx = varone[0],"(",vartwobase,"x",")","-",varone[1],"(",vartwobase,"x",")","|","+C"
                dydx = ''.join(dydx)     
            elif vartwopower == 0:
                dydx = varone[0],"(",vartwobase,")","-",varone[1],"(",vartwobase,")","|","+C"
                dydx = ''.join(dydx)         
            equationsplit[sctinit] = dydx
        else:# elif"x" in var
            if var == "+":
                equationsplit[sctinit] = var
            elif var == "-":
                equationsplit[sctinit] = var
            else:
                varsplit = var.split("x")
                print(varsplit)
                varbase = varsplit[0]
                if "^" in varsplit[1]:
                    varsplit = ''.join(varsplit)
                    varsplit = var.split("^")
                    varpower = varsplit[1]
                elif "^" not in varsplit[1]:
                    varpower = 1
                #dydx
                varbase = int(varbase)
                varpower = int(varpower)
                varpower = varpower + 1
                varbase = varbase/varpower               
                varbase = str(varbase)
                if varpower > 1:
                    varpower = str(varpower)
                    dydx = varbase,"x^",varpower
                    dydx = ''.join(dydx)                
                elif varpower == 1:
                    dydx = varbase,"x"
                    dydx = ''.join(dydx)              
                elif varpower == 0:
                    dydx = varbase
                    dydx = ''.join(dydx)               
                equationsplit[sctinit] = dydx                                       
        sctinit = sctinit + 1        
        if sctinit == sctloclen:
            break
            
#def substituion(equationsplit):
#def chain(equationsplit):
#def quotient(equationsplit):


choice = input("differential,integral")           
equation = input("please enter the equation")
equationsplit = re.split('([+-])',equation)
if choice == "differential":
    secondarychoice = input("normal,chain,quotient")
    if secondarychoice == "normal":
        differential(equationsplit)
    elif secondarychoice == "chain":
        chain(equationsplit)
    elif secondarychoice == "quotient":
        quotient(equationsplit)
elif choice == "integral":
    integral(equationsplit)
    

print(equation," == ",equationsplit)


