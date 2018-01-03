from random import *


def main():
	menu()

def menu():
	seleccion = input("Selecciona una opcion.\n[1] Lectura de archivo\n[2] Manual\n[3] Automatico\n[4] Salir\n")

	if seleccion == 1:
		lectura()
	elif seleccion == 2:
		manual()
	elif seleccion == 3:
		automatico()
	elif seleccion == 4:
		print "Saliendo\n"
	else:
		print "Selecciona una opcion correct\n"
		menu()

def manual():
	texto = raw_input("Ingresa una expresion con parentesis derechos e izquierdos para determinar si esta completa:")
	lista = list()
	opcion = 2
	busqueda(texto, lista,opcion)

def lectura():
	archivo = open("PruebaParentesis.txt","r+")
	texto = archivo.read()
	lista = list()
	opcion = 1
	busqueda(texto,lista,opcion)
	archivo.close()

def automatico():
	texto = ''
	lista = list()
	rango = randint(1,100)
	for i in range(rango):
		numero = randint(1,500)
		if numero%2 == 0:
			texto = texto + '('
		else:
			texto = texto + ')'
	busqueda(texto,lista,3)



def busqueda(texto, lista,opcion):
	if opcion == 1:
		archivo = open("SalidaParentesisLectura.txt","w+")
	elif opcion == 2:
		archivo = open("SalidaParentesisManual.txt","w+")
	elif opcion == 3:
		archivo = open("SalidaParentesisAutomatico.txt","w+")
	izq = 0
	der = 0
	x = 'R'
	lista = ['B']
	marca = 0
	error = 0
	print "La expresion es la siguiente:"+texto+"\n"
	archivo.write("La expresion es la siguiente:"+texto+"\n")
	for i in texto:
		if i == '(':
			if marca == 0:
				if len(lista) == 1:
					lista.insert(0,'(')
					j = 0
					for j in range(len(lista)):
						if lista[j] == 'B':
							lista.insert(j,'R')
					print "(1) - "+"".join(lista)+"\n"
					archivo.write("(1) - "+"".join(lista)+"\n")
					marca = 1
					izq = izq + 1
				else:
					j = 0
					for j in range(len(lista)):
						if lista[j] == 'B':
							lista.insert(j,'(')
							lista.insert(j+1,'R')
							print "(1) - "+"".join(lista)+"\n"
							archivo.write("(1) - "+"".join(lista)+"\n")
							break
					marca = 1
					izq = izq + 1
			else:
				j = 0
				for j in range(len(lista)):
					if lista[j] == 'R':
						lista.insert(j,'(')
						lista.insert(j+1,'R')
						print "(4) - "+"".join(lista)+"\n"
						archivo.write("(4) - "+"".join(lista)+"\n")
						break
				izq = izq + 1		
		elif i == ')':
			j = 0
			indicador = 0
			while indicador == 0:
				if lista.count('R') > 0:
					if lista[j] == 'R':
						lista.remove(x)
						lista.insert(j,')')
						indicador = 1
				else:
					indicador = 1
				j = j + 1
				if lista[j-1] == ')' and lista[j] == 'B':
					marca = 0	
			print "(3) - "+"".join(lista)+"\n"
			archivo.write("(3) - "+"".join(lista)+"\n")
			der = der + 1
		else:
			print "Caracter no reconocido, terminando el proceso\n"
			archivo.write("Caracter no reconocido, terminando el proceso\n")
			error = 1
			break
	if error == 0:
		lista.remove('B')
		print "(2) - "+"".join(lista)+"\n"
		archivo.write("(2) - "+"".join(lista)+"\n")
		if der == izq:
			print "Estan balanceados los parentesis\n"
			archivo.write("Estan balanceados los parentesis\n")
		elif izq>der:
			print "Estan desbalanceados por la izquierda\n"
			archivo.write("Estan desbalanceados por la izquierda\n")
		elif der>izq:
			print "Estan desbalanceados por la derecha\n"
			archivo.write("Estan desbalanceados por la derecha\n")
	
	archivo.close()

main()
