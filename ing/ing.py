import turtle
import time

def main ():
	sel = input("Selecciona la opcion deseada:\n[1] Lectura de archivo\n[2] Ingreso manual\n[3] Grafo\n[4] Salir\n")

	if sel == 1:
		lecturaArchivo()
	elif sel == 2:
		manual()
	elif sel == 3:
		dibujo()
	else:
		print ("Saliendo...")

def lecturaArchivo():
	i = 0
	estado = 0
	palabras =[]
	caracteres = []
	ap = id(caracteres)
	archivo = open("ArchivoPrueba.txt")
	salida = open("SalidaIng.txt","w+")
	
	caracteres = archivo.read()

	for ap in caracteres:
		if (ap == 'i' or ap == 'I') and estado == 0:
			salida.write("Estado:")
			salida.write(str(estado))
			salida.write("\nLetra:")
			salida.write(str(ap))
			salida.write("\n\n")
			impresion(ap,estado)
			estado = 1
		elif (ap == 'n' or ap == 'N') and estado == 1:
			salida.write("Estado:")
			salida.write(str(estado))
			salida.write("\nLetra:")
			salida.write(str(ap))
			salida.write("\n\n")
			impresion(ap,estado)
			estado = 2
		elif (ap == 'g' or ap == 'G') and estado == 2 and caracteres[i+1] == ' ':
			salida.write("Estado:")
			salida.write(str(estado))
			salida.write("\nLetra:")
			salida.write(str(ap))
			salida.write("\n\n")
			impresion(ap,estado)

		elif (ap == 'g' or ap == 'G') and estado == 2 and caracteres[i+1] !=' ':
			salida.write("Estado:")
			salida.write(str(estado))
			salida.write("\nLetra:")
			salida.write(str(ap))
			salida.write("\n\n")
			impresion(ap,estado)
			estado = 0

		elif ap == ' ':
			salida.write("Estado:")
			salida.write(str(estado))
			salida.write("\nLetra:")
			salida.write(str(ap))
			salida.write("\n\n")
			impresion(ap, estado)
			estado = 0
		else:
				salida.write("Estado:")
				salida.write(str(estado))
				salida.write("\nLetra:")
				salida.write(str(ap))
				salida.write("\n\n")
				impresion(ap,estado)
				estado = 0
	
	with open("ArchivoPrueba.txt") as f:
	    for line in f:
	        words = line.split(" ")
	        for word in words:
	           if 'ing' == word[-3:]:
	              palabras.append(word)

	print "Las palabras que aperecen son:"
	for x in palabras:
			print (x)
			salida.write(str(x))
			salida.write("\n")
	
	pregunta()




def manual():
	texto = []
	palabras=[]
	posiciones=[]
	i = 0;
	ap = id(texto)
	id(palabras)
	estado = 0
	pos = 0
	salida = open("SalidaIng.txt","w+")
	texto = raw_input("Ingresa la cadena de texto en la que se buscara la terminacion ing:")
	copia = open("Copia.txt","w+")
	for j in texto:
		copia.write(str(j))
	copia.close()
	for ap in texto:
		if (ap == 'i' or ap == 'I') and estado == 0:
			salida.write("Estado:")
			salida.write(str(estado))
			salida.write("\nLetra:")
			salida.write(str(ap))
			salida.write("\n\n")
			impresion(ap,estado)
			estado = 1
		elif (ap == 'n' or ap == 'N') and estado == 1:
			salida.write("Estado:")
			salida.write(str(estado))
			salida.write("\nLetra:")
			salida.write(str(ap))
			salida.write("\n\n")
			impresion(ap,estado)
			estado = 2
		elif (ap == 'g' or ap == 'G') and estado == 2 and texto[i+1] == ' ':
			salida.write("Estado:")
			salida.write(str(estado))
			salida.write("\nLetra:")
			salida.write(str(ap))
			salida.write("\n\n")
			impresion(ap,estado)

		elif (ap == 'g' or ap == 'G') and estado == 2 and texto[i+1] !=' ':
			salida.write("Estado:")
			salida.write(str(estado))
			salida.write("\nLetra:")
			salida.write(str(ap))
			salida.write("\n\n")
			impresion(ap,estado)
			estado = 0

		elif ap == ' ':
			salida.write("Estado:")
			salida.write(str(estado))
			salida.write("\nLetra:")
			salida.write(str(ap))
			salida.write("\n\n")
			impresion(ap, estado)
			estado = 0
		else:
				salida.write("Estado:")
				salida.write(str(estado))
				salida.write("\nLetra:")
				salida.write(str(ap))
				salida.write("\n\n")
				impresion(ap,estado)
				estado = 0
	ap = id(texto[i+1])
	

	
	with open("Copia.txt") as f:
	    for line in f:
	        words = line.split(" ")
	        for word in words:
	           if 'ing' == word[-3:]:
	              palabras.append(word)

	print "Las palabras que aperecen son:"
	for x in palabras:
			print (x)
			salida.write(str(x))
			salida.write("\n")

	pregunta()

def dibujo():

	print "Una vez que termine de ver el grafo, presione enter en la terminal para salir."

	turtle.showturtle()
	turtle.penup()
	turtle.goto(-250,0)
	turtle.pendown()
	turtle.circle(30)
	turtle.penup()
	turtle.goto(-260,25)
	turtle.write("q0",font=("Arial",20,"normal"))
	turtle.penup()
	turtle.goto(-220,30)
	turtle.pendown()
	turtle.forward(135)
	turtle.dot(8)
	turtle.penup()

	turtle.goto(-50,0)
	turtle.pendown()
	turtle.circle(30)
	turtle.penup()
	turtle.goto(-60,25)
	turtle.write("q1",font=("Arial",20,"normal"))
	turtle.penup()
	turtle.goto(-20,30)
	turtle.pendown()
	turtle.forward(140)
	turtle.dot(8)
	turtle.penup()

	turtle.goto(150,0)
	turtle.pendown()
	turtle.circle(30)
	turtle.penup()
	turtle.goto(150,5)
	turtle.pendown()
	turtle.circle(25)
	turtle.penup()
	turtle.goto(140,25)
	turtle.write("q2",font=("Arial",20,"normal"))
	turtle.penup()
	turtle.goto(150,60)
	turtle.right(270)
	turtle.pendown()
	turtle.circle(60,90)
	turtle.goto(-190,120)
	turtle.circle(60,90)
	turtle.dot(8)

	turtle.penup()
	turtle.goto(-250,0)
	turtle.pendown()
	turtle.dot(8)
	turtle.circle(60,90)
	turtle.goto(-110,-60)
	turtle.circle(60,90)

	turtle.penup()
	turtle.goto(-100,125)
	turtle.write("Diferente de ' ' o de final de cadena",font=("Arial",12,"normal"))
	turtle.goto(-180,-75)
	turtle.write("Diferente de g",font=("Arial",12,"normal"))
	turtle.goto(-160,35)
	turtle.write("n",font=("Arial",12,"normal"))
	turtle.goto(65,35)
	turtle.write("g",font=("Arial",12,"normal"))
	turtle.goto(-390,30)
	turtle.pendown()
	turtle.goto(-280,30)
	turtle.dot(7)
	turtle.penup()
	turtle.goto(-420,30)
	turtle.write("Inicio",font=("Arial",12,"normal"))
	turtle.goto(-370,35)
	turtle.write("Diferente i o i",font=("Arial",12,"normal"))
	raw_input()
	pregunta()


def pregunta():
	opcion = raw_input("Desea regresar al menu\n[1] Si\n[2] No\n")
	if opcion == '2':
		print "Saliendo..."
	else:
		main()
		
		


def impresion(ap,estado):
	print "Estado:",estado,"\nLetra:"+ap,"\n"

main()