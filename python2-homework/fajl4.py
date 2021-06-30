# Megnyitjuk az adat fájlt, végigiteráljuk, és a sorvéget levágva egy lista változóba írjuk.
fajl_list = []
with open("adat.txt", "r") as f:
    for sor in f:
        fajl_list.append(sor.strip())
f.close()

# Megnyijuk az új fájlt, a változón végigiterálunk és minden szó után sortörést berakva kiírjuk az új fájlba.
with open("adat_new4.txt", "w") as nf:
    for nsor in fajl_list:
        nf.write(nsor + '\n')
nf.close()
