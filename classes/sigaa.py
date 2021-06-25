import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pyautogui
from loguru import logger
from .user import User

class SigaaBot:

    def __init__(self):
        """
        The class that represents the bot itself which will interact directely with the SIGAA site.
        """
        # the commented `option` below are used to test this code without open the browser
        #option = Options()
        #option.headless = True
        # when test, options=option
        try:
            self.driver = webdriver.Firefox()
        except:
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.user = User()
        self.eixoX = 500
        self.eixoY_dropdown_menu = 195

    def sigaa_user(self, name:str, password:str, year:str):
        """Method to take the SIGAA credentials from the user"""
        logger.debug("We're at sigaa_user method")
        self.user.name = name
        self.user.password = password
        self.user.year = year

    def sigaa_site(self):
        """
        Method that access the site properly.
        It ends up when land in the homepage of the user.
        """
        self.driver.get('https://sigaa.ufpa.br/sigaa/verTelaLogin.do;jsessionid=6EC32AADFAC73E4050E1CCDC6BAB805C.bacaba2')
        time.sleep(5)
        logger.debug("We're at the login page.")
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
        logger.debug("We landed in the homepage successfuly!")
        
    # Methods that uses pyautogui: 

    def ver_notas(self):
        """Interact with the button `see the grades`"""
        logger.debug("See the grades method.")
        pyautogui.moveTo(x=self.eixoX, y=self.eixoY_dropdown_menu) 
        pyautogui.moveTo(x=self.eixoX, y=215)
        pyautogui.click()
        time.sleep(5)
        pyautogui.scroll(-20, x=512, y=900)
        logger.debug("Success!")

    def ver_atestado(self):
        """Interact with the button `see the certificate of enrollment`"""
        logger.debug("See the certificate of enrollment method.")
        pyautogui.moveTo(x=self.eixoX, y=self.eixoY_dropdown_menu) 
        pyautogui.moveTo(x=self.eixoX, y=257)
        pyautogui.click()
        logger.debug("Success!")

    def ver_historico(self):
        """Interact with the button `see the history`"""
        logger.debug("See the history method.")
        pyautogui.moveTo(x=self.eixoX, y=self.eixoY_dropdown_menu) 
        pyautogui.moveTo(x=self.eixoX, y=275)
        pyautogui.click()
        logger.debug("Success!")
    
    def emitir_declaracao_vinculo(self):
        """Interact with the button `see the bond statement method`"""
        logger.debug("See the bond statement method.")
        pyautogui.moveTo(x=self.eixoX, y=self.eixoY_dropdown_menu) 
        pyautogui.moveTo(x=self.eixoX, y=317)
        pyautogui.click()
        logger.debug("Success!")

    def matricula_online(self):
        """Interact with the button `Online enrollment` then with `Do enrollment`"""
        logger.debug("Online enrollment method.")
        pyautogui.moveTo(x=self.eixoX, y=self.eixoY_dropdown_menu) 
        pyautogui.moveTo(x=self.eixoX, y=388)
        pyautogui.moveTo(x=788, y=388)
        pyautogui.click()
        logger.debug("Success!")
