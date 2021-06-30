# Megnyitjuk az eredeti fájl és az új fájlt is, végig iterálunk a szövegen és közben beleírjuk az új fájlba.

with open("adat.txt", "r") as f:
    with open("adat_new5.txt", "w") as nf:
        for sor in f:
            nf.write(sor)
    nf.close()
f.close()
