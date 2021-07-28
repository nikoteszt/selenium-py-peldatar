import random


class MessageBox:
    def __init__(self):
        self.operations = []

    def send(self):
        self.operations.append(2)

    def receive(self):
        self.operations.append(1)

    def szamlalas(self):
        fu = 0  # fogadott üzenetek száma
        ku = 0  # küldött üzenetek száma
        fara = 30  # fogadott üzenet ára
        kara = 150  # küldött üzenet ára
        for i in self.operations:
            if i == 1:
                fu += 1
            elif i == 2:
                ku += 1
        return fu * fara + ku * kara

    def poperations(self):
        return self.operations


uzenet = MessageBox()

for _ in range(15):  # random generálunk 15 darab üzenetet
    m = random.randint(1, 2)  # 1 a fogadott, 2 a küldött üzenetet jelenti
    if m == 2:
        uzenet.send()
    else:
        uzenet.receive()

print("Küldött üzenetek fajtái: ", uzenet.poperations())
print("Üzenetek költsége :", uzenet.szamlalas(), "Ft")
