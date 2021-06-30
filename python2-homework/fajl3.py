# Az adat fájból egy lista változóba írjuk az adatokat, sortörést eltávolítva
fajl_list = []
with open("adat.txt", "r") as f:
    for sor in f:
        fajl_list.append(sor.strip())
f.close()

# A lista változóból egy új fájlba írjuk az adatokat, szöveggé összefüzve.
with open("adat_new3.txt", "w") as nf:
    nf.write(' '.join(fajl_list))
nf.close()
