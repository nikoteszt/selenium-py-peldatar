age = int(input("Kérem adja meg az életkorát :"))
drink = str(input("Kérem adja meg milyen italt kér :"))

if drink != "sör" and drink != "kóla":
    print("Csak sört vagy kólát tudunk adni.")
else:
    if age < 18 and drink == "sör":
        print("Kiskorúnak nem szolgálhatunk ki sört!")
    elif age > 60 and drink == "kóla":
        print("A koffein megemelheti a vérnyomását, nem tanácsos kólát innia.")
    else:
        print("Parancsoljon a kért ", drink, "!")
