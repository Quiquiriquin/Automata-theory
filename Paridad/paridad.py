import random
import turtle

def main():
	menu()

def pregunta():
	opcion = raw_input("Desea regresar al menu\n[1] Si\n[2] No\n")
	if opcion == '2':
		print "Saliendo..."
	else:
		main()


def menu():
	sel = input("Selecciona la opcion deseada:\n[1] Cantidad aleatoria\n[2] Ingreso manual\n[3] Grafo\n[4] Salir\n")

	if sel == 1:
		automatico()
	elif sel == 2:
		manual()
	elif sel == 3:
		grafo()
	else:
		print ("Saliendo...")

def manual():

	numero=[]
	ap = id(numero)
	salida = open("SalidaParidad.txt","w+")
	estado = 0
	i = 0
	contador = 0
	numero = raw_input("Ingrese solo 0 y 1 para formar el numero deseado:")

	for ap in numero:
		if ap == '1' or ap =='0':
			if estado == 0:
				if ap == '0':
					salida.write("Estado:")
					salida.write(str(estado))
					salida.write("\nNumero:")
					salida.write(str(ap))
					salida.write("\n\n")
					impresion(ap,estado)
					estado = 1
					ap = id(numero[i+1])
				elif ap == '1':
					salida.write("Estado:")
					salida.write(str(estado))
					salida.write("\nNumero:")
					salida.write(str(ap))
					salida.write("\n\n")
					impresion(ap,estado)
					estado = 3
					ap = id(numero[i+1])
			if estado == 1:
				if ap == '0':
					salida.write("Estado:")
					salida.write(str(estado))
					salida.write("\nNumero:")
					salida.write(str(ap))
					salida.write("\n\n")
					impresion(ap,estado)
					estado = 0
					ap = id(numero[i+1])
				elif ap == '1':
					salida.write("Estado:")
					salida.write(str(estado))
					salida.write("\nNumero:")
					salida.write(str(ap))
					salida.write("\n\n")
					impresion(ap,estado)
					estado = 2
					ap = id(numero[i+1])
			if estado == 2:
				if ap == '0':
					salida.write("Estado:")
					salida.write(str(estado))
					salida.write("\nNumero:")
					salida.write(str(ap))
					salida.write("\n\n")
					impresion(ap,estado)
					estado = 3
					ap = id(numero[i+1])
				elif ap == '1':
					salida.write("Estado:")
					salida.write(str(estado))
					salida.write("\nNumero:")
					salida.write(str(ap))
					salida.write("\n\n")
					impresion(ap,estado)
					estado = 1
					ap = id(numero[i+1])
			if estado == 3:
				if ap == '0':
					salida.write("Estado:")
					salida.write(str(estado))
					salida.write("\nNumero:")
					salida.write(str(ap))
					salida.write("\n\n")
					impresion(ap,estado)
					estado = 2
					ap = id(numero[i+1])
				elif ap == '1':
					salida.write("Estado:")
					salida.write(str(estado))
					salida.write("\nNumero:")
					salida.write(str(ap))
					salida.write("\n\n")
					impresion(ap,estado)
					estado = 0
					ap = id(numero[i+1])
		else:
			print "Dato no reconocido"
			contador = 1
			break

	estado_fin = estado
	if estado_fin == 0 and contador == 0:
		print "La cadena "+numero+"tiene paridad"
	elif estado_fin != 0 and contador == 0:
		print "La cadena "+numero+" no tiene paridad"
	elif contador == 1:
		print "La cadena "+numero+" no pudo ser reconocida"

	pregunta()

def automatico():
	numero=[]
	ap = id(numero)
	salida = open("SalidaParidad.txt","w+")
	estado = 0

	x = 1
	contador = 0
	cantidad = random.randint(1,50)
	print "Se generaran ",cantidad," caracteres"
	while x <= cantidad:
		numero.append(random.randrange(0,2))
		x = x + 1
	
	
	for i in numero:
		if i == 1 or i ==0:
			if estado == 0:
				if i == 0:
					salida.write("Estado:")
					salida.write(str(estado))
					salida.write("\nNumero:")
					salida.write(str(i))
					salida.write("\n\n")
					impresion(i,estado)
					estado = 1
				elif i == 1:
					salida.write("Estado:")
					salida.write(str(estado))
					salida.write("\nNumero:")
					salida.write(str(i))
					salida.write("\n\n")
					impresion(i,estado)
					impresion(i,estado)
					estado = 3
			if estado == 1:
				if i == 0:
					salida.write("Estado:")
					salida.write(str(estado))
					salida.write("\nNumero:")
					salida.write(str(i))
					salida.write("\n\n")
					impresion(i,estado)
					impresion(i,estado)
					estado = 0
				elif i == 1:
					salida.write("Estado:")
					salida.write(str(estado))
					salida.write("\nNumero:")
					salida.write(str(i))
					salida.write("\n\n")
					impresion(i,estado)
					impresion(i,estado)
					estado = 2
			if estado == 2:
				if i == 0:
					salida.write("Estado:")
					salida.write(str(estado))
					salida.write("\nNumero:")
					salida.write(str(i))
					salida.write("\n\n")
					impresion(i,estado)
					impresion(i,estado)
					estado = 3
				elif i == 1:
					salida.write("Estado:")
					salida.write(str(estado))
					salida.write("\nNumero:")
					salida.write(str(i))
					salida.write("\n\n")
					impresion(i,estado)
					impresion(i,estado)
					estado = 1
			if estado == 3:
				if i == 0:
					salida.write("Estado:")
					salida.write(str(estado))
					salida.write("\nNumero:")
					salida.write(str(i))
					salida.write("\n\n")
					impresion(i,estado)
					impresion(i,estado)
					estado = 2
				elif i == 1:
					salida.write("Estado:")
					salida.write(str(estado))
					salida.write("\nNumero:")
					salida.write(str(i))
					salida.write("\n\n")
					impresion(i,estado)
					impresion(i,estado)
					estado = 0
		else:
			print "Dato no reconocido"
			contador = 1
			break

	print (estado)
	estado_fin = estado
	if estado_fin == 0 and contador == 0:
		salida.write("La cadena ")
		salida.write(str(numero))
		salida.write(" tiene paridad")
		salida.write("\n\n")
		print "La cadena ",numero," tiene paridad"
	elif estado_fin != 0 and contador == 0:
		print "La cadena ",numero," no tiene paridad"
		salida.write("La cadena ")
		salida.write(str(numero))
		salida.write(" no tiene paridad")
		salida.write("\n\n")
	elif contador == 1:
		salida.write("La cadena ")
		salida.write(str(numero))
		salida.write(" no pudo ser reconocida")
		salida.write("\n\n")
		print "La cadena ",numero," no pudo ser reconocida"
	
	pregunta()

def grafo():
	print "Una vez terminado el grafo, presione enter para cerrar el grafo"
	turtle.reset()
	turtle.showturtle()
	#Estado 0
	turtle.penup()
	turtle.goto(-200,50)
	turtle.pendown()
	turtle.circle(30)
	turtle.penup()
	turtle.goto(-210,75)
	turtle.write("q0",font=("Arial",20,"normal"))
	turtle.goto(-200,55)
	turtle.pendown()
	turtle.circle(25)
	turtle.penup()
	turtle.goto(-175,95)
	turtle.dot(7)
	turtle.pendown()
	turtle.goto(175,95)
	turtle.penup()
	turtle.goto(175,65)
	turtle.pendown()
	turtle.dot(7)
	turtle.goto(-175,65)
	turtle.penup()
	turtle.goto(0,100)
	turtle.write("0",font=("Arial",12,"normal"))
	turtle.goto(0,50)
	turtle.write("0",font=("Arial",12,"normal"))
	turtle.goto(-233,80)
	turtle.dot(7)
	turtle.pendown()
	turtle.goto(-280,80)
	turtle.penup()
	turtle.goto(-320,80)
	turtle.write("Inicio",font=("Arial",12,"normal"))


	#Estado 1
	turtle.goto(200,50)
	turtle.pendown()
	turtle.circle(30)
	turtle.penup()
	turtle.goto(190,75)
	turtle.write("q1",font=("Arial",20,"normal"))
	turtle.goto(180,56)
	turtle.pendown()
	turtle.goto(180,-96)
	turtle.dot(7)
	turtle.penup()
	turtle.goto(220,-96)
	turtle.pendown()
	turtle.goto(220,57)
	turtle.dot(7)
	turtle.penup()
	turtle.goto(170,-20)
	turtle.write("1",font=("Arial",12,"normal"))
	turtle.goto(226,-20)
	turtle.write("1",font=("Arial",12,"normal"))

	#Estado 2
	turtle.goto(200,-150)
	turtle.pendown()
	turtle.circle(30)
	turtle.penup()
	turtle.goto(190,-125)
	turtle.write("q2",font=("Arial",20,"normal"))
	turtle.goto(173,-105)
	turtle.pendown()
	turtle.goto(-173,-105)
	turtle.dot(7)
	turtle.penup()
	turtle.goto(-173,-135)
	turtle.pendown()
	turtle.goto(173,-135)
	turtle.dot(7)
	turtle.penup()
	turtle.goto(0,-105)
	turtle.write("0",font=("Arial",12,"normal"))
	turtle.goto(0,-155)
	turtle.write("0",font=("Arial",12,"normal"))



	#Estado 3
	turtle.goto(-200,-150)
	turtle.pendown()
	turtle.circle(30)
	turtle.penup()
	turtle.goto(-210,-125)
	turtle.write("q3",font=("Arial",20,"normal"))
	turtle.goto(-180,56)
	turtle.dot(7)
	turtle.pendown()
	turtle.goto(-180,-96)
	turtle.penup()
	turtle.goto(-220,-96)
	turtle.dot(7)
	turtle.pendown()
	turtle.goto(-220,57)
	turtle.penup()
	turtle.goto(-173,-20)
	turtle.write("1",font=("Arial",12,"normal"))
	turtle.goto(-230,-20)
	turtle.write("1",font=("Arial",12,"normal"))
	raw_input()
	pregunta()





def impresion(ap,estado):

	if estado == 1:
		datos(ap,estado)
	elif estado == 2:
		datos(ap,estado)
	elif estado == 3:
		datos(ap,estado)
	elif estado == 0:
		datos(ap,estado)

def datos(ap, estado):
	print "Estado:",estado,"\nNumero ingresado:",ap,"\n"

main()
