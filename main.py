print("Hello! i am Pytagora, and me is here to help you with Pythagorean theorem. To calculate the hypotenuse, press 1, to calculate a cathetus press 2, and to exit, press 3")

p = input (' enter 1, 2 or 3 ')

i = float(p)

if i == 1:
    print("OK! type here the number of the first cathetus ")
    a = input('type the first cathetus ')
    FC = float(a)

    print("OK! type here the number of the second cathetus ")
    b = input (' type the second cathetus ')
    SC = float(b)

    FC2 = FC * FC
    SC2 = SC * SC

    C2 = FC2 + SC2

    C1 = C2**(1/2)

    C = str(C1)

    print("the number of your hypotenuse is " + C)
elif i == 2:
    print("OK! type here the number of one cathetus ")
    CA = input('type one of the cathetus ')
    OC = float(CA)

    print("OK! type here the number of the hypotenuse ")
    H = input (' type the hypotenuse ')
    HY = float(H)

    CA1 = OC * OC
    H1 = HY * HY

    R1 = H1 - CA1

    R2 = R1**(1/2)

    R = str(R2)

    print("the number of the missing cathetus is " + R)

elif i == 3:
    print("Bye!")
    exit()

else:
    print("the number is invalid, please try again and type 1 or 2 or 3")