from selenium import webdriver
from decouple import config
import pyautogui
import time

class SigaaBot:
    def __init__(self):
        #credenciais
        self.user = config('USUARIO')
        self.passw = config('PASS')
        self.eixoX = 512
        self.eixoY_ensino = 179
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        options.add_argument('start-maximized')
        #as duas linhas abaixo removem a msgm de chrome sendo testado por software de automacao
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver', options=options)

    def abrir_sigaa(self):
        self.driver.get('https://sigaa.ufpa.br/sigaa/verTelaLogin.do;jsessionid=6EC32AADFAC73E4050E1CCDC6BAB805C.bacaba2')
        time.sleep(2)
        campo_user = self.driver.find_element_by_name("user.login")
        campo_user.click()
        campo_user.send_keys(self.user)
        campo_passw = self.driver.find_element_by_name("user.senha")
        campo_passw.click()
        campo_passw.send_keys(self.passw)
        botao_entrar = self.driver.find_element_by_xpath("//input[@type='submit']")
        botao_entrar.click()
    
    def selecionar_periodo_discente(self):
        periodo = self.driver.find_element_by_partial_link_text("2021-1")
        periodo.click()
        time.sleep(2)
        discente = self.driver.find_element_by_partial_link_text("Discente")
        discente.click()

    def ver_notas(self):
        pyautogui.moveTo(self.eixoX, self.eixoY_ensino) #menu ensino
        pyautogui.moveTo(self.eixoX, 199)
        pyautogui.click()
        time.sleep(2)
        pyautogui.scroll(-20, x=512, y=900)
        time.sleep(8)

    def emitir_atestado(self):
        pyautogui.moveTo(self.eixoX, self.eixoY_ensino) #menu ensino
        pyautogui.moveTo(self.eixoX, 244)
        pyautogui.click()
        time.sleep(10)

    def emitir_historico(self):
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

    #fazer essa porra funcionar
    def imprimir(self):
        imprime = self.driver.find_element_by_partial_link_text("Imprimir")
        imprime.click()
        time.sleep(15)

    def voltar(self):
        voltar = self.driver.find_element_by_partial_link_text("Voltar")
        voltar.click()
        time.sleep(5)

    def sair(self):
        sair = self.driver.find_element_by_partial_link_text("SAIR")
        sair.click()
        time.sleep(5)
        pyautogui.hotkey('alt', 'f4')

robot = SigaaBot()
robot.abrir_sigaa()
robot.selecionar_periodo_discente()
robot.ver_notas()
robot.voltar()
robot.emitir_atestado()
#robot.voltar()
#robot.emitir_historico()
#robot.emitir_declaracao_vinculo()
#robot.sair()

#falta resolver o problema do fechamento automatico do chrome, nos breakpoints acima
#e como apertar os botões imprimir acima