# Változók dekralálása
i = 1
my_list = []

# Számok bekérése, lista legyártása

while i != 0:
    number = input("Adj meg egy pozitív számot (kilépés 0-val) :")
    try:
        if float(number) < 0:
            print("Ez negatív szám, nem fogadom el!")
        elif float(number) > 0:
            my_list.append(number)
        else:
            i = 0
    except:
        print("Ez nem szám volt, SZÁMOT kérek")
    finally:
        pass

# A lista kiiratása fordított sorrendben
print(my_list[::-1])
