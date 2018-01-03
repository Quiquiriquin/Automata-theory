from turtle import *

def main():
	menu()

def menu():
	sel = input("Seleccione una opcion:\n[1] Lectura de archivo\n[2] Ingreso manual\n[3] Grafo\n[4] Salir\n")

	if sel == 1:
		lecturaArchivo()
	elif sel == 2:
		manual()
	elif sel == 3:
		grafo()
	elif sel == 4:
		print "Saliendo...\n"
	else:
		print "Ingrese una opcion valida.\n"
		menu()

def busqueda(texto,opcion):
	if opcion == 1:
		archivo = open("SalidaWebayAutomatico.txt","w+")
	elif opcion == 2:
		archivo = open("SalidaWebayManual.txt","w+")
	
	posicionesweb = []
	posicionesebay = []
	j = 0
	x = 0
	contador_pos = 0
	contador_web=0
	contador_ebay=0
	estado = 0
	estado2 = 0
	for i in texto:	
		if (i == 'w' or i == 'W') and (estado == 0 or estado != 0):
			estado = 1
			archivo.write("Estado:")
			archivo.write(str(estado))
			archivo.write("\nDato:")
			archivo.write(str(i))
			archivo.write("\n\n")
			contador_pos = contador_pos + 1
			print "Estado:",estado,"\nDato:"+i+"\n"
		elif (i == 'e' or i == 'E') and (estado2 == 0 or estado2 != 0):
			if estado == 1:
				estado = 2
				estado2 = 4
				archivo.write("Estado:")
				archivo.write(str(estado))
				archivo.write(",")
				archivo.write(str(estado2))
				archivo.write("\nDato:")
				archivo.write(str(i))
				archivo.write("\n\n")
				contador_pos = contador_pos + 1
				print "Estado:",estado2,"\nDato:"+i+"\n"
			elif estado == 2:
				estado = 0
				estado2 = 4
				archivo.write("Estado:")
				archivo.write(str(estado))
				archivo.write(",")
				archivo.write(str(estado2))
				archivo.write("\nDato:")
				archivo.write(str(i))
				archivo.write("\n\n")
				contador_pos = contador_pos + 1
				print "Estado:",estado2,"\nDato:"+i+"\n"
			else:
				estado2 = 4
				archivo.write("Estado:")
				archivo.write(str(estado2))
				archivo.write("\nDato:")
				archivo.write(str(i))
				archivo.write("\n\n")
				contador_pos = contador_pos + 1
				print "Estado:",estado2,"\nDato:"+i+"\n"
		elif i == 'b' or i == 'B':
			if estado == 2:
				estado = 3
				estado2 = 5
				archivo.write("Estado:")
				archivo.write(str(estado))
				archivo.write(",")
				archivo.write(str(estado2))
				archivo.write("\nDato:")
				archivo.write(str(i))
				archivo.write("\n")
				contador_pos = contador_pos + 1
				print "Estado:",estado2,"\nDato:"+i
				if estado == 3:
						posicionesweb.append(contador_pos-3)
						j = j+1
						archivo.write("Se ha encontrado la subcadena web.\n\n")
						print "Se ha encontrado la subcadena web."
						estado = 0
						contador_web = contador_web+1
			elif estado2 == 4:
				estado2 = 5
				archivo.write("Estado:")
				archivo.write(str(estado2))
				archivo.write("\nDato:")
				archivo.write(str(i))
				archivo.write("\n\n")
				contador_pos = contador_pos + 1
				print "Estado:",estado2,"\nDato:"+i+"\n"
		elif (i == 'a' or i == 'A') and estado2 == 5:
			estado2 = 6
			archivo.write("Estado:")
			archivo.write(str(estado2))
			archivo.write("\nDato:")
			archivo.write(str(i))
			archivo.write("\n\n")
			contador_pos = contador_pos + 1
			print "Estado:",estado2,"\nDato:"+i+"\n"
		elif (i == 'y' or i == 'Y') and estado2 == 6:
			estado2 = 7
			archivo.write("Estado:")
			archivo.write(str(estado2))
			archivo.write("\nDato:")
			archivo.write(str(i))
			archivo.write("\n\n")
			contador_pos = contador_pos + 1
			print "Estado:",estado2,"\nDato:"+i
			if estado2 == 7:
				archivo.write("Se ha encontrado la subcadena ebay.\n\n")
				print "Se ha encontrado la subcadena ebay."
				posicionesebay.append(contador_pos-4)
				x = x + 1
				contador_ebay = contador_ebay + 1
		else:
			estado = 0
			estadoP = 0
			archivo.write("Estado:")
			archivo.write(str(estado))
			archivo.write("\nDato:")
			archivo.write(str(i))
			archivo.write("\n\n")
			print "Estado:",estado,"\nDato:"+i+"\n"
			contador_pos = contador_pos + 1
	print "Se ha encontrado la subcadena web:",contador_web,"veces\nSe ha encontrado la subcadena ebay:",contador_ebay,"veces\n"
	archivo.write("Se ha encontrado la subcadena web: ")
	archivo.write(str(contador_web))
	archivo.write(" veces\n\nSe ha encontrado la subcadena ebay: ")
	archivo.write(str(contador_ebay))
	archivo.write(" veces\n\n")

	print "Las posiciones de la subcadena web son:"
	archivo.write("Las posiciones de la subcadena web son: ")
	for pos in posicionesweb:
		archivo.write(str(pos))
		archivo.write(" ")
		print "",pos," "

	print "\nLas posiciones de la subacdena ebay son:"
	archivo.write("\n\nLas posiciones de la subcadena ebay son: ")
	for pos in posicionesebay:
		archivo.write(str(pos))
		archivo.write(" ")
		print "",pos," "

	archivo.write("\n")

	archivo.close()




def manual():
	opcion = 2	
	texto = []
	texto = raw_input("Ingrese un texto o palabras en las que se buscaran las subcadenas web & ebay:")
	busqueda(texto,opcion)

	option = input("Desea repetir el proceso\n[1] Si   [2] No:")
	if option == 1:
		main()
	else:
		print "Saliendo..."

def lecturaArchivo():
	texto = []
	archivo = open("ArchivoWebay.txt","r+")
	texto = archivo.read()
	opcion = 1
	busqueda(texto,opcion)

	option = input("Desea repetir el proceso\n[1] Si   [2] No:")
	if option == 1:
		main()
	else:
		print "Saliendo..."

def grafo():
	print "Una vez que termine de ver el grafo, presione enter en la terminal para salir."
	reset()
	showturtle()
	penup()
	goto(0,-30)
	pendown()
	circle(30)
	penup()
	goto(-5,-5)
	pendown()
	write("q0",font=("Arial",12,"normal"))
	penup()
	goto(0,30)
	pendown()
	goto(0,130)
	dot(7)
	circle(30)
	penup()
	goto(7,85)
	write("w",font=("Arial",12,"normal"))
	goto(-5,155)
	write("w",font=("Arial",12,"normal"))
	goto(-15,135)
	pendown()
	goto(-120,100)
	dot(7)
	penup()
	goto(-150,70)
	pendown()
	circle(30)
	penup()
	goto(-155,95)
	write("e",font=("Arial",12,"normal"))
	goto(-155,70)
	penup()
	goto(-155,-90)
	pendown()
	circle(30)
	penup()
	goto(-160,-65)
	write("e",font=("Arial",12,"normal"))
	goto(-155,-90)
	pendown()
	goto(-90,-150)
	dot(7)
	penup()
	goto(-125,-140)
	write("b",font=("Arial",12,"normal"))
	goto(-60,-180)
	pendown()
	circle(30)
	penup()
	goto(-65,-155)
	write("b",font=("Arial",12,"normal"))
	goto(-30,-150)
	pendown()
	goto(60,-150)
	dot(7)
	penup()
	goto(15,-145)
	write("a",font=("Arial",12,"normal"))
	goto(90,-180)
	pendown()
	circle(30)
	penup()
	goto(85,-155)
	write("a",font=("Arial",12,"normal"))
	goto(120,-150)
	pendown()
	goto(220,0)
	dot(7)
	circle(30)
	penup()
	goto(165,-75)
	write("y",font=("Arial",12,"normal"))
	goto(215,25)
	write("y",font=("Arial",12,"normal"))

	goto(190,30)
	pendown()
	goto(30,0)
	dot(7)
	penup()
	goto(100,2)
	write("S-e-w",font=("Arial",9,"normal"))
	goto(0,-30)
	pendown()
	dot(7)
	goto(90,-120)
	penup()
	goto(50,-75)
	write("S-e-w-y",font=("Arial",9,"normal"))
	goto(-60,-120)
	pendown()
	goto(-20,-25)
	dot(7)
	penup()
	goto(-60,-60)
	write("S-b-w-e",font=("Arial",9,"normal"))
	goto(-125,-60)
	pendown()
	goto(-25,-10)
	dot(7)
	penup()
	goto(-75,-35)
	write("S-b-w-e",font=("Arial",9,"normal"))
	goto(-125,85)
	pendown()
	goto(-30,10)
	dot(7)
	penup()
	goto(-70,45)
	write("S-b-w-e",font=("Arial",9,"normal"))
	goto(-125,120)
	pendown()
	goto(-30,160)
	dot(7)
	penup()
	goto(-80,140)
	write("w",font=("Arial",9,"normal"))
	goto(-125,-65)
	pendown()
	goto(-10,130)
	dot(7)
	penup()
	goto(-55,15)
	write("w",font=("Arial",9,"normal"))
	goto(-70,-120)
	pendown()
	goto(-115,15)
	goto(-10,130)
	penup()
	goto(-120,15)
	write("w",font=("Arial",9,"normal"))
	goto(90,-125)
	pendown()
	goto(125,15)
	goto(10,130)
	dot(7)
	penup()
	goto(130,15)
	write("w",font=("Arial",9,"normal"))
	goto(190,30)
	pendown()
	goto(10,130)
	penup()
	goto(100,85)
	write("w",font=("Arial",9,"normal"))

	goto(-55,-125)
	pendown()
	goto(-145,-85)
	dot(7)
	penup()
	goto(-95,-105)
	write("e",font=("Arial",9,"normal"))
	goto(80,-180)
	pendown()
	goto(60,-190)
	goto(-150,-190)
	goto(-150,-90)
	penup()
	goto(-150,-205)
	write("e",font=("Arial",9,"normal"))
	goto(220,0)
	pendown()
	goto(220,-210)
	goto(-160,-210)
	goto(-160,-90)
	dot(7)
	penup()
	goto(-170,-220)
	write("e",font=("Arial",9,"normal"))
	raw_input()



main()

