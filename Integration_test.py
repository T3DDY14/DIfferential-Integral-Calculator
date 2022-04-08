from fractions import Fraction
import numpy as np
import math
import re

def differential(equationsplit):
    trigfunction = ['sin','cos','tan','sec','cosec','cot']
    sctloclen = len(equationsplit)
    sctinit = 0
    dif = []
    while sctinit < sctloclen:
        var = equationsplit[sctinit] #puting variable from array into a string variable
        #checking if the variable is a trig function or a normal
        if "sin" in var:
            #splitting the variable at the trig function
            varsplit = var.split("sin")
            #replacing the empty variable with the new trig function
            varsplit[0] = "cos"
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            #saving the first variable for use later
            varone = varsplit[0]
            #making the split variable one variable
            varsplit = varsplit[1]
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            #taking the new variable and storing it
            vartwo = varsplit[0]
            #splitting the new variable at x to take the base and power
            vartwo = vartwo.split("x")
            #saving the x variable base
            vartwobase = vartwo[0]
            #making the array one variable again
            vartwo = vartwo[1]
            #splitting the array at ^ to find the power
            vartwo = vartwo.split("^")
            #checking if there is a power present
            vartwolen = len(vartwo)
            #if there is no power then power = 1
            if vartwolen == 1:
                vartwopower = 1
            #otherwise power is the power present
            else:
                vartwopower = vartwo[1]
            #starting the differential
            vartwobase = vartwobase*vartwopower
            vartwopower = vartwopower - 1
            #converting integers back to strings for manipulation
            vartwobase = str(vartwobase)
            #checking if there is still a power and if its its greater than 1 
            if vartwopower > 1:
                vartwopower = str(vartwopower)
                #joining both variables together
                dydx = varone,"(",vartwobase,"x^",vartwopower,")"
                dydx = ''.join(dydx)
                #adding the variable back to inital array
                dif.append(dydx)
            #checking if the power == 1 then there is no need for a power
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")"
                dydx = ''.join(dydx)
                dif.append(dydx)
            #checking if power == 0 then there is no need for a power or x variable
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")"
                dydx = ''.join(dydx)
                dif.append(dydx)
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
            vartwobase = vartwobase*vartwopower
            vartwopower = vartwopower - 1
            vartwobase = str(vartwobase)
            if vartwopower > 1:
                vartwopower = str(vartwopower)
                dydx = varone,"(",vartwobase,"x^",vartwopower,")"
                dydx = ''.join(dydx)
                dif.append(dydx))
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")"
                dydx = ''.join(dydx)
                dif.append(dydx)
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")"
                dydx = ''.join(dydx)
                dif.append(dydx)
            equationsplit[sctinit] = dydx
        if "tan" in var:
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
            vartwobase = vartwobase*vartwopower
            vartwopower = vartwopower - 1
            vartwobase = str(vartwobase)
            if vartwopower > 1:
                vartwopower = str(vartwopower)
                dydx = varone,"(",vartwobase,"x^",vartwopower,")"
                dydx = ''.join(dydx)
                dif.append(dydx))
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")"
                dydx = ''.join(dydx)
                dif.append(dydx)
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")"
                dydx = ''.join(dydx)
                dif.append(dydx)
            equationsplit[sctinit] = dydx
        if "cot" in var:
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
            vartwobase = vartwobase*vartwopower
            vartwopower = vartwopower - 1
            vartwobase = str(vartwobase)
            if vartwopower > 1:
                vartwopower = str(vartwopower)
                dydx = varone,"(",vartwobase,"x^",vartwopower,")"
                dydx = ''.join(dydx)
                dif.append(dydx))
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")"
                dydx = ''.join(dydx)
                dif.append(dydx)
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")"
                dydx = ''.join(dydx)
                dif.append(dydx)
            equationsplit[sctinit] = dydx  
        if "sec" in var:
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
            vartwobase = vartwobase*vartwopower
            vartwopower = vartwopower - 1
            vartwobase = str(vartwobase)
            if vartwopower > 1:
                vartwopower = str(vartwopower)
                dydx = varone[0],"(",vartwobase,"x^",vartwopower,")",varone[1],"(",vartwobase,"x^",vartwopower,")"
                dydx = ''.join(dydx)
                dif.append(dydx))
            elif vartwopower == 1:
                dydx = varone[0],"(",vartwobase,"x",")",varone[1],"(",vartwobase,"x",")"
                dydx = ''.join(dydx)
                dif.append(dydx)
            elif vartwopower == 0:
                dydx = varone[0],"(",vartwobase,")",varone[1],"(",vartwobase,")"
                dydx = ''.join(dydx)
                dif.append(dydx)
            equationsplit[sctinit] = dydx
        if "cosec" in var:
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
            vartwobase = vartwobase*vartwopower
            vartwopower = vartwopower - 1
            vartwobase = str(vartwobase)
            if vartwopower > 1:
                vartwopower = str(vartwopower)
                dydx = varone[0],"(",vartwobase,"x^",vartwopower,")",varone[1],"(",vartwobase,"x^",vartwopower,")"
                dydx = ''.join(dydx)
                dif.append(dydx))
            elif vartwopower == 1:
                dydx = varone[0],"(",vartwobase,"x",")",varone[1],"(",vartwobase,"x",")"
                dydx = ''.join(dydx)
                dif.append(dydx)
            elif vartwopower == 0:
                dydx = varone[0],"(",vartwobase,")",varone[1],"(",vartwobase,")"
                dydx = ''.join(dydx)
                dif.append(dydx)
            equationsplit[sctinit] = dydx
        elif "x" in var:
            varsplit = var.split("x")
            print(varsplit)
            varbase = varsplit[0]
            if "^" in varsplit[1]:
                varsplit = ''.join(varsplit)
                varsplit = varsplit("^")
                varpower = varsplit[1]
            elif "^" not in varsplit[1]:
                varpower = 1
            #dydx
            varbase = varbase*varpower
            varpower = varpower - 1
            varbase = str(varbase)
            if varpower > 1:
                varpower = str(varpower)
                dydx = varone,"x^",varpower
                dydx = ''.join(dydx)
                dif.append(dydx))
            elif varpower == 1:
                dydx = varone,"x"
                dydx = ''.join(dydx)
                dif.append(dydx)
            elif varpower == 0:
                dydx = varone
                dydx = ''.join(dydx)
                dif.append(dydx)
            equationsplit[sctinit] = dydx            
        else:
            print("oops")                    
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
                dif.append(dydx))
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")","+C"
                dydx = ''.join(dydx)
                dif.append(dydx)
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")","+C"
                dydx = ''.join(dydx)
                dif.append(dydx)
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
                dif.append(dydx))
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")","+C"
                dydx = ''.join(dydx)
                dif.append(dydx)
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")","+C"
                dydx = ''.join(dydx)
                dif.append(dydx)
            equationsplit[sctinit] = dydx
        if "tan" in var:
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
                dif.append(dydx))
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")","|","+C"
                dydx = ''.join(dydx)
                dif.append(dydx)
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")","|","+C"
                dydx = ''.join(dydx)
                dif.append(dydx)
            equationsplit[sctinit] = dydx
        if "cot" in var:
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
                dif.append(dydx))
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")","|","+C"
                dydx = ''.join(dydx)
                dif.append(dydx)
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")","|","+C"
                dydx = ''.join(dydx)
                dif.append(dydx)
            equationsplit[sctinit] = dydx  
        if "sec" in var:
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
                dif.append(dydx))
            elif vartwopower == 1:
                dydx = varone[0],"(",vartwobase,"x",")","+",varone[1],"(",vartwobase,"x",")",")","|","+C"
                dydx = ''.join(dydx)
                dif.append(dydx)
            elif vartwopower == 0:
                dydx = varone[0],"(",vartwobase,")","+",varone[1],"(",vartwobase,")",")","|","+C"
                dydx = ''.join(dydx)
                dif.append(dydx)
            equationsplit[sctinit] = dydx
        if "cosec" in var:
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
                dif.append(dydx))
            elif vartwopower == 1:
                dydx = varone[0],"(",vartwobase,"x",")","-",varone[1],"(",vartwobase,"x",")","|","+C"
                dydx = ''.join(dydx)
                dif.append(dydx)
            elif vartwopower == 0:
                dydx = varone[0],"(",vartwobase,")","-",varone[1],"(",vartwobase,")","|","+C"
                dydx = ''.join(dydx)
                dif.append(dydx)
            equationsplit[sctinit] = dydx
        elif "x" in var:
            varsplit = var.split("x")
            print(varsplit)
            varbase = varsplit[0]
            if "^" in varsplit[1]:
                varsplit = ''.join(varsplit)
                varsplit = varsplit("^")
                varpower = varsplit[1]
            elif "^" not in varsplit[1]:
                varpower = 1
            #dydx
            varpower = varpower + 1
            varbase = varbase/varpower      
            varbase = str(varbase)
            if varpower > 1:
                varpower = str(varpower)
                dydx = varone,"x^",varpower
                dydx = ''.join(dydx)
                dif.append(dydx))
            elif varpower == 1:
                dydx = varone,"x"
                dydx = ''.join(dydx)
                dif.append(dydx)
            elif varpower == 0:
                dydx = varone
                dydx = ''.join(dydx)
                dif.append(dydx)
            equationsplit[sctinit] = dydx            
        else:
            print("oops")                    
        sctinit = sctinit + 1
        if sctinit == sctloclen:
            break
def substituion(equationsplit):
def chain(equationsplit):
def quotient(equationsplit):















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
    

print(equationsplit)


