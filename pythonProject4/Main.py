class Promin:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Це {self.name} випромінювання."

class Radio(Promin):
    def __repr__(self):
        return super().__repr__() + " Радіо."

class Zvuk(Promin):
    def __repr__(self):
        return super().__repr__() + " Звук."

class Vidimi(Promin):
    def __repr__(self):
        return super().__repr__() + " Видиме."

class InfraChervoni(Promin):
    def __repr__(self):
        return super().__repr__() + " Інфрачервоне."

class Ultrafioletov(Promin):
    def __repr__(self):
        return super().__repr__() + " Ультрафіолетове."

class Gamma(Promin):
    def __repr__(self):
        return super().__repr__() + " Гамма."

class Rentgen(Promin):
    def __repr__(self):
        return super().__repr__() + " Рентгенівське."

def print_promin(promin):
    print(promin)

lamp = Vidimi("Лампочка")
radia = Radio("Рація")

print_promin(lamp)
print_promin(radia)
