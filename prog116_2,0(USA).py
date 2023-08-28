print("Which system do you want?")
print("Enter 1 for calculator")
print("")
print("Enter 2 to play a number guessing game")
print("")

e = float(input(""))

if e == 1:
    print("CALCULATOR")
    print(" ")
    while True:
        a = float(input("Enter the first number: "))
        if a == 0:
            print("infinite sum: to exit type 0")
            tu = []
            while True:
                wad = float(input("number: "))
                print("")
                if wad != 0:
                    tu.append(wad)
                    sla = sum(tu)
                    print(sla)
                else:
                    break
        bb = float(input("Enter the second number: "))
        c = input("Do you want a third number? ")
        if c.lower() == "yes":
            cc = float(input("Enter the third number: "))
            print("ok")
            print(" ")
            print("Enter the operation you want to do")
            print(" ")
            print("plus, minus or multiplication")
            print(" ")
            b = input("")
            print(" ")
            beb = a + bb + cc
            be = a - bb - cc
            bcb = a * bb * cc
            f = a ** bb
            if b.lower() == "plus" or b == "+":
                print(beb)
            elif b.lower() == "minus" or b == "-":
                print(be)
            else:
                print(bcb)
        else:
            print("ok")
            print(" ")
            print("Enter the operation you want to do:")
            print(" ")
            print("plus, minus, multiplication, division, power or percentage?")
            print(" ")
            aa = input("")
            e = a + bb
            ee = a - bb
            eee = a / bb
            eeee = a * bb
            eeeee = a * bb / 100
            f = a ** bb
            if aa.lower() == "plus" or aa == "+":
                print(e)
            elif aa.lower() == "minus" or aa == "-":
                print(ee)
            elif aa.lower() == "multiplication" or aa.lower() == "mult" or aa == "x":
                print(eeee)
            elif aa.lower() == "division" or aa.lower() == "div" or aa == "÷":
                print(eee)
            elif aa.lower() == "percentage" or aa.lower() == "per" or aa == "%":
                print(eeeee)
            elif aa.lower() == "power" or aa.lower() == "pot":
                print(f)
            i = input("Do you want to calculate more? ")
            if i.lower() == "no":
                print("Ok")
                print("Coming out of the calculator...")
                break

else:
    print("NUMBER GUESSER")
    print("")
    import random
    print("Do you want to customize the game or leave the default?")
    print("(default is 0 to 100)")
    pootis = input("")
    if pootis.lower() == "default" or pootis.lower() == "leave default":
        print("ok")
        print("")
        pootisr = random.randint(0, 100)
        while True:
            r = float(input(""))
            if r > pootisr:
                print("You passed")
                print(".")
            elif r < pootisr:
                print("You passed")
                print(".")
            else:
                    print("You win")
                    break
    else:
        print("ok")
        er = float(input("enter the number that starts the count:  "))
        err = float(input("enter the number that starts the count:  "))
        pootisrr = random.randint(er, err)
        while True:
            r = float(input(""))
            if r > pootisrr:
                	print("You passed")
            elif r < pootisrr:
                	print("You passed")
            else:
                    print("You win")
                    break
