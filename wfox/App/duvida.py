

class Duv:
    def a(self):

        a1 = input("Valor de a")
        a2 = input("valro de b")
        dev2 = int(a1) + int(a2)
        return dev2

    def b(self):
        a4 = input("Valor de a")
        a5 = input("Valor de a")
        dev3 = int(a4) - int(a5)
        return dev3


class Duv2:
    def a2(self):

        du = Duv()
        dev = du.a()
        devb = du.b()

        print(dev)
        print(devb)

        total = (dev * devb)

        return total


d1 = Duv2()
dr = d1.a2()
print(dr)
