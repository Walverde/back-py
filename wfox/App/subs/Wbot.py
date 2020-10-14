from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Wbot():
    def __init__(self):

        # instanciando o WebDrive
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')

        # Usado o Drive baixado.
        self.navegador = webdriver.Chrome(
            executable_path=r"chromedriver.exe")

        # Informando site alvo
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

        # escolhendo categoria ESPORTES
        time.sleep(10)
        cat = self.navegador.find_element_by_xpath(
            f"//a[@id='category_item-6000']")
        # time.sleep(3)
        cat.click()
        time.sleep(1)

        # escolhendo sub-categoria Ciclismo.
        subcat = self.navegador.find_element_by_xpath(
            f"//a[@id='category_item-6060']")
        # time.sleep(3)
        subcat.click()
        time.sleep(1)

        # Clicando no titulo.
        titulo = self.navegador.find_element_by_xpath(
            f"//input[@id='input_subject']")
        # time.sleep(3)
        titulo.click()
        time.sleep(1)

        # nova aba

        # else:

    def new_tab(self):

        newtab = self.navegador.find_element_by_tag_name("body")
        # newtab.send_keys(Keys.CONTROL + 't')
        # print("Current Page Title is : %s" % newtab.title)
        newtab.execute_script("window.open('');")

        #     print("Fim do loop")


w = Wbot()
w.new_tab()
