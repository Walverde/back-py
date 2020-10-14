from selenium webdriver 
import time

class bot:
    def __init__(self):
        self.messagem="Bsodaijsdaoajs"
        self.grupos=["ndad",""] 
        options = webdriver.ChromeOptions()
        options.add_argument ('lang=pr-br')
        self.drive = webdriver.chrome(executable_path=r'.chromedrive.exe')

    def Enviar(self):   
        #Endereco do grupo no whats Web
        #<span dir="auto" title="ndad" class="_19RFN _1ovWX _F7Vk">ndad</span>
        #<div tabindex="-1" class="_13mgZ">
        #<span data-icon="send" class="">
        self.driver.get(https:https://web.whatsapp.com/)
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_13mgZ')
            time.sleep(3)
            grupo.click()
            chat_box.send_keys(self.messagem)
            self.drive.find_element_by_xpath('//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(3)

bot = whatsbot()
bot.enviarmessagens()