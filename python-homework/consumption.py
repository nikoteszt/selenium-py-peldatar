orszFogy = int(input("Fogyasztás országúton literben :"))
varFogy = int(input("Fogyasztás városban literben :"))
orszUt = int(input("Órszágúti szakasz hossza km-ben :"))
varUt = int(input("Városi útszakasz hossza km-ben :"))
benzin = int(input("Benzin ára Ft-ban :"))

# Auto fogyasztása csak oda
autoFogy = (orszUt * orszFogy + varUt * varFogy) / 100

# Auto fogyasztása oda-vissza
autoFogyReturn = 2 * autoFogy

# A teljes út ára
szummaKoltseg = benzin * autoFogyReturn
print("A fogyasztás oda-vissza: ", autoFogyReturn, " liter")
print("Az utazás költsége: ", szummaKoltseg, " Forint")
