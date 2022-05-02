from fractions import Fraction
#import numpy as np
import math
import re
import tkinter as tk
import sympy 

def differential(equationsplit): # done
    trigfunction = ['sin','cos','tan','sec','cosec','cot']
    sctloclen = len(equationsplit)
    sctinit = 0
    dif = []
    while sctinit < sctloclen:
        var = equationsplit[sctinit] #puting variable from array into a string variable
        print(var,"var")        
        #checking if the variable is a trig function or a normal
        if "sin" in var: #done 
            #splitting the variable at the trig function
            varsplit = re.split('(sin)',var)
            ##print(varsplit)
            varsplitlen = len(varsplit)
            varsplitbase = varsplit[0]
            ##print(varsplitlen)
            if varsplitbase == "":
                varsplitbase = 1
                #replacing the empty variable with the new trig function
                varsplit[1] = "cos"
                # #saving the first variable for use later 
                varone = varsplit[1]
            else:
                varsplitbase = varsplit[0]            
                varsplitbase = varsplitbase
                #replacing the empty variable with the new trig function
                varsplit[1] = "cos"
                #saving the first variable for use later
                varone = varsplit[1]     
            ##print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            ##print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            ##print(varsplit)
            
            #making the split variable one variable
            varsplit = varsplit[1]
            ##print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            ##print(varsplit)
            vartwo = ''.join(varsplit)
            ##print(vartwo)
            varthree = []            
            vartwo = re.sub('[y]','+',vartwo)
            vartwo = re.sub('[u]','-',vartwo)
            vartwo = re.sub('[d]','/',vartwo)
            varthree = vartwo
            varsplitbasex = re.search("x",varsplitbase)
            print(varsplitbasex,"xd")
            varsplitbase = re.sub('[y]','+',varsplitbase)
            varsplitbase = re.sub('[u]','-',varsplitbase)
            varsplitbase = re.sub('[d]','/',varsplitbase) 
            varsplitbase = re.split('([y|u|d])',varsplitbase)
            varsplitbaselen = len(varsplitbase)
            varsplitbaseinit = 0            
            print(vartwo)
            vartwo = re.split('([y|u|d])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo,"vartwo")
            #varthree = re.split('([y|u|d])',varthree)
            vartwolen = len(vartwo)
            #varthreelen = len(varthree)
            vartwoinit = 0
            #varthreeinit = 0
            if varsplitbasex == None:
                varsplitbase = varsplitbase
            else:
                while varsplitbaseinit < varsplitbaselen:
                    if varsplitbaseinit == varsplitbaselen:
                        break
                    workingvar = varsplitbase[varsplitbaseinit]
                    if workingvar == "y":
                        workingvar = "+"
                        varsplitbase[varsplitbaseinit] = workingvar
                        varsplitbaseinit += 1
                    elif workingvar == "u":
                        workingvar = "-"
                        varsplitbase[varsplitbaseinit] = workingvar
                        varsplitbaseinit += 1
                    elif workingvar == "d":
                        workingvar = "/"
                        varthree[varthreeinit] = workingvar
                        varthreeinit += 1                    
                    elif workingvar != "y":
                        ##print(workingvar)
                        workingvar = workingvar.split("x")
                        base = workingvar[0]
                        power = workingvar[1]
                        power = ''.join(power)
                        power = power.split("^")
                        powerlen = len(power)
                        if powerlen == 2:
                            power = power[1]
                        elif powerlen == 1:
                            power = 1
                        base = Fraction(base)
                        power = Fraction(power)
                        base = base*power
                        ##base = base*varsplitbase
                        power = power - 1                  
                        if power == 1:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x"
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power == 0:
                            base = str(base)
                            xvar = base
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power > 1:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x^",power
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power < 0:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x^",power
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar                   
                        varsplitbaseinit += 1
            while vartwoinit < vartwolen:
                if vartwoinit == vartwolen:
                    break
                workingvar = vartwo[vartwoinit]
                print("workingvar",workingvar)
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "d":
                    workingvar = "/"
                    varthree[varthreeinit] = workingvar
                    varthreeinit += 1    
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    if base == "x":
                        base = 1
                    else:
                        base = base
                    base = Fraction(base)
                    power = Fraction(power)
                    base = base*power
                    ##base = base*varsplitbase
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
            vartwo = ''.join(vartwo)
            varthree = ''.join(varthree)
            varsplitbase = ''.join(varsplitbase)
            varsplitbase = str(varsplitbase)            
            dydx = varsplitbase,"*",vartwo,varone,"(",varthree,")"
            print("dydx",dydx)
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
            print(vartwo)   
        elif "cosec" in var: # done
            varsplit = re.split('(cosec)',var)
            ##print(varsplit)
            varsplitlen = len(varsplit)
            varsplitbase = varsplit[0]
            ##print(varsplitlen)
            if varsplitbase == "":
                varsplitbase = 1
                #replacing the empty variable with the new trig function
                varsplit[1] = "cosec,cot"
                # #saving the first variable for use later 
                varone = varsplit[1]
            else:
                varsplitbase = varsplit[0]            
                varsplitbase = varsplitbase
                #replacing the empty variable with the new trig function
                varsplit[1] = "cosec,cot"
                #saving the first variable for use later
                varone = varsplit[1]
            ##print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            ##print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            ##print(varsplit)

            #making the split variable one variable
            varsplit = varsplit[1]
            ##print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            ##print(varsplit)
            vartwo = ''.join(varsplit)
            ##print(vartwo)
            varthree = []
            vartwo = re.sub('[y]','+',vartwo)
            vartwo = re.sub('[u]','-',vartwo)
            vartwo = re.sub('[d]','/',vartwo)
            varthree = vartwo
            varsplitbasex = re.search("x",varsplitbase)
            print(varsplitbasex,"xd")
            varsplitbase = re.sub('[y]','+',varsplitbase)
            varsplitbase = re.sub('[u]','-',varsplitbase)
            varsplitbase = re.sub('[d]','/',varsplitbase) 
            varsplitbase = re.split('([y|u|d])',varsplitbase)
            varsplitbaselen = len(varsplitbase)
            varsplitbaseinit = 0            
            print(vartwo)
            vartwo = re.split('([y|u|d])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo,"vartwo")
            #varthree = re.split('([y|u|d])',varthree)
            vartwolen = len(vartwo)
            #varthreelen = len(varthree)
            vartwoinit = 0
            #varthreeinit = 0 
            if varsplitbasex == None:
                varsplitbase = varsplitbase
            else:
                while varsplitbaseinit < varsplitbaselen:
                    if varsplitbaseinit == varsplitbaselen:
                        break
                    workingvar = varsplitbase[varsplitbaseinit]
                    if workingvar == "y":
                        workingvar = "+"
                        varsplitbase[varsplitbaseinit] = workingvar
                        varsplitbaseinit += 1
                    elif workingvar == "u":
                        workingvar = "-"
                        varsplitbase[varsplitbaseinit] = workingvar
                        varsplitbaseinit += 1
                    elif workingvar == "d":
                        workingvar = "/"
                        varthree[varthreeinit] = workingvar
                        varthreeinit += 1                    
                    elif workingvar != "y":
                        ##print(workingvar)
                        workingvar = workingvar.split("x")
                        base = workingvar[0]
                        power = workingvar[1]
                        power = ''.join(power)
                        power = power.split("^")
                        powerlen = len(power)
                        if powerlen == 2:
                            power = power[1]
                        elif powerlen == 1:
                            power = 1
                        base = Fraction(base)
                        power = Fraction(power)
                        base = base*power
                        ##base = base*varsplitbase
                        power = power - 1                  
                        if power == 1:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x"
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power == 0:
                            base = str(base)
                            xvar = base
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power > 1:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x^",power
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power < 0:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x^",power
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar                   
                        varsplitbaseinit += 1           
            while vartwoinit < vartwolen:
                if vartwoinit == vartwolen:
                    break
                workingvar = vartwo[vartwoinit]
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "d":
                    workingvar = "/"
                    varthree[varthreeinit] = workingvar
                    varthreeinit += 1    
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    if base == "x":
                        base = 1
                    else:
                        base = base
                    base = Fraction(base)
                    power = Fraction(power)
                    base = base*power
                    ##base = base*varsplitbase
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
            vartwo = ''.join(vartwo)
            varthree = ''.join(varthree)
            varsplitbase = ''.join(varsplitbase)
            varsplitbase = str(varsplitbase)
            varone = varone.split(",")
            print(varone,"varone")
            dydx = "-",varsplitbase,"*",vartwo,varone[0],"(",varthree,")",varone[1],"(",varthree,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx                     
        elif "cos" in var: #done
            #splitting the variable at the trig function
            varsplit = re.split('(cos)',var)
            ##print(varsplit)
            varsplitlen = len(varsplit)
            varsplitbase = varsplit[0]
            ##print(varsplitlen)
            if varsplitbase == "":
                varsplitbase = 1
                #replacing the empty variable with the new trig function
                varsplit[1] = "sin"
                # #saving the first variable for use later 
                varone = varsplit[1]
            else:
                varsplitbase = varsplit[0]            
                varsplitbase = varsplitbase
                #replacing the empty variable with the new trig function
                varsplit[1] = "sin"
                #saving the first variable for use later
                varone = varsplit[1]     
            ##print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            ##print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            ##print(varsplit)
            
            #making the split variable one variable
            varsplit = varsplit[1]
            ##print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            ##print(varsplit)
            vartwo = ''.join(varsplit)
            ##print(vartwo)
            varthree = []            
            vartwo = re.sub('[y]','+',vartwo)
            vartwo = re.sub('[u]','-',vartwo)
            vartwo = re.sub('[d]','/',vartwo)
            varthree = vartwo
            varsplitbasex = re.search("x",varsplitbase)
            print(varsplitbasex,"xd")
            varsplitbase = re.sub('[y]','+',varsplitbase)
            varsplitbase = re.sub('[u]','-',varsplitbase)
            varsplitbase = re.sub('[d]','/',varsplitbase) 
            varsplitbase = re.split('([y|u|d])',varsplitbase)
            varsplitbaselen = len(varsplitbase)
            varsplitbaseinit = 0            
            print(vartwo)
            vartwo = re.split('([y|u|d])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo,"vartwo")
            #varthree = re.split('([y|u|d])',varthree)
            vartwolen = len(vartwo)
            #varthreelen = len(varthree)
            vartwoinit = 0
            #varthreeinit = 0
            if varsplitbasex == None:
                varsplitbase = varsplitbase
            else:
                while varsplitbaseinit < varsplitbaselen:
                    if varsplitbaseinit == varsplitbaselen:
                        break
                    workingvar = varsplitbase[varsplitbaseinit]
                    if workingvar == "y":
                        workingvar = "+"
                        varsplitbase[varsplitbaseinit] = workingvar
                        varsplitbaseinit += 1
                    elif workingvar == "u":
                        workingvar = "-"
                        varsplitbase[varsplitbaseinit] = workingvar
                        varsplitbaseinit += 1
                    elif workingvar == "d":
                        workingvar = "/"
                        varthree[varthreeinit] = workingvar
                        varthreeinit += 1                    
                    elif workingvar != "y":
                        ##print(workingvar)
                        workingvar = workingvar.split("x")
                        base = workingvar[0]
                        power = workingvar[1]
                        power = ''.join(power)
                        power = power.split("^")
                        powerlen = len(power)
                        if powerlen == 2:
                            power = power[1]
                        elif powerlen == 1:
                            power = 1
                        base = Fraction(base)
                        power = Fraction(power)
                        base = base*power
                        ##base = base*varsplitbase
                        power = power - 1                  
                        if power == 1:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x"
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power == 0:
                            base = str(base)
                            xvar = base
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power > 1:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x^",power
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power < 0:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x^",power
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar                   
                        varsplitbaseinit += 1
            while vartwoinit < vartwolen:
                if vartwoinit == vartwolen:
                    break
                workingvar = vartwo[vartwoinit]
                print("workingvar",workingvar)
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "d":
                    workingvar = "/"
                    varthree[varthreeinit] = workingvar
                    varthreeinit += 1    
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    if base == "x":
                        base = 1
                    else:
                        base = base
                    base = Fraction(base)
                    power = Fraction(power)
                    base = base*power
                    ##base = base*varsplitbase
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
            vartwo = ''.join(vartwo)
            varthree = ''.join(varthree)
            varsplitbase = ''.join(varsplitbase)
            varsplitbase = str(varsplitbase)            
            dydx = "-",varsplitbase,"*",vartwo,varone,"(",varthree,")"
            print("dydx",dydx)
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
            print(vartwo)
        elif "tan" in var: #done
            #splitting the variable at the trig function
            varsplit = re.split('(tan)',var)
            ##print(varsplit)
            varsplitlen = len(varsplit)
            varsplitbase = varsplit[0]
            ##print(varsplitlen)
            if varsplitbase == "":
                varsplitbase = 1
                #replacing the empty variable with the new trig function
                varsplit[1] = "sec^2"
                # #saving the first variable for use later 
                varone = varsplit[1]
            else:
                varsplitbase = varsplit[0]            
                varsplitbase = varsplitbase
                #replacing the empty variable with the new trig function
                varsplit[1] = "sec^2"
                #saving the first variable for use later
                varone = varsplit[1]     
            ##print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            ##print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            ##print(varsplit)
            
            #making the split variable one variable
            varsplit = varsplit[1]
            ##print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            ##print(varsplit)
            vartwo = ''.join(varsplit)
            ##print(vartwo)
            varthree = []            
            vartwo = re.sub('[y]','+',vartwo)
            vartwo = re.sub('[u]','-',vartwo)
            vartwo = re.sub('[d]','/',vartwo)
            varthree = vartwo
            varsplitbasex = re.search("x",varsplitbase)
            print(varsplitbasex,"xd")
            varsplitbase = re.sub('[y]','+',varsplitbase)
            varsplitbase = re.sub('[u]','-',varsplitbase)
            varsplitbase = re.sub('[d]','/',varsplitbase) 
            varsplitbase = re.split('([y|u|d])',varsplitbase)
            varsplitbaselen = len(varsplitbase)
            varsplitbaseinit = 0            
            print(vartwo)
            vartwo = re.split('([y|u|d])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo,"vartwo")
            #varthree = re.split('([y|u|d])',varthree)
            vartwolen = len(vartwo)
            #varthreelen = len(varthree)
            vartwoinit = 0
            #varthreeinit = 0
            if varsplitbasex == None:
                varsplitbase = varsplitbase
            else:
                while varsplitbaseinit < varsplitbaselen:
                    if varsplitbaseinit == varsplitbaselen:
                        break
                    workingvar = varsplitbase[varsplitbaseinit]
                    if workingvar == "y":
                        workingvar = "+"
                        varsplitbase[varsplitbaseinit] = workingvar
                        varsplitbaseinit += 1
                    elif workingvar == "u":
                        workingvar = "-"
                        varsplitbase[varsplitbaseinit] = workingvar
                        varsplitbaseinit += 1
                    elif workingvar == "d":
                        workingvar = "/"
                        varthree[varthreeinit] = workingvar
                        varthreeinit += 1                    
                    elif workingvar != "y":
                        ##print(workingvar)
                        workingvar = workingvar.split("x")
                        base = workingvar[0]
                        power = workingvar[1]
                        power = ''.join(power)
                        power = power.split("^")
                        powerlen = len(power)
                        if powerlen == 2:
                            power = power[1]
                        elif powerlen == 1:
                            power = 1
                        base = Fraction(base)
                        power = Fraction(power)
                        base = base*power
                        ##base = base*varsplitbase
                        power = power - 1                  
                        if power == 1:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x"
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power == 0:
                            base = str(base)
                            xvar = base
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power > 1:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x^",power
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power < 0:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x^",power
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar                   
                        varsplitbaseinit += 1
            while vartwoinit < vartwolen:
                if vartwoinit == vartwolen:
                    break
                workingvar = vartwo[vartwoinit]
                print("workingvar",workingvar)
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "d":
                    workingvar = "/"
                    varthree[varthreeinit] = workingvar
                    varthreeinit += 1    
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    if base == "x":
                        base = 1
                    else:
                        base = base
                    base = Fraction(base)
                    power = Fraction(power)
                    base = base*power
                    ##base = base*varsplitbase
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
            vartwo = ''.join(vartwo)
            varthree = ''.join(varthree)
            varsplitbase = ''.join(varsplitbase)
            varsplitbase = str(varsplitbase)
            dydx = varsplitbase,"*",vartwo,varone,"(",varthree,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
        elif "cot" in var: #done
            #splitting the variable at the trig function
            varsplit = re.split('(cot)',var)
            ##print(varsplit)
            varsplitlen = len(varsplit)
            varsplitbase = varsplit[0]
            ##print(varsplitlen)
            if varsplitbase == "":
                varsplitbase = 1
                #replacing the empty variable with the new trig function
                varsplit[1] = "cosec^2"
                # #saving the first variable for use later 
                varone = varsplit[1]
            else:
                varsplitbase = varsplit[0]            
                varsplitbase = varsplitbase
                #replacing the empty variable with the new trig function
                varsplit[1] = "cosec^2"
                #saving the first variable for use later
                varone = varsplit[1]     
            ##print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            ##print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            ##print(varsplit)
            
            #making the split variable one variable
            varsplit = varsplit[1]
            ##print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            ##print(varsplit)
            vartwo = ''.join(varsplit)
            ##print(vartwo)
            varthree = []            
            vartwo = re.sub('[y]','+',vartwo)
            vartwo = re.sub('[u]','-',vartwo)
            vartwo = re.sub('[d]','/',vartwo)
            varthree = vartwo
            varsplitbasex = re.search("x",varsplitbase)
            print(varsplitbasex,"xd")
            varsplitbase = re.sub('[y]','+',varsplitbase)
            varsplitbase = re.sub('[u]','-',varsplitbase)
            varsplitbase = re.sub('[d]','/',varsplitbase) 
            varsplitbase = re.split('([y|u|d])',varsplitbase)
            varsplitbaselen = len(varsplitbase)
            varsplitbaseinit = 0            
            print(vartwo)
            vartwo = re.split('([y|u|d])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo,"vartwo")
            #varthree = re.split('([y|u|d])',varthree)
            vartwolen = len(vartwo)
            #varthreelen = len(varthree)
            vartwoinit = 0
            #varthreeinit = 0
            if varsplitbasex == None:
                varsplitbase = varsplitbase
            else:
                while varsplitbaseinit < varsplitbaselen:
                    if varsplitbaseinit == varsplitbaselen:
                        break
                    workingvar = varsplitbase[varsplitbaseinit]
                    if workingvar == "y":
                        workingvar = "+"
                        varsplitbase[varsplitbaseinit] = workingvar
                        varsplitbaseinit += 1
                    elif workingvar == "u":
                        workingvar = "-"
                        varsplitbase[varsplitbaseinit] = workingvar
                        varsplitbaseinit += 1
                    elif workingvar == "d":
                        workingvar = "/"
                        varthree[varthreeinit] = workingvar
                        varthreeinit += 1                    
                    elif workingvar != "y":
                        ##print(workingvar)
                        workingvar = workingvar.split("x")
                        base = workingvar[0]
                        power = workingvar[1]
                        power = ''.join(power)
                        power = power.split("^")
                        powerlen = len(power)
                        if powerlen == 2:
                            power = power[1]
                        elif powerlen == 1:
                            power = 1
                        base = Fraction(base)
                        power = Fraction(power)
                        base = base*power
                        ##base = base*varsplitbase
                        power = power - 1                  
                        if power == 1:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x"
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power == 0:
                            base = str(base)
                            xvar = base
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power > 1:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x^",power
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power < 0:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x^",power
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar                   
                        varsplitbaseinit += 1
            while vartwoinit < vartwolen:
                if vartwoinit == vartwolen:
                    break
                workingvar = vartwo[vartwoinit]
                print("workingvar",workingvar)
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "d":
                    workingvar = "/"
                    varthree[varthreeinit] = workingvar
                    varthreeinit += 1    
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    if base == "x":
                        base = 1
                    else:
                        base = base
                    base = Fraction(base)
                    power = Fraction(power)
                    base = base*power
                    ##base = base*varsplitbase
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
            vartwo = ''.join(vartwo)
            varthree = ''.join(varthree)
            varsplitbase = ''.join(varsplitbase)
            varsplitbase = str(varsplitbase)            
            dydx = varsplitbase,"*",vartwo,varone,"(",varthree,")"
            print("dydx",dydx)
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
            print(vartwo)          
        elif "sec" in var: #done
            varsplit = re.split('(sec)',var)
            ##print(varsplit)
            varsplitlen = len(varsplit)
            varsplitbase = varsplit[0]
            ##print(varsplitlen)
            if varsplitbase == "":
                varsplitbase = 1
                #replacing the empty variable with the new trig function
                varsplit[1] = "sec,tan"
                # #saving the first variable for use later 
                varone = varsplit[1]
            else:
                varsplitbase = varsplit[0]            
                varsplitbase = varsplitbase
                #replacing the empty variable with the new trig function
                varsplit[1] = "sec,tan"
                #saving the first variable for use later
                varone = varsplit[1]
            ##print(varsplit)
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            ##print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            ##print(varsplit)

            #making the split variable one variable
            varsplit = varsplit[1]
            ##print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            ##print(varsplit)
            vartwo = ''.join(varsplit)
            ##print(vartwo)
            varthree = []
            vartwo = re.sub('[y]','+',vartwo)
            vartwo = re.sub('[u]','-',vartwo)
            vartwo = re.sub('[d]','/',vartwo)
            varthree = vartwo
            varsplitbasex = re.search("x",varsplitbase)
            print(varsplitbasex,"xd")
            varsplitbase = re.sub('[y]','+',varsplitbase)
            varsplitbase = re.sub('[u]','-',varsplitbase)
            varsplitbase = re.sub('[d]','/',varsplitbase) 
            varsplitbase = re.split('([y|u|d])',varsplitbase)
            varsplitbaselen = len(varsplitbase)
            varsplitbaseinit = 0            
            print(vartwo)
            vartwo = re.split('([y|u|d])',vartwo) #splits the vartwo by the y whilst keeping the y key
            print(vartwo,"vartwo")
            #varthree = re.split('([y|u|d])',varthree)
            vartwolen = len(vartwo)
            #varthreelen = len(varthree)
            vartwoinit = 0
            #varthreeinit = 0 
            if varsplitbasex == None:
                varsplitbase = varsplitbase
            else:
                while varsplitbaseinit < varsplitbaselen:
                    if varsplitbaseinit == varsplitbaselen:
                        break
                    workingvar = varsplitbase[varsplitbaseinit]
                    if workingvar == "y":
                        workingvar = "+"
                        varsplitbase[varsplitbaseinit] = workingvar
                        varsplitbaseinit += 1
                    elif workingvar == "u":
                        workingvar = "-"
                        varsplitbase[varsplitbaseinit] = workingvar
                        varsplitbaseinit += 1
                    elif workingvar == "d":
                        workingvar = "/"
                        varthree[varthreeinit] = workingvar
                        varthreeinit += 1                    
                    elif workingvar != "y":
                        ##print(workingvar)
                        workingvar = workingvar.split("x")
                        base = workingvar[0]
                        power = workingvar[1]
                        power = ''.join(power)
                        power = power.split("^")
                        powerlen = len(power)
                        if powerlen == 2:
                            power = power[1]
                        elif powerlen == 1:
                            power = 1
                        base = Fraction(base)
                        power = Fraction(power)
                        base = base*power
                        ##base = base*varsplitbase
                        power = power - 1                  
                        if power == 1:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x"
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power == 0:
                            base = str(base)
                            xvar = base
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power > 1:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x^",power
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar
                        elif power < 0:
                            base = str(base)
                            power = str(power)
                            xvar = base,"x^",power
                            xvar = ''.join(xvar)
                            varsplitbase[varsplitbaseinit] = xvar                   
                        varsplitbaseinit += 1           
            while vartwoinit < vartwolen:
                if vartwoinit == vartwolen:
                    break
                workingvar = vartwo[vartwoinit]
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "d":
                    workingvar = "/"
                    varthree[varthreeinit] = workingvar
                    varthreeinit += 1    
                elif workingvar != "y":
                    print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    if base == "x":
                        base = 1
                    else:
                        base = base
                    base = Fraction(base)
                    power = Fraction(power)
                    base = base*power
                    ##base = base*varsplitbase
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
            vartwo = ''.join(vartwo)
            varthree = ''.join(varthree)
            varsplitbase = ''.join(varsplitbase)
            varsplitbase = str(varsplitbase)
            varone = varone.split(",")
            print(varone,"varone")
            dydx = "-",varsplitbase,"*",vartwo,varone[0],"(",varthree,")",varone[1],"(",varthree,")"
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx             
        elif "ln" in var: #needs rewriting        
            #splitting the variable at the trig function
            varsplit = re.split('(ln)',var)
            print(varsplit,"ad")
            varsplitlen = len(varsplit)
            varsplitbase = varsplit[0]
            ##print(varsplitlen)
            if varsplitbase == "":
                varsplitbase = 1
                #replacing the empty variable with the new trig function
                varsplit[1] = "1/"
                # #saving the first variable for use later 
                varone = varsplit[1]
                varpower = varsplit[2]
            else:
                varsplitbase = varsplit[0]            
                varsplitbase = varsplitbase
                #replacing the empty variable with the new trig function
                varsplit[1] = "1/"
                #saving the first variable for use later
                varone = varsplit[1]
                varpower = varsplit[2]                
            print(varsplit)
            #joining the array back together for another split
            ##varwhole = "".join(varsplit)
            ##print(varwhole)
            #splitting the array for the x component
            
            varsplit = varpower.split("(")
            print(varsplit)
            
            #making the split variable one variable
            varsplit = varsplit[1]
            print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            print(varsplit)
            vartwo = ''.join(varsplit)
            print(vartwo)
            varthree = []
            
            vartwo = re.sub('[y]','+',vartwo)
            vartwo = re.sub('[u]','-',vartwo)
            vartwo = re.sub('[d]','/',vartwo)           
            vartwo = re.split('([y|u|d])',vartwo) #splits the vartwo by the y whilst keeping the y key
            ##varthree = re.split('([y|u|d])',varthree)
            varthree = vartwo
            varsplitbase = re.sub('[y]','+',varsplitbase)
            varsplitbase = re.sub('[u]','-',varsplitbase)
            varsplitbase = re.sub('[d]','/',varsplitbase) 
            varsplitbase = re.split('([y|u|d])',varsplitbase)
            varsplitbaselen = len(varsplitbase)
            varsplitbaseinit = 0
            vartwolen = len(vartwo)
            varthreelen = len(varthree)
            vartwoinit = 0
            varthreeinit = 0 
            while varthreeinit < varthreelen:
                workingvar = vartwo[varthreeinit]
                if varthreeinit == varthreelen:
                    break
                if workingvar == "y":
                    workingvar = "+"
                    varthree[varthreeinit] = workingvar
                    varthreeinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    varthree[varthreeinit] = workingvar
                    varthreeinit += 1
                elif workingvar == "d":
                    workingvar = "/"
                    varthree[varthreeinit] = workingvar
                    varthreeinit += 1                    
                elif workingvar != "y":
                    varthree[varthreeinit] = workingvar
                    varthreeinit += 1
            while vartwoinit < vartwolen:
                if vartwoinit == vartwolen:
                    break
                workingvar = vartwo[vartwoinit]
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "d":
                    workingvar = "/"
                    varthree[varthreeinit] = workingvar
                    varthreeinit += 1                    
                elif workingvar != "y":
                    ##print(workingvar)
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    base = Fraction(base)
                    power = Fraction(power)
                    base = base*power
                    ##base = base*varsplitbase
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
            while varsplitbaseinit < varsplitbaselen:
                if varsplitbaseinit == varsplitbaselen:
                    break
                workingvar = varsplitbase[varsplitbaseinit]
                print(workingvar,"working")
                if workingvar == "y":
                    workingvar = "+"
                    varsplitbase[varsplitbaseinit] = workingvar
                    varsplitbaseinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    varsplitbase[varsplitbaseinit] = workingvar
                    varsplitbaseinit += 1
                elif workingvar == "d":
                    workingvar = "/"
                    varthree[varthreeinit] = workingvar
                    varthreeinit += 1                    
                elif workingvar != "y":
                    ##print(workingvar)
                    workingvar = workingvar.split("x")
                    workingvarlen = len(workingvar)
                    print(workingvarlen,"len")
                    if workingvarlen == 1:
                        power = 1
                    else:
                        power = workingvar[1]
                        power = ''.join(power)
                        power = power.split("^")
                        powerlen = len(power)
                        if powerlen == 2:
                            power = power[1]
                        elif powerlen == 1:
                            power = 1
                    base = workingvar[0]
                    base = Fraction(base)
                    power = Fraction(power)
                    base = base*power
                    ##base = base*varsplitbase
                    power = power - 1                  
                    if power == 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x"
                        xvar = ''.join(xvar)
                        varsplitbase[varsplitbaseinit] = xvar
                    elif power == 0:
                        base = str(base)
                        xvar = base
                        varsplitbase[varsplitbaseinit] = xvar
                    elif power > 1:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        varsplitbase[varsplitbaseinit] = xvar
                    elif power < 0:
                        base = str(base)
                        power = str(power)
                        xvar = base,"x^",power
                        xvar = ''.join(xvar)
                        varsplitbase[varsplitbaseinit] = xvar                   
                    varsplitbaseinit += 1
                        
            vartwo = ''.join(vartwo)
            varthree = ''.join(varthree)
            varsplitbase = ''.join(varsplitbase)
            varsplitbase = str(varsplitbase)
            
            dydx = varsplitbase,"*",varone,"(",varthree,")"
            ##print("dydx",dydx)
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx    
        elif "e^" in var: #done        
            #splitting the variable at the trig function
            varsplit = re.split('(e)',var)
            ##print(varsplit,"varsplit")
            varsplitlen = len(varsplit)
            varsplitbase = varsplit[0]
            if varsplitbase == "":
                varsplitbase = 1
                varsplitbase = Fraction(varsplitbase)
            else:
                varsplitbase = Fraction(varsplitbase)
            varone = "e^"
            #joining the array back together for another split
            varwhole = "".join(varsplit)
            ##print(varwhole)
            #splitting the array for the x component
            varsplit = varwhole.split("(")
            print(varsplit,"var")
            
            #making the split variable one variable
            varsplit = varsplit[1]
            ##print(varsplit)
            #splitting the closed bracked to work on variable
            varsplit = varsplit.split(")")
            ##print(varsplit)
            vartwo = ''.join(varsplit)
            ##print(vartwo)
            varthree = []
            vartwo = re.sub('[y]','+',vartwo)
            vartwo = re.sub('[u]','-',vartwo)
            vartwo = re.sub('[d]','/',vartwo)
            varthree = vartwo
            vartwo = re.split('([y|u]|d)',vartwo) #splits the vartwo by the y whilst keeping the y key
            ##varthree = re.split('([y|u|d])',varthree)
            vartwolen = len(vartwo)
            varthreelen = len(varthree)
            vartwoinit = 0
            varthreeinit = 0 
            
            while vartwoinit < vartwolen:
                if vartwoinit == vartwolen:
                    break
                workingvar = vartwo[vartwoinit]
                ##print(workingvar,"wrkvar")
                if workingvar == "y":
                    workingvar = "+"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    vartwo[vartwoinit] = workingvar
                    vartwoinit += 1
                elif workingvar == "d":
                    workingvar = "/"
                    varthree[varthreeinit] = workingvar
                    varthreeinit += 1                    
                elif workingvar != "y":
                    ##print(workingvar,"wrkvar2")
                    workingvar = workingvar.split("x")
                    base = workingvar[0]
                    power = workingvar[1]
                    power = ''.join(power)
                    power = power.split("^")
                    powerlen = len(power)
                    if powerlen == 2:
                        power = power[1]
                    elif powerlen == 1:
                        power = 1
                    base = Fraction(base)
                    power = Fraction(power)
                    base = base*power
                    base = base*varsplitbase
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

                        
            vartwo = ''.join(vartwo)
            varthree = ''.join(varthree) 
            dydx = vartwo,varone,"(",varthree,")"
            ##print("dydx",dydx)
            dydx = ''.join(dydx)
            equationsplit[sctinit] = dydx
        elif "x" in var:
            print("hello")
            varsplit = var.split("x")
            varbase = varsplit[0]
            if "^" in varsplit[1]:
                varsplit = ''.join(varsplit)
                varsplit = varsplit.split("^")
                varpower = varsplit[1]
            elif "^" not in varsplit[1]:
                varpower = 1
            #dydx
            varbase = re.split('([y|u|d])',varbase) #splits the vartwo by the y whilst keeping the y key
            varpower = re.split('([y|u|d])',varpower)            
            varbaselen = len(varbase)
            varpowerlen = len(varpower)
            varbaseinit = 0
            varpowerinit = 0 
            while varbaseinit < varbaselen:
                workingvar = varbase[varbaseinit]
                if varbaseinit == varbaselen:
                    break
                if workingvar == "y":
                    workingvar = "+"
                    varbase[varbaseinit] = workingvar
                    varbaseinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    varbase[varbaseinit] = workingvar
                    varbaseinit += 1
                elif workingvar == "d":
                    workingvar = "/"
                    varbase[varbaseinit] = workingvar
                    varbaseinit += 1
                elif workingvar != "y":
                    varbase[varbaseinit] = workingvar
                    varbaseinit += 1            
            while varpowerinit < varpowerlen:
                workingvar = varpower[varpowerinit]
                if varpowerinit == varpowerlen:
                    break
                if workingvar == "y":
                    workingvar = "+"
                    varpower[varpowerinit] = workingvar
                    varpowerinit += 1
                elif workingvar == "u":
                    workingvar = "-"
                    varpower[varpowerinit] = workingvar
                    varpowerinit += 1
                elif workingvar == "d":
                    workingvar = "/"
                    varpower[varpowerinit] = workingvar
                    varpowerinit += 1
                elif workingvar != "y":
                    varpower[varpowerinit] = workingvar
                    varpowerinit += 1
            varbase = ''.join(varbase)
            varpower = ''.join(varpower)
            varbase = Fraction(varbase)
            varpower = Fraction(varpower)
            varbase = varbase*varpower
            varpower = varpower - 1
            varbase = Fraction(varbase)
            varpower = Fraction(varpower) 
            varbase = str(varbase)
            if varpower > 1 or varpower < 0:
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
    
def integral(equationsplit): # needs fixing
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
                    base = Fraction(base)
                    power = Fraction(power)
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
                    base = Fraction(base)
                    power = Fraction(power)
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
                    base = Fraction(base)
                    power = Fraction(power)
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
                    base = Fraction(base)
                    power = Fraction(power)
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
                    base = Fraction(base)
                    power = Fraction(power)
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
                    base = Fraction(base)
                    power = Fraction(power)
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
            varbase = Fraction(varbase)
            varpower = Fraction(varpower)
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
    print("placeholder")
def reversechain(equation): # needs starting
    print("placeholder")
def parts(equation): # needs starting
    print("placeholder")
def output():
    inp = maininput.get(1.0,"end-1c")
    lblin.config(text = "input: "+inp)
def tkdiff():
    inp = maininput.get(1.0,"end-1c")
    equation = inp
    equationsplit = re.split('([+-/])',equation)
    differential(equationsplit)
    lblin.config(text = "input: "+equation)
    equationsplit = ''.join(equationsplit)
    lblout.config(text = "output: "+equationsplit)
def tkinte():
    inp = maininput.get(1.0,"end-1c")
    equation = inp
    equationsplit = re.split('([+-/])',equation)
    integral(equationsplit)
    lblin.config(text = "input: "+equation)
    equationsplit = ''.join(equationsplit)
    lblout.config(text = "output: "+equationsplit)
    
main= tk.Tk()
main.title("calculator")
lbltxt = tk.Label(main,text="use brackets for any variables after a function eg e^(2x)")
lbltxt.pack()
maininput = tk.Text(main,height = 2 , width = 30)
maininput.pack()
printbutton = tk.Button(main,text = "print",command=output)
printbutton.pack()
differentialbttn = tk.Button(main,text = "differential",command=tkdiff)
differentialbttn.pack()
integralbttn = tk.Button(main,text = "integral",command=tkinte)
integralbttn.pack()
lblin = tk.Label(main,text="")
lblin.pack()
lblout = tk.Label(main,text="")
lblout.pack()


main.mainloop()   
    

choice = input("differential,integral")           
if choice == "differential":
    secondarychoice = input("normal,chain,quotient")
    print("please use y for + and u for - and d for / for multiple variables in brackets, only for use when using normal")
    equation = input("please enter the equation")
    bgnequation = equation
    if secondarychoice == "normal":
        equationsplit = re.split('([+-/])',equation)
        differential(equationsplit)
        print(bgnequation," == ",equationsplit)
    elif secondarychoice == "chain":
        equationchain = chain(equation)
        print(bgnequation ," == ",equationchain)
    elif secondarychoice == "quotient":
        equationquotient = quotient(equation)
        print(bgnequation ," == ",equationquotient)
    elif secondarychoice == "product":
        equationproduct = product(equation)
        print(bgnequation ," == ",equationproduct)
elif choice == "integral":
    secondarychoice = input("normal,substituion")
    print("please use y for + and u for - and d for / for multiple variables in brackets, only for use when using normal")
    equation = input("please enter the equation")
    bgnequation = equation
    if secondarychoice == "normal":
        equationsplit = re.split('([+-])',equation)
        integral(equationsplit)
        print(bgnequation," == ",equationsplit)
    elif secondarychoice == "substituion":
        equationsub = substituion(equation)
        print(bgnequation," == ",equationsub)
    elif secondarychoice == "reversechain":
        equationrevchain = reversechain(equation)
        print(bgnequation," == ",equationrevchain)
    elif secondarychoice == "parts":
        equationparts = parts(equation)
        print(bgnequation," == ",equationparts)
        
input('Press ENTER to exit') 



