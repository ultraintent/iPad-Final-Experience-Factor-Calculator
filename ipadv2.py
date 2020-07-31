import math
done=True
def ipadv2():
    # fetch price
    price=input("What's the final price? ")
    price=float(price)
    price=round(price,2)
    print("Price is $" + str(price) + ";\n")

    #fetch storage
    storage=input("What's the storage? (GB) ")
    storage=int(storage)
    storage=round(storage,0)
    print("Storage is " + str(storage) + "GB;\n")

    #fetch generation
    generation=input("What's the generation? ")
    generation=int(generation)
    generation=round(generation,0)
    print("Generation is: " + str(generation) + ";\n")

    #convert to factors
    pricefactor=price/10
    storagefactor=(math.sqrt(storage))
    generationfactor=(math.sqrt(64*generation))

    #print factors
    #print("pricefactor is " + str(pricefactor))
    #print("storagefactor is " + str(storagefactor))
    #print("generationfactor is " + str(generationfactor))


    #calculate FEF
    fef=100*(storagefactor+generationfactor)/pricefactor
    print("FEF is " + str(fef) + "!\n")

    input("Press enter to repeat\n")
    done=True
while done:
    ipadv2()


