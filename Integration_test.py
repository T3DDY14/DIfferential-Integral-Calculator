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
        else:
            print("oops")

                    
        sctinit = sctinit + 1
        if sctinit == sctloclen:
            break

equation = input("please enter the equation")
equationsplit = re.split('([+-])',equation)
print(equationsplit)
differential(equationsplit)
print(equationsplit)


