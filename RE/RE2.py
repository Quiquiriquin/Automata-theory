import random

def main():
	menu()

def menu():
	sel = input("Seleccione una opcion:\n[1] (0+10)*(e+1)\n[2] [(10)*0+1(01)*1][(0(01)*(1+00)+(01)*(0+11))]\n[3] Salir\n")

	if sel == 1:
		primera()
	elif sel == 2:
		segunda()
	elif sel == 3:
		print "Saliendo...\n"
	else:
		print "Ingrese una opcion valida.\n"
		menu()

def primera():
	archivo = open("SalidaRE.txt","w+")
	print "Se generaran 5 ncadenas de la expresion regular (0+10)*(e+1)\n"
	archivo.write("Se generaran 5 cadenas de la expresion regular (0+10)*(e+1)\n")
	i = 0
	j = 0
	for i in range(5):
		total = cerradura010() 
		archivo.write(str(total)+"\n-------------------")
		print total
		print "---------------------------------------------"
		archivo.write("\n")
		total = ''

	archivo.close()

def cerradura010():
	total = ''
	seleccion = random.randrange(0,2)

	if seleccion==0:
		potencia = random.randint(0,10)
		if potencia == 0:
				total = total + 'e'
		else:
			i = 0
			for i in range(potencia):
				if i == 0:
					total = total + 'e'
				else:
					total = total + '0'
		
	elif seleccion > 0:
		potencia = random.randint(0,10)
		if potencia == 0:
				total = 'e' + total
		else:
			i = 0
			for i in range(potencia):
				if i == 0:
					total = total + 'e'
				else:
					dato = random.randint(0,3)
					if dato == 0:
						total = total + '0'
					else:
						total = total + '1'
		
		total = total + '1'
	total = total + epsilonUno()

	return total



def epsilonUno():
	
	seleccion = random.randrange(0,2)
	if seleccion == 0:
		total = 'e'
	elif seleccion >= 1:
		total = '1'
	return total

def segunda():
	total = ''
	archivo = open("SalidaRE.txt","w+")
	print "Se generaran 5 cadenas de la expresion regular [(10)*0+1(01)*1][(0(01)*(1+00)+(01)*(0+11))]\n"
	archivo.write("Se generaran 5 cadenas de la expresion regular [(10)*0+1(01)*1][(0(01)*(1+00)+(01)*(0+11))]\n\n")
	i = 0
	for i in range(5):
		total = total + primeramitad() + segundamitad()
		print total
		archivo.write(str(total))
		print "---------------------------------------------"
		archivo.write("\n-----------------------\n")
		print "\n"
		total = ''

	archivo.close()
	pregunta()

def primeramitad():
	total =  ''
	seleccion = random.randrange(0,2)
	if seleccion == 0:
		total = total + cerradura10() + '0'
	else:
		total = '1' + cerradura01() + '1'

	return total

def cerradura01():
	total = ''
	potencia = random.randrange(0,10)
	if potencia<5:
		total = 'e'
	else:
		i = 0
		for i in range(potencia):
			if i == 0:
				total = 'e'
			caracter = random.randrange(0,10)
			if caracter<=0:
				total = total + '1'
			else:
				total = total + '0'
	return total

def cerradura10():
	total = ''
	potencia = random.randrange(0,10)
	if potencia == 0:
		total = 'e'
	else:
		i = 0
		for i in range(potencia):
			caracter = random.randrange(0,10)
			if i == 0:
				total = 'e'
			elif caracter<5:
				total = total + '0'
			elif caracter>=5:
				total = total + '1'
	return total

def segundamitad():
	total = ''
	seleccion = random.randrange(0,2)
	if seleccion == 1:
		total = '0' + cerradura01() + opcion100()
	else:
		total = cerradura01() + opcion011()
	
	return total 
	

def opcion100():
	total = ''
	seleccion = random.randrange(0,2)
	if seleccion == 0:
		total = '1'
	else:
		total = '00'
	
	return total

def opcion011():
	total = ''
	seleccion = random.randrange(0,2)
	if seleccion == 0:
		total = '0'
	else:
		total = '11'
	
	return total

def pregunta():
	seleccion = input("Desea repetir el proceso.     [1] Si    [2] No\n")
	if seleccion == 1:
		menu()
	else:
		print "Saliendo...\n"

#demostrar que la gramitca es ambigua
#tienes que demostrar con una cadena que se pueda derivar por la izquierda y por la derecha. Ya que la tienes, sacas una derivacion por la izquierda y la derecha. Basta eso para demostrar que es ambigua
main()
