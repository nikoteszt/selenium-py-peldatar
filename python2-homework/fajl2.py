# # Az adat fájból egy lista változóba írjuk az adatokat, sortörést eltávolítva, majd kiprinteljük szüveggé összefüzve

fajl_list = []
with open("adat.txt", "r") as f:
    for sor in f:
        fajl_list.append(sor.strip())
print(' '.join(fajl_list))
f.close()
