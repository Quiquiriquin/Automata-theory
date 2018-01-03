def main():
	sel = input("Seleccione una opcion\n[1] Lectura de archivo\n[2] Ingreso manual\n[3] Salir\n")

	if sel == 1:
		lecturaArchivo()
	elif sel == 2:
		manual()
	elif sel == 3:
		print "Saliendo..."
	elif sel != 1 and sel!=2 and sel!=3:
		print "Opcion no valida, ingrese la opcion correcta.\n"
		main()

def lecturaArchivo():
	entrada = open("ArchivoP.txt","r")
	salida = open("SalidaP.txt","w+")
	texto = []
	texto = entrada.read()
	indices_palabras = ['','','','','','','','','']
	contador_palabras = 8
	palabras = ['falso','falsificar','engano','enganar','violencia','copiar','corrupcion','mentir','traficar']
	for i in texto:
		if i == 'f' or i == 'F':
			indices_palabras[0] = falso(texto,i)
			indices_palabras[1] = falsificar(texto,i)
		elif i == 'e' or i == 'E':
			indices_palabras[2] = engano(texto,i)
			indices_palabras[3] = enganar(texto,i)
		elif i == 'v' or i == 'V':
			indices_palabras[4] = violencia(texto,i)
		elif i == 'c' or i == 'C':
			indices_palabras[5] = copiar(texto,i)
			indices_palabras[6] = corrupcion(texto,i)
		elif i == 'm' or i == 'M':
			indices_palabras[7] = mentir(texto,i)
		elif i == 't' or i == 'T':
			indices_palabras[8] = traficar(texto,i)

	print "Las palabras que aparecen en el texto son:\n"
	salida.write("Las palabras que aparecen en el texto son:\n")
	k = 0
	for x in indices_palabras:
		if x == 1:
			print (palabras[k])
			salida.write(str(palabras[k]))
			salida.write("\n")
		k = k + 1	
	entrada.close()
	salida.close()
	pregunta()




def manual():
	salida = open("SalidaP.txt","w+")
	texto = raw_input("Ingrese cualquier texto para comprobar que no  haya palabras peligrosas:")
	indices_palabras = ['','','','','','','','','']
	contador_palabras = 8
	palabras = ['falso','falsificar','engano','enganar','violencia','copiar','corrupcion','mentir','traficar']
	for i in texto:
		if i == 'f' or i == 'F':
			indices_palabras[0] = falso(texto,i)
			indices_palabras[1] = falsificar(texto,i)
		elif i == 'e' or i == 'E':
			indices_palabras[2] = engano(texto,i)
			indices_palabras[3] = enganar(texto,i)
		elif i == 'v' or i == 'V':
			indices_palabras[4] = violencia(texto,i)
		elif i == 'c' or i == 'C':
			indices_palabras[5] = copiar(texto,i)
			indices_palabras[6] = corrupcion(texto,i)
		elif i == 'm' or i == 'M':
			indices_palabras[7] = mentir(texto,i)
		elif i == 't' or i == 'T':
			indices_palabras[8] = traficar(texto,i)
	print "Las palabras que aparecen en el texto son:\n"
	salida.write("Las palabras que aparecen en el texto son:\n")
	k = 0
	for x in indices_palabras:
		if x == 1:
			print (palabras[k])
			salida.write(str(palabras[k]))
			salida.write("\n")
		k = k + 1	
	salida.close()
	pregunta()





def falso(texto,i):
	contador = 0
	contador_ap = 0
	for i in texto:
		if i == 'f' or i == 'F' and contador == 0:
			contador += 1
		elif i == 'a' or i == 'A' and contador == 1:
			contador += 1
		elif i == 'l' or i =='L' and contador == 2:
			contador += 1
		elif i == 's' or i == 'S' and contador == 3:
			contador += 1
		elif i =='o' or i == 'O' and contador == 4:
			contador += 1
		elif contador == 5 and i == ' ':
			contador_ap = contador_ap + 1
			"""print (contador_ap)"""
			contador = 0
			return 1
		elif i == ' ':
			contador = 0


def falsificar(texto,i):
	contador = 0
	contador_ap = 0
	for i in texto:
		if (i == 'f' or i == 'F') and (contador == 0 or contador == 5):
			contador += 1
		elif (i == 'a' or i == 'A') and (contador == 1 or contador == 8):
			contador += 1
		elif i == 'l' or i == 'L' and contador == 2:
			contador += 1
		elif i == 's' or i == 'S' and contador == 3:
			contador += 1
		elif (i == 'i' or i == 'R') and (contador == 4 or contador == 6):
			contador += 1
		elif i == 'c' or i =='C' and contador == 7:
			contador += 1
		elif i == 'R' or i == 'r' and contador == 9:
			contador += 1		
		elif i == ' ':
			contador = 0
	if contador == 10:
			contador_ap += 1
			"""print (contador_ap)"""
			return 1

def engano(texto,i):
	contador = 0
	contador_ap = 0
	for i in texto:
		if i == 'e' or i == 'E' and contador == 0:
			contador += 1
		elif (i == 'n' or i == 'N') and (contador == 1 or contador == 4):
			contador += 1
		elif i == 'g' or i == 'G' and contador == 2:
			contador += 1
		elif i == 'A' or i == 'a' and contador == 3:
			contador += 1
		elif i == 'o' or i == 'O' and contador == 5:
			contador += 1	
		elif contador == 6:
			contador_ap = contador_ap + 1
			"""print (contador_ap)"""
			contador = 0
			return 1
		elif i == ' ':
			contador = 0


def enganar(texto,i):
	contador = 0
	contador_ap = 0
	for i in texto:
		if i == 'e' or i == 'E' and contador == 0:
			contador += 1
		elif (i == 'n' or i == 'N') and (contador == 1 or contador == 4): 
			contador += 1
		elif i == 'g' or i == 'G' and contador == 2:
			contador += 1
		elif (i == 'A' or i == 'a') and (contador == 3 or contador == 5) :
			contador += 1
		elif i == 'r' or i == 'R' and contador == 6:
			contador += 1	
		elif contador == 7:
			contador_ap = contador_ap + 1
			"""print (contador_ap)"""
			contador = 0
			return 1
		elif i == ' ':
			contador = 0


def violencia(texto,i):
	contador = 0
	contador_ap = 0
	for i in texto:
		if i == 'v' or i == 'V' and contador == 0:
			contador += 1
		elif i == 'a' or i == 'A' and contador == 8:
			contador += 1
		elif (i == 'l' or i == 'L') and contador == 3:
			contador += 1
		elif i == 'e' or i == 'E' and contador == 4:
			contador += 1
		elif (i == 'i' or i == 'I') and (contador == 1 or contador == 7):
			contador += 1
		elif i == 'c' or i =='C' and contador == 6:
			contador += 1
		elif i == 'n' or i =='N' and contador == 5:
			contador += 1
		elif i == 'o' or i == 'O' and contador == 2:
			contador += 1		
		elif contador == 9:
			contador_ap = contador_ap + 1
			"""print (contador_ap)"""
			contador = 0
			return 1
		elif i == ' ':
			contador = 0



def copiar(texto,i):
	contador = 0
	contador_ap = 0
	for i in texto:
		if i == 'a' or i == 'A' and contador == 4:
			contador += 1
		elif i == 'i' or i == 'R' and contador == 3:
			contador += 1
		elif i == 'c' or i =='C' and contador == 5:
			contador += 1
		elif i == 'r' or i =='R' and contador == 2:
			contador += 1
		elif i == 'o' or i == 'O' and contador == 0:
			contador += 1		
		elif i == 'p' or i == 'P' and contador == 1:
			contador += 1
		elif contador == 6:
			contador_ap = contador_ap + 1
			"""print (contador_ap)"""
			contador = 0
			return 1
		elif i == ' ':
			contador = 0


def corrupcion(texto,i):
	contador = 0
	contador_ap = 0
	for i in texto:
		if (i == 'c' or i == 'C') and (contador == 0 or contador == 6) :
			contador += 1
		elif (i == 'o' or i == 'O') and (contador == 1 or contador == 8):
			contador += 1
		elif (i == 'r' or i == 'R') and (contador == 2 or contador == 3):
			contador += 1
		elif i == 'u' or i == 'U' and contador == 4:
			contador += 1
		elif i == 'p' or i == 'P' and contador == 5:
			contador += 1
		elif i == 'i' or i =='i' and contador == 7:
			contador += 1
		elif i == 'n' or i =='N' and contador == 9:
			contador += 1	
		elif contador == 10:
			contador_ap = contador_ap + 1
			"""print (contador_ap)"""
			contador = 0
			return 1
		elif i == ' ':
			contador = 0

def mentir(texto,i):
	contador = 0
	contador_ap = 0
	for i in texto:
		if (i == 'm' or i == 'M') and contador == 0 :
			contador += 1
		elif (i == 'e' or i == 'E') and contador == 1:
			contador += 1
		elif (i == 'n' or i == 'N') and contador == 2:
			contador += 1
		elif i == 't' or i == 'T' and contador == 3:
			contador += 1
		elif i == 'i' or i == 'I' and contador == 4:
			contador += 1
		elif i == 'r' or i =='R' and contador == 5:
			contador += 1
		elif contador == 6:
			contador_ap = contador_ap + 1
			"""print (contador_ap)"""
			contador = 0
			return 1
		elif i == ' ':
			contador = 0


def traficar(texto,i):
	contador = 0
	contador_ap = 0
	for i in texto:
		if i == 't' or i == 'T' and contador == 0:
			contador += 1
		elif i == 'r' or i =='R' and (contador == 1 or contador == 7):
			contador += 1
		elif (i == 'a' or i == 'A') and (contador == 2 or contador == 6):
			contador += 1
		elif (i == 'f' or i == 'F') and contador == 3:
			contador += 1
		elif i == 'i' or i == 'I' and contador == 4:
			contador += 1
		elif (i == 'c' or i == 'C') and contador == 5:
			contador += 1
		if contador == 8:
			contador_ap = contador_ap + 1
			"""print (contador_ap)"""
			contador = 0
			return 1
		if i == ' ':
			contador = 0
	
def pregunta():
	sel = raw_input("Desea regresar al menu\n[1] Si      [2] No\n")
	if sel == '1':
		main()
	elif sel == '2':
		print"Saliendo..."
		
main()