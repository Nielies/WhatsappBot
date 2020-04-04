from Wabot import wabot
import re

bot = wabot('Nielies', 'edited2.txt')
bot.Start('Vinicim')
bot.Saudacao('Olá, eu finalmente estou funcionando, utilize & antes da mensagem para falar comigo!')
ultimo_texto = ""

while True:
	texto = bot.Escutar()
	if texto != ultimo_texto and re.match(r'^&', texto):
		ultimo_texto = texto
		texto = texto.replace('&', "")
		texto = texto.lower()
		bot_response = bot.Responder(texto)
	else:
		nothing = 'none' 