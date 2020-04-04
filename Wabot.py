from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer
import time
class wabot:
	def __init__(self, nome_bot, name_list):
		self.bot = ChatBot(nome_bot)
		self.trainer = ListTrainer(self.bot)
		file = open(name_list, 'r').readlines()
		self.trainer.train(file)
		self.options = webdriver.ChromeOptions()
		self.options.add_argument("user-data-dir=/home/nielies/.config/google-chrome")
		self.driver = webdriver.Chrome(executable_path=r'./chromedriver', chrome_options=self.options)
		
	def Start(self, nome_contato):
		self.driver.get('https://web.whatsapp.com/')
		self.driver.implicitly_wait(20)
		self.pesquisa = self.driver.find_element_by_class_name('_3F6QL')
		print(self.pesquisa)
		self.pesquisa.click()
		self.pesquisa.send_keys(nome_contato)
		time.sleep(2)
		print(nome_contato)
		self.contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome_contato))
		self.contato.click()
		time.sleep(2)
	
	def Saudacao(self, frase_inicial):
		self.chat = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
		self.chat.send_keys(frase_inicial)
		self.chat.send_keys('\n')

	def Escutar(self):
		post = self.driver.find_elements_by_class_name('_3_7SH')
		print(post)
		ultimo = len(post) - 1
		print(ultimo)
		print(type(post))
		print(type(ultimo))
		texto = post[ultimo].find_element_by_css_selector('span.selectable-text').text
		return texto

	def Responder(self, ultima_resposta):
		response = self.bot.get_response(ultima_resposta)
		response = str(response)
		self.chat.send_keys(response)
		self.chat.send_keys('\n')