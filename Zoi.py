import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import datetime
import webbrowser
import pymysql
import os

name = 'zoe'

listener=sr.Recognizer()

engine=pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
	engine.say(text)
	engine.runAndWait()

def listen(text):
	try:
		with sr.Microphone() as source:
			print(text)
			voice = listener.listen(source)
			rec = listener.recognize_google(voice, language='es-ES')
			rec = rec.lower()

			if name in rec:
				rec = rec.replace(name, '')
				print('Usted dijo: '+ rec)

	except:
		pass


	return rec

def basic_functions():
	#------------Musica y videos en yt---------------------------------

	rec = listen("Esperando orden...")

	if 'reproduce' in rec:

		music = rec.replace('reproduce','')
		talk('Reproduciendo ' + music)
		pywhatkit.playonyt(music)


	#------------HORA--------------------------------------------

	elif 'dime la hora actual' in rec:
		hora = datetime.datetime.now().strftime('%I:%M %p')
		talk("Son las " + hora)

	#------------FECHA--------------------------------------------

	elif 'dime la fecha actual' in rec:
		fecha = datetime.datetime.now().strftime('%d/%m/%Y')
		talk("La fecha es " + fecha)


	#------------BUSCAR EN GOOGLE

	elif 'busca' in rec:
		order = rec.replace('busca','')
		talk('Buscando' + order)
		pywhatkit.search(order)

	elif 'dime un chiste' in rec:
		order = rec.replace('dime un chiste', '')
		joke = pyjokes.get_joke('es')
		talk(joke)

#----------------------FUNCIoNES PRO OwO--------------------------------------

def advanced_funtions():

	rec = listen('Esperando orden')

	#--------------APLICACIONES .exe-------------------------------

	if 'ejecuta' in rec:
		order = rec.replace('ejecuta', '')
		talk('Ejecutando...' + order)

		app = order + '.exe'
		os.system(app)

		#-----------------CREAR DIRECTORIO-----------------
	elif 'crea el directorio' in rec:
		home = "C:\\Users\\Usuario.DESKTOP-FSUFRIM\\Desktop\\Asistente\\ "
		order = rec.replace('crea el directorio','')

		if os.path.exists(order):
			talk('Existe un archivo con este nombre')

		else:
			mrk = os.mkdir(home+order)
			talk('El directorio fue creado con exito')

		#---------------ELIMINAR DIRECTORIO.-------------

	elif 'elimina el directorio' in rec:
		order = rec.replace('elimina el directorio','')
		if os.path.exists(order):
			talk('El directorio se elimino correctamente')
			rd = os.rmdir(order)
		else:
			talk('El directorio no existe')

	#-------------ARCHIVOS TXT----------------------

	elif 'crea el archivo' in rec:
		order = rec.replace('crea el archivo','')

		order = order + '.txt'
		if os.path.exists(order):
			talk("Este nombre de archivo ya existe")

		else:
			archivo = open(order,"w")
			archivo.close()
			talk("El archivo se creo con exito")


	#--------------ELIMINAR TXT-----------------

	elif 'elimina el archivo' in rec:
		order = rec.replace('borra el archivo', '')
		order = order + '.txt'

		if os.path.exists(order):
			os.remove(order)
		else:
			talk('El archivo no existe')


	#------------------REDIRIGIR A PAGINAS WEB--------------------


	elif 'inicia' in rec:
		webbrowser.open('https://sima.unicartagena.edu.co/login/index.php')

	else:
		talk('No te entendi')
		advanced_funtions()


#Indicador

if __name__=='__main__':
	advanced_funtions()
	#basic_functions()