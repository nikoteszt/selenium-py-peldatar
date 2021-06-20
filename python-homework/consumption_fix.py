orszFogy = 7  # Fogyasztás országúton liter
varFogy = 9  # Fogyasztás városban liter
orszUt = 170  # Órszágúti szakasz hossza km
varUt = 35  # Városi útszakasz hossza km
benzin = 350  # Benzin ára Ft

# Auto fogyasztása csak oda
autoFogy = (orszUt * orszFogy + varUt * varFogy) / 100
# Auto fogyasztása oda-vissza
autoFogyReturn = 2 * autoFogy

# A teljes út ára
szummaKoltseg = benzin * autoFogyReturn
print("A fogyasztás oda-vissza: ", autoFogyReturn, " liter")
print("Az utazás költsége: ", szummaKoltseg, " Forint")
