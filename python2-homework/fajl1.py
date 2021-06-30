# Beolvassunk az adat fájlból, és a sortörést eltávolítva, majd szóközt beíktatva egy sorba kiírjuk

with open("adat.txt", "r") as f:
    for sor in f:
        print(sor.strip() + ' ', end='')

f.close()
