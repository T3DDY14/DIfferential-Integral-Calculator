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
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")","|","+C"
                dydx = ''.join(dydx)               
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")","|","+C"
                dydx = ''.join(dydx)                
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
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")","|","+C"
                dydx = ''.join(dydx)                
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")","|","+C"
                dydx = ''.join(dydx)               
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
            elif vartwopower == 1:
                dydx = varone[0],"(",vartwobase,"x",")","+",varone[1],"(",vartwobase,"x",")",")","|","+C"
                dydx = ''.join(dydx)               
            elif vartwopower == 0:
                dydx = varone[0],"(",vartwobase,")","+",varone[1],"(",vartwobase,")",")","|","+C"
                dydx = ''.join(dydx)              
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
            elif vartwopower == 1:
                dydx = varone[0],"(",vartwobase,"x",")","-",varone[1],"(",vartwobase,"x",")","|","+C"
                dydx = ''.join(dydx)     
            elif vartwopower == 0:
                dydx = varone[0],"(",vartwobase,")","-",varone[1],"(",vartwobase,")","|","+C"
                dydx = ''.join(dydx)         
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
            elif varpower == 1:
                dydx = varone,"x"
                dydx = ''.join(dydx)    
            elif varpower == 0:
                dydx = varone
                dydx = ''.join(dydx)     
            equationsplit[sctinit] = dydx            
        else:
            print("oops")                    
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


