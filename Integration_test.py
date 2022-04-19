from fractions import Fraction
import numpy as np
import math
import re

def differential(equationsplit): # done
    trigfunction = ['sin','cos','tan','sec','cosec','cot']
    sctloclen = len(equationsplit)
    sctinit = 0
    dif = []
    while sctinit < sctloclen:
        var = equationsplit[sctinit] #puting variable from array into a string variable
        print(var,"var")
        #checking if the variable is a trig function or a normal
        if "sin" in var:
            #splitting the variable at the trig function
            varsplit = var.split("sin")
            print(varsplit)
            #replacing the empty variable with the new trig function
            varsplit[0] = "cos"
            varone = varsplit[0]
            print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            print(varsplit)
            #saving the first variable for use later
            varone = varsplit[0]
            print(varone)
            #making the split variable one variable
            varsplit = varsplit[1]
            print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = ''.join(varsplit)
            print(vartwo)
            vartwo = re.split('([y|u])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo)
            vartwolen = len(vartwo)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                workingvar = vartwo[vartwoinit]
                print(workingvar,"workingvar")
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    print(powerlen,"powerlen")
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    print(base,"base")
                    print(power,"power")
                    base = int(base)
                    power = int(power)
                    base = base*power
                    power = power - 1
                    if power == 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x"
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power == 0:
                        base = str(base)
                        xvar = base
                        vartwo[vartwoinit] = xvar
                    elif power > 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power < 0:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar                   
                    vartwoinit += 1
                    if vartwoinit == vartwolen:
                        break
            vartwo = ''.join(vartwo)   
            dydx = varone,"(",vartwo,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
            print(vartwo)   
        elif "cos" in var:
            #splitting the variable at the trig function
            varsplit = var.split("cos")
            print(varsplit)
            #replacing the empty variable with the new trig function
            varsplit[0] = "-sin"
            varone = varsplit[0]
            print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            print(varsplit)
            #saving the first variable for use later
            varone = varsplit[0]
            print(varone)
            #making the split variable one variable
            varsplit = varsplit[1]
            print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = ''.join(varsplit)
            print(vartwo)
            vartwo = re.split('([y|u])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo)
            vartwolen = len(vartwo)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                workingvar = vartwo[vartwoinit]
                print(workingvar,"workingvar")
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    print(powerlen,"powerlen")
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    print(base,"base")
                    print(power,"power")
                    base = int(base)
                    power = int(power)
                    base = base*power
                    power = power - 1
                    if power == 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x"
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power == 0:
                        base = str(base)
                        xvar = base
                        vartwo[vartwoinit] = xvar
                    elif power > 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power < 0:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar                   
                    vartwoinit += 1
                    if vartwoinit == vartwolen:
                        break
            vartwo = ''.join(vartwo)   
            dydx = varone,"(",vartwo,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
            print(vartwo)  
        elif "tan" in var:
            #splitting the variable at the trig function
            varsplit = var.split("tan")
            print(varsplit)
            #replacing the empty variable with the new trig function
            varsplit[0] = "sec^2"
            varone = varsplit[0]
            print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            print(varsplit)
            #saving the first variable for use later
            varone = varsplit[0]
            print(varone)
            #making the split variable one variable
            varsplit = varsplit[1]
            print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = ''.join(varsplit)
            print(vartwo)
            vartwo = re.split('([y|u])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo)
            vartwolen = len(vartwo)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                workingvar = vartwo[vartwoinit]
                print(workingvar,"workingvar")
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    print(powerlen,"powerlen")
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    print(base,"base")
                    print(power,"power")
                    base = int(base)
                    power = int(power)
                    base = base*power
                    power = power - 1
                    if power == 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x"
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power == 0:
                        base = str(base)
                        xvar = base
                        vartwo[vartwoinit] = xvar
                    elif power > 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power < 0:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar                   
                    vartwoinit += 1
                    if vartwoinit == vartwolen:
                        break
            vartwo = ''.join(vartwo)   
            dydx = varone,"(",vartwo,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
            print(vartwo)
        elif "cot" in var:
            #splitting the variable at the trig function
            varsplit = var.split("cot")
            print(varsplit)
            #replacing the empty variable with the new trig function
            varsplit[0] = "ln|sin"
            varone = varsplit[0]
            print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            print(varsplit)
            #saving the first variable for use later
            varone = varsplit[0]
            print(varone)
            #making the split variable one variable
            varsplit = varsplit[1]
            print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = ''.join(varsplit)
            print(vartwo)
            vartwo = re.split('([y|u])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo)
            vartwolen = len(vartwo)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                workingvar = vartwo[vartwoinit]
                print(workingvar,"workingvar")
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    print(powerlen,"powerlen")
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    print(base,"base")
                    print(power,"power")
                    base = int(base)
                    power = int(power)
                    base = base*power
                    power = power - 1
                    if power == 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x"
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power == 0:
                        base = str(base)
                        xvar = base
                        vartwo[vartwoinit] = xvar
                    elif power > 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power < 0:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar                   
                    vartwoinit += 1
                    if vartwoinit == vartwolen:
                        break
            vartwo = ''.join(vartwo)   
            dydx = varone,"(",vartwo,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
            print(vartwo)            
        elif "sec" in var:
            #splitting the variable at the trig function
            varsplit = var.split("sec")
            print(varsplit)
            #replacing the empty variable with the new trig function
            varsplit[0] = "sec,tan"
            varone = varsplit[0]
            varone = varone.split(",")
            print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            print(varsplit)
            #saving the first variable for use later
            varone = varsplit[0]
            print(varone)
            #making the split variable one variable
            varsplit = varsplit[1]
            print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = ''.join(varsplit)
            print(vartwo)
            vartwo = re.split('([y|u])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo)
            vartwolen = len(vartwo)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                workingvar = vartwo[vartwoinit]
                print(workingvar,"workingvar")
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    print(powerlen,"powerlen")
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    print(base,"base")
                    print(power,"power")
                    base = int(base)
                    power = int(power)
                    base = base*power
                    power = power - 1
                    if power == 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x"
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power == 0:
                        base = str(base)
                        xvar = base
                        vartwo[vartwoinit] = xvar
                    elif power > 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power < 0:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar                   
                    vartwoinit += 1
                    if vartwoinit == vartwolen:
                        break
            vartwo = ''.join(vartwo)   
            dydx = varone[0],"(",vartwo,")",varone[1],"(",vartwo,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
            print(vartwo)  
        elif "cosec" in var:
            #splitting the variable at the trig function
            varsplit = var.split("cosec")
            print(varsplit)
            #replacing the empty variable with the new trig function
            varsplit[0] = "-cosec,cot"
            varone = varsplit[0]
            varone = varone.split(",")
            print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            print(varsplit)
            #saving the first variable for use later
            varone = varsplit[0]
            print(varone)
            #making the split variable one variable
            varsplit = varsplit[1]
            print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = ''.join(varsplit)
            print(vartwo)
            vartwo = re.split('([y|u])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo)
            vartwolen = len(vartwo)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                workingvar = vartwo[vartwoinit]
                print(workingvar,"workingvar")
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    print(powerlen,"powerlen")
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    print(base,"base")
                    print(power,"power")
                    base = int(base)
                    power = int(power)
                    base = base*power
                    power = power - 1
                    if power == 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x"
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power == 0:
                        base = str(base)
                        xvar = base
                        vartwo[vartwoinit] = xvar
                    elif power > 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power < 0:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar                   
                    vartwoinit += 1
                    if vartwoinit == vartwolen:
                        break
            vartwo = ''.join(vartwo)   
            dydx = varone[0],"(",vartwo,")",varone[1],"(",vartwo,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
            print(vartwo)
        elif "x" in var:
            ##print("doing x var")
            varsplit = var.split("x")
            ##print(varsplit)
            varbase = varsplit[0]
            ##print(varbase,"varbase")
            if "^" in varsplit[1]:
                varsplit = ''.join(varsplit)
                varsplit = varsplit.split("^")
                varpower = varsplit[1]
                ##print(varpower,"varpower")
            elif "^" not in varsplit[1]:
                varpower = 1
            #dydx
            varbase = int(varbase)
            varpower = int(varpower)
            varbase = varbase*varpower
            varpower = varpower - 1
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
def integral(equationsplit): # done
    trigfunction = ['sin','cos','tan','sec','cosec','cot']
    sctloclen = len(equationsplit)
    sctinit = 0
    dif = []
    while sctinit < sctloclen:
        var = equationsplit[sctinit] #puting variable from array into a string variable
        print(var,"var")
        #checking if the variable is a trig function or a normal
        if "sin" in var:
            #splitting the variable at the trig function
            varsplit = var.split("sin")
            print(varsplit)
            #replacing the empty variable with the new trig function
            varsplit[0] = "-cos"
            varone = varsplit[0]
            print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            print(varsplit)
            #saving the first variable for use later
            varone = varsplit[0]
            print(varone)
            #making the split variable one variable
            varsplit = varsplit[1]
            print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = ''.join(varsplit)
            print(vartwo)
            vartwo = re.split('([y|u])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo)
            vartwolen = len(vartwo)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                workingvar = vartwo[vartwoinit]
                print(workingvar,"workingvar")
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    print(powerlen,"powerlen")
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    print(base,"base")
                    print(power,"power")
                    base = int(base)
                    power = int(power)
                    power = power + 1
                    base = base/power
                    
                    if power == 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x"
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power == 0:
                        base = str(base)
                        xvar = base
                        vartwo[vartwoinit] = xvar
                    elif power > 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power < 0:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar                   
                    vartwoinit += 1
                    if vartwoinit == vartwolen:
                        break
            vartwo = ''.join(vartwo)   
            dydx = varone,"(",vartwo,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
            print(vartwo)   
        elif "cos" in var:
            #splitting the variable at the trig function
            varsplit = var.split("cos")
            print(varsplit)
            #replacing the empty variable with the new trig function
            varsplit[0] = "sin"
            varone = varsplit[0]
            print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            print(varsplit)
            #saving the first variable for use later
            varone = varsplit[0]
            print(varone)
            #making the split variable one variable
            varsplit = varsplit[1]
            print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = ''.join(varsplit)
            print(vartwo)
            vartwo = re.split('([y|u])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo)
            vartwolen = len(vartwo)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                workingvar = vartwo[vartwoinit]
                print(workingvar,"workingvar")
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    print(powerlen,"powerlen")
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    print(base,"base")
                    print(power,"power")
                    base = int(base)
                    power = int(power)
                    power = power + 1
                    base = base/power
                    if power == 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x"
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power == 0:
                        base = str(base)
                        xvar = base
                        vartwo[vartwoinit] = xvar
                    elif power > 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power < 0:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar                   
                    vartwoinit += 1
                    if vartwoinit == vartwolen:
                        break
            vartwo = ''.join(vartwo)   
            dydx = varone,"(",vartwo,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
            print(vartwo)  
        elif "tan" in var:
            #splitting the variable at the trig function
            varsplit = var.split("tan")
            print(varsplit)
            #replacing the empty variable with the new trig function
            varsplit[0] = "-ln|cos"
            varone = varsplit[0]
            print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            print(varsplit)
            #saving the first variable for use later
            varone = varsplit[0]
            print(varone)
            #making the split variable one variable
            varsplit = varsplit[1]
            print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = ''.join(varsplit)
            print(vartwo)
            vartwo = re.split('([y|u])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo)
            vartwolen = len(vartwo)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                workingvar = vartwo[vartwoinit]
                print(workingvar,"workingvar")
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    print(powerlen,"powerlen")
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    print(base,"base")
                    print(power,"power")
                    base = int(base)
                    power = int(power)
                    power = power + 1
                    base = base/power
                    if power == 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x"
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power == 0:
                        base = str(base)
                        xvar = base
                        vartwo[vartwoinit] = xvar
                    elif power > 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power < 0:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar                   
                    vartwoinit += 1
                    if vartwoinit == vartwolen:
                        break
            vartwo = ''.join(vartwo)   
            dydx = varone,"(",vartwo,")","|"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
            print(vartwo)
        elif "cot" in var:
            #splitting the variable at the trig function
            varsplit = var.split("cot")
            print(varsplit)
            #replacing the empty variable with the new trig function
            varsplit[0] = "ln|sin"
            varone = varsplit[0]
            print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            print(varsplit)
            #saving the first variable for use later
            varone = varsplit[0]
            print(varone)
            #making the split variable one variable
            varsplit = varsplit[1]
            print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = ''.join(varsplit)
            print(vartwo)
            vartwo = re.split('([y|u])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo)
            vartwolen = len(vartwo)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                workingvar = vartwo[vartwoinit]
                print(workingvar,"workingvar")
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    print(powerlen,"powerlen")
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    print(base,"base")
                    print(power,"power")
                    base = int(base)
                    power = int(power)
                    power = power + 1
                    base = base/power
                    if power == 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x"
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power == 0:
                        base = str(base)
                        xvar = base
                        vartwo[vartwoinit] = xvar
                    elif power > 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power < 0:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar                   
                    vartwoinit += 1
                    if vartwoinit == vartwolen:
                        break
            vartwo = ''.join(vartwo)   
            dydx = varone,"(",vartwo,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
            print(vartwo)            
        elif "sec" in var:
            #splitting the variable at the trig function
            varsplit = var.split("sec")
            print(varsplit)
            #replacing the empty variable with the new trig function
            varsplit[0] = "ln|sec,tan"
            varone = varsplit[0]
            varone = varone.split(",")
            print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            print(varsplit)
            #saving the first variable for use later
            varone = varsplit[0]
            print(varone)
            #making the split variable one variable
            varsplit = varsplit[1]
            print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = ''.join(varsplit)
            print(vartwo)
            vartwo = re.split('([y|u])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo)
            vartwolen = len(vartwo)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                workingvar = vartwo[vartwoinit]
                print(workingvar,"workingvar")
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    print(powerlen,"powerlen")
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    print(base,"base")
                    print(power,"power")
                    base = int(base)
                    power = int(power)
                    power = power + 1
                    base = base/power
                    if power == 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x"
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power == 0:
                        base = str(base)
                        xvar = base
                        vartwo[vartwoinit] = xvar
                    elif power > 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power < 0:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar                   
                    vartwoinit += 1
                    if vartwoinit == vartwolen:
                        break
            vartwo = ''.join(vartwo)   
            dydx = varone[0],"(",vartwo,")",varone[1],"(",vartwo,")","|"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
            print(vartwo)  
        elif "cosec" in var:
            #splitting the variable at the trig function
            varsplit = var.split("cosec")
            print(varsplit)
            #replacing the empty variable with the new trig function
            varsplit[0] = "ln|cosec,-cot"
            varone = varsplit[0]
            varone = varone.split(",")
            print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            print(varsplit)
            #saving the first variable for use later
            varone = varsplit[0]
            print(varone)
            #making the split variable one variable
            varsplit = varsplit[1]
            print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = ''.join(varsplit)
            print(vartwo)
            vartwo = re.split('([y|u])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo)
            vartwolen = len(vartwo)
            vartwoinit = 0
            while vartwoinit < vartwolen:
                workingvar = vartwo[vartwoinit]
                print(workingvar,"workingvar")
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    print(powerlen,"powerlen")
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    print(base,"base")
                    print(power,"power")
                    base = int(base)
                    power = int(power)
                    power = power + 1
                    base = base/power
                    if power == 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x"
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power == 0:
                        base = str(base)
                        xvar = base
                        vartwo[vartwoinit] = xvar
                    elif power > 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar
                    elif power < 0:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        vartwo[vartwoinit] = xvar                   
                    vartwoinit += 1
                    if vartwoinit == vartwolen:
                        break
            vartwo = ''.join(vartwo)   
            dydx = varone[0],"(",vartwo,")",varone[1],"(",vartwo,")","|"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
            print(vartwo)
        elif "x" in var:
            print("doing x var")
            varsplit = var.split("x")
            print(varsplit)
            varbase = varsplit[0]
            print(varbase,"varbase")
            if "^" in varsplit[1]:
                varsplit = ''.join(varsplit)
                varsplit = varsplit.split("^")
                varpower = varsplit[1]
                print(varpower,"varpower")
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
def substituion(equation): # done
    u = equation
    equation = re.split("([(])",equation)
    print(equation,"equation")
    bsloc = equation.index("(")
    yvarloc = bsloc - 1
    uvarloc = bsloc + 1
    uvar = equation[uvarloc]
    uvar = re.split("([)])",uvar)
    uvarlen = len(uvar)   
    uvarlen = uvarlen - 1
    del uvar[uvarlen]
    uvarlen = uvarlen - 1
    del uvar[uvarlen]
    uvar = ''.join(uvar)
    yvarbase = equation[yvarloc]
    equation = ''.join(equation)
    equation = re.split("([)])",equation)
    beloc = equation.index(")")
    yvarpwrloc = beloc + 1
    yvarpwr = equation[yvarpwrloc]
    if yvarpwr == None:
        yvarpwr = 1
    else:
        yvarpwr = yvarpwr    
    yvar = yvarbase,"(u)",yvarpwr
    yvar = ''.join(yvar)
    equationsplit = re.split('([+-])',uvar)
    differential(equationsplit)
    uvarnew = equationsplit
    dydx = u,"*",uvarnew
    dydx = ''.join(dydx)
    return dydx
def chain(equation): # done needs testing
    u = equation
    equation = re.split("([(])",equation)
    ##print(equation,"equation")
    bsloc = equation.index("(")
    ##yvarloc = bsloc - 1
    #finding the u variable
    uvarloc = bsloc + 1
    #saving uvariable for use
    uvar = equation[uvarloc]
    uvar = re.split("([)])",uvar)
    uvarlen = len(uvar)   
    uvarlen = uvarlen - 1
    del uvar[uvarlen]
    uvarlen = uvarlen - 1
    del uvar[uvarlen]
    #getting uvariable without brackets
    uvar = ''.join(uvar)
    ##yvarbase = equation[yvarloc]
    ##equation = ''.join(equation)
    ##equation = re.split("([)])",equation)
    ##beloc = equation.index(")")
    ##yvarpwrloc = beloc + 1
    ##yvarpwr = equation[yvarpwrloc]
    ##if yvarpwr == None:
    ##    yvarpwr = 1
    ##else:
    ##    yvarpwr = yvarpwr    
    ##yvar = yvarbase,"(u)",yvarpwr
    ##yvar = ''.join(yvar)
    #differntial of u var
    equationsplit = re.split('([+-])',uvar)
    differential(equationsplit)
    uvarnew = equationsplit 
    uvarnew = ''.join(uvarnew)
    #finding what y is
    yeqfrst = re.split("([(])",u)
    yeqscnd = re.split("([)])",u)
    ybsloc = yeqfrst.index("(")
    ybsscndloc = yeqscnd.index(")")
    #finding the y base
    ysbaseloc = ybsloc - 1
    ysbasescndloc = ybsscndloc + 1
    yeqbase = yeqfrst[ysbaseloc]
    #finding the y power
    yeqpwr = yeqscnd[ysbasescndloc]
    #differential of y power and base
    equationsplit = re.split('([+-])',yeqbase)
    differential(equationsplit)
    yvarbse = equationsplit
    yvarbse = ''.join(yvarbse)
    equationsplit = re.split('([+-])',yeqpwr)
    differential(equationsplit)
    yvarpwr = equationsplit
    yvarpwr = ''.join(yvarpwr)
    #creating final output
    dydx = yvarbse,"(",uvarnew,")",yvarpwr
    
    print(dydx,"equationfinal")
    dydx = ''.join(dydx)
    return dydx
def quotient(equation): # done needs testing
    equation = re.split("([/])",equation)
    divloc = equation.index("/")
    uvarloc = divloc - 1
    vvarloc = divloc + 1
    uvar = equation[uvarloc]
    vvar = equation[uvarloc]
    uvar = ''.join(uvar)
    vvar = ''.join(vvar)
    equationsplit = re.split('([+-])',uvar)
    differential(equationsplit)
    uvarnew = equationsplit
    equationsplit = re.split('([+-])',vvar)
    differential(equationsplit)
    vvarnew = equationsplit
    dydx = uvarnew,"/",vvarnew
    dydx = ''.join(dydx)
    return dydx
def product(equation): # needs starting
def reversechain(equation): # needs starting
def parts(equation): # needs starting
   
    
    

choice = input("differential,integral")           
if choice == "differential":
    secondarychoice = input("normal,chain,quotient")
    print("please use y for + and u for - for multiple variables in brackets, only for use when using normal")
    equation = input("please enter the equation")
    bgnequation = equation
    if secondarychoice == "normal":
        equationsplit = re.split('([+-])',equation)
        differential(equationsplit)
        print(bgnequation," == ",equationsplit)
    elif secondarychoice == "chain":
        equationchain = chain(equation)
        print(bgnequation ," == ",equationchain)
    elif secondarychoice == "quotient":
        equationquotient = quotient(equation)
        print(bgnequation ," == ",equationquotient)
elif choice == "integral":
    secondarychoice = input("normal,substituion")
    print("please use y for + and u for - for multiple variables in brackets, only for use when using normal")
    equation = input("please enter the equation")
    bgnequation = equation
    if secondarychoice == "normal":
        equationsplit = re.split('([+-])',equation)
        integral(equationsplit)
        print(bgnequation," == ",equationsplit)
    elif secondarychoice == "substituion":
        equationsub = substituion(equation)
        print(bgnequation," == ",equationsub)
        



