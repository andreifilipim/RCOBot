from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AbrindoRCO:
    def __init__(self):
        self.username = None
        self.password = None
        self.navegador = self.iniciar_navegador()
        self.rco_url = "https://auth-cs.identidadedigital.pr.gov.br/centralautenticacao/login.html?response_type=token&client_id=f340f1b1f65b6df5b5e3f94d95b11daf&redirect_uri=https%3A%2F%2Frco.paas.pr.gov.br&scope=emgpr.mobile%20emgpr.v1.ocorrencia.post&state=null&urlCert=https://certauth-cs.identidadedigital.pr.gov.br&dnsCidadao=https://cidadao-cs.identidadedigital.pr.gov.br/centralcidadao&loginPadrao=btnCentral&labelCentral=CPF,E-Mail&modulosDeAutenticacao=btnSms,btnCpf,btnEmail,btnCentral&urlLogo=https%3A%2F%2Fwww.registrodeclasse.seed.pr.gov.br%2Frcdig%2Fimages%2Flogo_sistema.png&acesso=2060&tokenFormat=jwt&exibirLinkAutoCadastro=true&exibirLinkRecuperarSenha=true&exibirLinkAutoCadastroCertificado=false&captcha=false"

    def iniciar_navegador(self):
        # Iniciando o chrome
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("detach", True) # Tratando problema do navegador fechando sozinho

        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico, options=chrome_options)

        return navegador

    def acessar_site(self):
        self.navegador.get(self.rco_url)

    def fazer_login(self):
        botaoLogin = self.navegador.find_element('xpath', '//*[@id="btnCentral"]')
        botaoLogin.click()
        time.sleep(2)  # Aguardar carregar a nova página
        
        # Preenchendo os dados de login e acessando
        campo_username = self.navegador.find_element('xpath', '//*[@id="attribute_central"]')
        campo_password = self.navegador.find_element('xpath', '//*[@id="password"]')
        botao_entrar = self.navegador.find_element('xpath', '//*[@id="btn-central-acessar"]')
        
        with open("login.txt", "r") as arq:
            self.username = arq.readline().strip()
            self.password = arq.read()
            
        campo_username.send_keys(self.username)
        campo_password.send_keys(self.password)
        botao_entrar.click()

    def selecionar_livro(self):
        # Rede estadual, selecionar livro na esquerda
        botao_RedeEstadual = self.navegador.find_element('xpath', '//*[@id="__BVID__23"]/div/p[1]/div/label')
        botao_RedeEstadual.click()
        time.sleep(2)
        
        botao_SelecionarLivro = self.navegador.find_element('xpath' ,'//*[@id="sidebar"]/div/div/div/div[2]/header/button/span')
        botao_SelecionarLivro.click()
        time.sleep(2)

    def copiar_titulo(self):
        # (escolher o trimestre especifico da série específica),
        # ir em planejamento na esquerda e copiar o 'Título' e o link em Slides/Encaminhamentos
        # Isso depende de como a estrutura da página está definida
        botao_planejamento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div/div/div/div[2]/div/p/ul/li[4]/a'))
        )
        botao_planejamento.click()
        

    def colar_no_classroom(self):
        # Após isso, colar no classroom
        pass
    
        