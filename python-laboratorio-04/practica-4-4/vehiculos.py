# vehiculos.py
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje


if __name__ == "__main__":
    moto1 = Motocicleta("Yamaha", "MT-03", "321cc")
    moto2 = Motocicleta("Honda", "CB500F", "471cc")

    print(f"Moto 1 - Marca: {moto1.marca}, Modelo: {moto1.modelo}, Cilindraje: {moto1.cilindraje}")
    print(f"Moto 2 - Marca: {moto2.marca}, Modelo: {moto2.modelo}, Cilindraje: {moto2.cilindraje}")