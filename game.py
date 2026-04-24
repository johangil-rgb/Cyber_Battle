# =========================
# BATALLA DE ACERO 3000
# =========================

import time
import random

# Clase base Robot
class Robot:

    def __init__(self, nombre, bateria, escudo):
        self.__Nombre = nombre
        self.__Bateria = bateria
        self.__Escudo = escudo

    def getNombre(self):
        return self.__Nombre

    def getBateria(self):
        return self.__Bateria

    def setBateria(self, bateria):
        self.__Bateria = bateria

    def getEscudo(self):
        return self.__Escudo

    def setEscudo(self, escudo):
        self.__Escudo = escudo

    def mostrarEstado(self):
        print("\n===== ESTADO DEL ROBOT =====")
        print("Nombre:", self.__Nombre)
        print("Batería:", self.__Bateria)
        print("Escudo:", self.__Escudo)


# =========================
# Clase RobotAtaque
# =========================

class RobotAtaque(Robot):

    def atacar(self, objetivo):
        if self.getBateria() >= 10:
            daño = random.randint(15, 25)
            objetivo.setEscudo(objetivo.getEscudo() - daño)
            self.setBateria(self.getBateria() - 10)

            if objetivo.getEscudo() < 0:
                objetivo.setEscudo(0)

            print(f"\n⚡ {self.getNombre()} atacó a {objetivo.getNombre()} y causó {daño} puntos")
        else:
            print(f"\n{self.getNombre()} no tiene batería suficiente")


# =========================
# Clase RobotDefensa
# =========================

class RobotDefensa(Robot):

    def recargar(self):
        if self.getBateria() >= 5:
            aumento = random.randint(10, 20)
            self.setEscudo(self.getEscudo() + aumento)
            self.setBateria(self.getBateria() - 5)

            print(f"\n🔋 {self.getNombre()} recargó {aumento} puntos de escudo")
        else:
            print(f"\n{self.getNombre()} no tiene batería suficiente")


# =========================
# Método principal
# =========================

def main():

    ataque = RobotAtaque("Destructor-X", 60, 100)
    defensa = RobotDefensa("Guardian-Z", 60, 100)

    print("===== BATALLA AUTOMÁTICA =====")

    while ataque.getBateria() > 0 and defensa.getEscudo() > 0:

        ataque.atacar(defensa)
        time.sleep(1)

        if defensa.getEscudo() > 0:
            defensa.recargar()
            time.sleep(1)

        ataque.mostrarEstado()
        defensa.mostrarEstado()
        time.sleep(1)

    print("\n===== RESULTADO FINAL =====")

    if defensa.getEscudo() == 0:
        print(f"🏆 {ataque.getNombre()} ha ganado la batalla")
    else:
        print(f"🛡️ {defensa.getNombre()} resistió la batalla")


if __name__ == "__main__":
    main()