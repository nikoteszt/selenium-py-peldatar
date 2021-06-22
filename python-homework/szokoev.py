def leap_year():

    if age % 400 != 0:
        if age % 100 == 0:
            return False
        elif age % 4 == 0:
            return True
        else:
            return False
    else:
        return True


age = int(input("Írj be egy évszámot : "))

answer = leap_year()

if answer:
    print(age, "Szökőév")
else:
    print(age, "Nem szökőév")
