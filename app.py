import time
from os import getenv
from sys import argv, exit
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv
import pyautogui
from loguru import logger

@logger.catch
class SigaaBot:

    def __init__(self):
        #credenciais
        load_dotenv()
        try:
            logger.debug(argv[1])
            self.command = argv[1]
        except IndexError as e:
            logger.debug(e)
            logger.debug("Passe um ano letivo da UFPA.")
            exit()
        self.user = getenv('SIGAA_USER')
        self.passw = getenv('SIGAA_PASS')
        #option = Options()
        #option.headless = True
        # executable_path is to the webdriver locate the binary of the driver
        self.driver = webdriver.Firefox(executable_path='/home/italo/Documents/python_projects/sigaa_bot/geckodriver')

    def sigaa(self):
        self.driver.get('https://sigaa.ufpa.br/sigaa/verTelaLogin.do;jsessionid=6EC32AADFAC73E4050E1CCDC6BAB805C.bacaba2')
        time.sleep(5)
        campo_user = self.driver.find_element_by_name("user.login")
        campo_user.click()
        campo_user.send_keys(self.user)
        campo_passw = self.driver.find_element_by_name("user.senha")
        campo_passw.click()
        campo_passw.send_keys(self.passw)
        botao_entrar = self.driver.find_element_by_xpath("//input[@type='submit']")
        botao_entrar.click()
        periodo = self.driver.find_element_by_partial_link_text(self.command)
        periodo.click()
        time.sleep(5)
        discente = self.driver.find_element_by_partial_link_text("Discente")
        discente.click()
        logger.debug("Success!!")

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


robot = SigaaBot()
robot.sigaa()
#falta resolver o problema do fechamento automatico do chrome, nos breakpoints acima
#e como apertar os botões imprimir acima