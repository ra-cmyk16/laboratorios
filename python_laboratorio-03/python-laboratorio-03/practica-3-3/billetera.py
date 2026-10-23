class Billetera:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def registrar_ingreso(self, monto):
        if monto <= 0:
            return False

        self.saldo += monto
        return True

    def registrar_gasto(self, monto):
        if monto <= 0:
            return False

        if monto > self.saldo:
            return False

        self.saldo -= monto
        return True

    def consultar_saldo(self):
        return self.saldo


billetera_ana = Billetera("Ana")
billetera_luis = Billetera("Luis")

print("Ingreso de Ana 50000:", billetera_ana.registrar_ingreso(50000))
print("Ingreso de Luis 20000:", billetera_luis.registrar_ingreso(20000))
print("Gasto de Ana 15000:", billetera_ana.registrar_gasto(15000))
print("Gasto de Luis 30000:", billetera_luis.registrar_gasto(30000))
print("Ingreso de Ana -100:", billetera_ana.registrar_ingreso(-100))
print("Gasto de Ana 0:", billetera_ana.registrar_gasto(0))

print()
print("Saldo de", billetera_ana.titular + ":", billetera_ana.consultar_saldo())
print("Saldo de", billetera_luis.titular + ":", billetera_luis.consultar_saldo())
