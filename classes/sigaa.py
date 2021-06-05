import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pyautogui
from loguru import logger
from .user import User


# criar uma arvore de elifs para pegar comando diretos no script e rodar só os métodos correspondentes
# talvez seja uma boa usar um arquivo de python para rodar o codigo e deixar esse com a classe
# criar um arquivo de log apena para logs de warning e errors
# botar ele pra rodar com um shell script através do nautilus
# o caminho para o interpretador da venv poetry é esse: "/home/italo/.cache/pypoetry/virtualenvs/ufpa-sigaa-bot-s4Id-V6p-py3.8/bin/python3"

class SigaaBot:
    """
    The class representing the bot that will interact with SIGAA site
    """
    def __init__(self):
        # the commented option below are used to test this code without open the browser
        option = Options()
        option.headless = True
        # executable_path is to the webdriver locate (absolute path) the binary of the driver
        self.driver = webdriver.Firefox(options=option) #when test, options=option
        self.user = User()

    def sigaa_user(self, name:str, password:str, year:str):
        logger.debug("We're at sigaa_user method")
        self.user.name = name
        self.user.password = password
        self.user.year = year

    def sigaa(self):
        self.driver.get('https://sigaa.ufpa.br/sigaa/verTelaLogin.do;jsessionid=6EC32AADFAC73E4050E1CCDC6BAB805C.bacaba2')
        time.sleep(5)
        logger.debug("We're at the homepage.")
        campo_user = self.driver.find_element_by_name("user.login")
        campo_user.click()
        campo_user.send_keys(self.user.name)
        campo_passw = self.driver.find_element_by_name("user.senha")
        campo_passw.click()
        campo_passw.send_keys(self.user.password)
        botao_entrar = self.driver.find_element_by_xpath("//input[@type='submit']")
        botao_entrar.click()
        logger.debug("Now on school term page.")
        periodo = self.driver.find_element_by_partial_link_text(self.user.year)
        periodo.click()
        time.sleep(5)
        logger.debug("'Discent' page.")
        discente = self.driver.find_element_by_partial_link_text("Discente")
        discente.click()
        logger.debug("Success!!")

# investigar o site do sigaa para saber se o menu dropdown é onhover ou onclick ou both
    def ver_notas(self):
        pyautogui.moveTo(self.eixoX, self.eixoY_ensino) #menu ensino
        pyautogui.moveTo(self.eixoX, 199)
        pyautogui.click()
        time.sleep(2)
        pyautogui.scroll(-20, x=512, y=900)
        time.sleep(8)

    def ver_atestado(self):
        pyautogui.moveTo(self.eixoX, self.eixoY_ensino) #menu ensino
        pyautogui.moveTo(self.eixoX, 244)
        pyautogui.click()
        time.sleep(10)

    def ver_historico(self):
        pyautogui.moveTo(self.eixoX, self.eixoY_ensino) #menu ensino
        pyautogui.moveTo(self.eixoX, 251)
        pyautogui.click()
        time.sleep(20)
        #não abre janela, logo não precisa do método voltar
    
    def emitir_declaracao_vinculo(self):
        pyautogui.moveTo(self.eixoX, self.eixoY_ensino) #menu ensino
        pyautogui.moveTo(self.eixoX, 294)
        pyautogui.click()
        time.sleep(30)
        #não abre janela, logo não precisa do método voltar
