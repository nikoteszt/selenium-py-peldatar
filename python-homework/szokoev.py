def leap_year(x):

    if x % 400 != 0:
        if x % 100 == 0:
            return False
        elif x % 4 == 0:
            return True
        else:
            return False
    else:
        return True


age = int(input("Írj be egy évszámot : "))

answer = leap_year(age)

if answer:
    print(age, "Szökőév")
else:
    print(age, "Nem szökőév")
