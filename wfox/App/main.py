from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from os.path import dirname, realpath
import json

# ---------------------------Navegador------------------------------------


class Int ():

    # input para texto
    def string(self, ss):
        s1 = input(ss)
        return s1

    # input para numero
    def number(self, num):
        n1 = int(input(num))
        return n1


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


class Wbot():
    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')

        self.navegador = webdriver.Chrome(
            executable_path=r"chromedriver.exe")
        self.navegador.get("https://www2.olx.com.br/desapega")

    def login(self, usuario, senha):

        dmail = self.navegador.find_element_by_xpath(f"//input[@type='email']")
        # time.sleep(3)
        dmail.click()
        time.sleep(1)
        dmail.send_keys(usuario)

        dpass = self.navegador.find_element_by_xpath(
            f"//input[@type='password']")
        # time.sleep(3)
        dpass.click()
        time.sleep(1)
        dpass.send_keys(senha)

        dbpass = self.navegador.find_element_by_xpath(
            f"//button[@class='sc-kGXeez dXzFBw']")
        # time.sleep(3)
        dbpass.click()
        time.sleep(1)

    # No futuro, vai ter outro metodos, para cada categoria
    # def cat_bike(self, vezes: int, vx: int = 0):
    def cat_bike(self):

        # if vx < vezes:

        #     vx = + 1

        # escolhendo categoria
        time.sleep(10)
        cat = self.navegador.find_element_by_xpath(
            f"//a[@id='category_item-6000']")
        # time.sleep(3)
        cat.click()
        time.sleep(1)

        subcat = self.navegador.find_element_by_xpath(
            f"//a[@id='category_item-6060']")
        # time.sleep(3)
        subcat.click()
        time.sleep(1)

        titulo = self.navegador.find_element_by_xpath(
            f"//input[@id='input_subject']")
        # time.sleep(3)
        titulo.click()
        time.sleep(1)

        # nova aba

        # else:

        #     print("Fim do loop")


class Jackson():

    # def __init__(self):
    #     self.path = dirname(realpath(__file__))

    # path_data_json = self.path + file
    # if not isfile(path_data_json):
    #     with open(path_data_json, 'w') as f:
    #         dump(data, f, indent=2, separators=(',', ':'))
    #     return True
    # else:
    #     return False

    def create_js(self, dados):  # Ok
        # dados = + dados
        with open('Logins.json', 'w', encoding='utf8', ) as f:
            json.dump(dados, f, ensure_ascii=False, indent=2,
                      sort_keys=True, separators=(',', ':'))

    def read_js(self):  # Ok
        # dados = + dados
        with open('Logins.json', 'r', encoding='utf8', ) as f:
            self.data = json.load(f)

            return self.data

    def update_js(self, do_update=False):

        with open("Logins.json", 'r', encoding='utf8') as json_file:
            # Carregamento do arquivo Json, para atualização.
            dados = json.load(json_file)
            # Elemento, contido no arquivo, a ser acrescido parametro. ID: 01
            temp = dados['classes']  # Original
            # dados['classes'] = []

            print(temp)
            # campo, a ser acrecido ao elemento do arqvuivo json
            # Adcionando campos, ao elemento importado (ID: 01)
            # do_update = {
            #     "auto": {"user": "testesdaadasdsda", "pssw": "testsdasdasdae"}}
            do_update_json = json.dumps(do_update)
            temp.append(do_update_json)
            # Exemplo de do_update: {"dado_1": "valor 1", "dado_2": "valor 2"}

        # with open('Logins.json', 'w', encoding='utf8', ) as f:
        #     # sobrescrevendo o arquivo Json, atualizado anteriomente.
        #     json.dump(dados, f, ensure_ascii=False, indent=2,
        #               sort_keys=True, separators=(',', ':'))

        # with open('Logins.json', 'w') as f:

        #     json.dump(data, f, indent=2)  # OK


# email = input("Email:")
# classe = input("class")
# senha = input("Senha")
# novaclasse = {classe: {"user": email, "pssw": senha, }, }
data = {
    "Credenciais": {
        "Gamer": {
            "email.1": "g.amermellok@gmail.com",
            "email.2": "ga.mermellok@gmail.com",
            "email.3": "gam.ermellok@gmail.com",
            "email.4": "gamer.mellok@gmail.com"
        },
        "senhas": {
            "s5": "5101520253035",
            "s3": "369121518",
            "s2": "2468101214"
        },
        "walgreen.melo": {
            "email.1": "sdfsddfsfsdsfd",
            "senha": "sfdsfdsfdsfdsfd"
        }
    },
    "classes": {
        "bike": {
            "pssw": "",
            "user": "walgreen.melo@gmail.com"
        }
    }
}

user = "www"
pssw = "ijoij"

update1 = {"auto": {"user": {}, "pssw": {}}

# update = json.loads({"auto": {"user": "testesdasda", "pssw": "teste"}})

update = json.loads(update1)

j = Jackson()
j.update_js(update)
# j.create_js(data)
# j.read_js()
# print(j.read_js()['classes'])


# navegador.quit()

# Execução selecionada do codigo----------------------------------------------------------------------------------------------------------------------


# ini = Int()
# user = ini.string("Email: ")
# passw = ini.string("Senha: ")
# cat = ini.string("Escolha a categoria: ")
# vezes = ini.number("Quantidade de abas: ")


# bot = Wbot()
# bot.login(user, passw)
# if cat == "bike":
#     bot.cat_bike(vezes)


# test

# ini = Menu()
# ini.menu()

# if __name__ == '__main__':
#     j = Jackson()
#     j.create_js('/data/data.json')

# user = "gamer.mellok@gmail.com"
# passw = "5101520253035"
# cat = "bike"
# # vezes = 1


# bot = Wbot()
# bot.login(user, passw)

# if cat == "bike":
#     bot.cat_bike()
