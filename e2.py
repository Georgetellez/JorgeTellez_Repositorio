listapersonas=[]

nombre = input("Ingresa tu nombre:")
apellido = input("Ingresa tu apellido:")
edad = input("ingresa tu edad:")
listapersonas.append(nombre)
listapersonas.append(apellido)
listapersonas.append(edad)
print(listapersonas)

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
		break
	else:
		nombre = input("Ingresa tu nombre:")
		apellido = input("Ingresa tu apellido:")
		edad = input("ingresa tu edad:")
		listapersonas.append(nombre)
		listapersonas.append(apellido)
		listapersonas.append(edad)
		print(listapersonas)		

