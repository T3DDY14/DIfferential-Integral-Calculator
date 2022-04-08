from fractions import Fraction
import numpy as np
import math
import re

def differential(equationsplit):
    trigfunction = ['sin','cos','tan','sec','cosec','cot']
    sctloclen = len(equationsplit)
    sctinit = 0
    difsct = []
    while sctinit < sctloclen:
        var = equationsplit[sctinit]
        if "sin" in var:
            varsplit = var.split("sin")
            print(varsplit)
            varsplit[0] = "cos"
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
                print(dydx)
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")"
                dydx = ''.join(dydx)
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")"
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
                print(dydx)
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")"
                dydx = ''.join(dydx)
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")"
                dydx = ''.join(dydx)
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
                print(dydx)
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")"
                dydx = ''.join(dydx)
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")"
                dydx = ''.join(dydx)
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
                print(dydx)
            elif vartwopower == 1:
                dydx = varone,"(",vartwobase,"x",")"
                dydx = ''.join(dydx)
            elif vartwopower == 0:
                dydx = varone,"(",vartwobase,")"
                dydx = ''.join(dydx)
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
                print(dydx)
            elif vartwopower == 1:
                dydx = varone[0],"(",vartwobase,"x",")",varone[1],"(",vartwobase,"x",")"
                dydx = ''.join(dydx)
            elif vartwopower == 0:
                dydx = varone[0],"(",vartwobase,")",varone[1],"(",vartwobase,")"
                dydx = ''.join(dydx)
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
                print(dydx)
            elif vartwopower == 1:
                dydx = varone[0],"(",vartwobase,"x",")",varone[1],"(",vartwobase,"x",")"
                dydx = ''.join(dydx)
            elif vartwopower == 0:
                dydx = varone[0],"(",vartwobase,")",varone[1],"(",vartwobase,")"
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
            varbase = varbase*varpower
            varpower = varpower - 1
            varbase = str(varbase)
            if varpower > 1:
                varpower = str(varpower)
                dydx = varone,"x^",varpower
                dydx = ''.join(dydx)
                print(dydx)
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
def integral(equationsplit):

    trigfunction = ['sin','cos','tan','sec','cosec','cot']
    sctloclen = len(equationsplit)
    sctinit = 0
    difsct = []
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
                print(dydx)
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
                print(dydx)
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
                print(dydx)
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
                print(dydx)
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
                print(dydx)
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
                print(dydx)
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
                print(dydx)
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
def substituion(equationsplit):
def chain(equationsplit):
def quotient(equationsplit):















choice = input("differential,integral")           
equation = input("please enter the equation")
equationsplit = re.split('([+-])',equation)
if choice == "differential":
    differential(equationsplit)
elif choice == "integral":
    integral(equationsplit)

print(equationsplit)


