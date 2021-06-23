a = ord('a')

for i in range(a, a+10):
    if i <= a+5:
        print(chr(i), i, chr(i + 10), i + 10, chr(i + 20), i + 20)
    else:
        print(chr(i), i, chr(i + 10), i + 10)
