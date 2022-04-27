x = "cos","cosec"
xinit = 0
print(x)
while xinit < 3:
    if x[xinit] == "cos":
        print(x[xinit])
        print("cos")
        xinit = xinit + 1
    elif x[xinit] == "cosec":
        print(x[xinit])
        print("cosec")
        xinit = xinit + 1    
    else:
        print("done")

