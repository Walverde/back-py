class Menu ():

    def __init__(self):
        print('''
        ╔════════════════════╗
        ║      Bem Vindo     ║
        ║   Webot - Albatroz ║
        ║          :D        ║
        ╚════════════════════╝''')

    def menu(self):

        n1 = 0
        while n1 != 5:
            print('''
            [1] Bike
            [2] Auto
            [3] Albatroz
            [4] Novo
            [5] Sair
                  ''')
            n1 = int(input("[Escolha uma Vertente: ]"))

            if n1 == 1:
                # Aqui vai entrar a função
                print("Vertente: Bike. / Email:{}".format(user))
                bot = Wbot()
                bot.login(user, passw)
                if cat == "bike":
                    bot.cat_bike(vezes)

            elif n1 == 2:
                print("Escolhou a opão 2")
            elif n1 == 3:
                print("Escolhou a opão 3")
            elif n1 == 4:
                print("Escolhou a opão 4")
            else:
                print("Opção invalida. Tente novamente")
            print('=-=' * 10)
        print("FIM")
