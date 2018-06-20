listapersonas=[]
import os
nombre = input("Ingresa tu nombre:")
apellido = input("Ingresa tu apellido:")
edad = input("ingresa tu edad:")
listapersonas.append(nombre)
listapersonas.append(apellido)
listapersonas.append(edad)


respuesta = input ("¿Deseas ingresar más usuarios S/N?")
while(respuesta=="s"):
	nombre = input("Ingresa tu nombre:")
	apellido = input("Ingresa tu apellido:")
	edad = input("ingresa tu edad:")
	listapersonas.append(nombre)
	listapersonas.append(apellido)
	listapersonas.append(edad)
	continuar=input("¿Deseas parar S/N?")
	if(continuar=="s"):
		print(listapersonas)
		os.system("pause") #pausa la pantalla para que no se cierre la ventana
		break #rompe el ciclo while
		
if(respuesta=="n"):
	print(listapersonas)
	os.system("pause") #pausa la pantalla para que no se cierre la ventana