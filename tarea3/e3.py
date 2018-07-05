import re
import getpass
import modulos
personas={}
listatemp=[]
cadenaaux=""
class usuario:
	name=""
	key=""
	nombre=""
	apellido=""
	edad=0.0
	tarjeta=0.0
	correo=""
	key1=""

def passwordpaypal(key1):
    # Declara las variables
    letters = len(key1)
    lower_case = 0
    upper_case = 0
    numeric = 0
    no_alpha = 0
    space = 0
 
    # Comprueba que la contraseña es correcta
    if letters < 8:
        print ("La contraseña debe contener 8 caracteres")
    else:
        for content in key1:
            if content.islower() == True:
                lower_case += 1
            elif content.isupper() == True:
                upper_case += 1
            elif content.isdigit() == True:
                numeric += 1
            else:
                if content.isspace() == True:
                    space += 1
                elif content.isalnum() == False:
                    no_alpha += 1
 
        # Comprueba si la contraseña cumple con los parametros
        if lower_case >= 1:
            if upper_case >= 1:
                if numeric >= 1:
                    if no_alpha >= 1:
                        if space >= 1:
                            print ("La contraseña no puede contener espacio en blancos")
                        else:
                            return True
                    else:
                        print ("La contraseña debe tener como minimo un caracter no alfanumerico")
                else:
                    print ("La contraseña debe tener como minimo un caracter numerico")
            else:
                print ("La contraseña debe tener como minimo un caracter en mayuscula")
        else:
            print ("La contraseña debe tener como minimo un caracter en minuscula")

def password(key):
    # Declara las variables
    letters = len(key)
    lower_case = 0
    upper_case = 0
    numeric = 0
    no_alpha = 0
    space = 0
 
    # Comprueba que la contraseña es correcta
    if letters < 8:
        print ("La contraseña debe contener 8 caracteres")
    else:
        for content in key:
            if content.islower() == True:
                lower_case += 1
            elif content.isupper() == True:
                upper_case += 1
            elif content.isdigit() == True:
                numeric += 1
            else:
                if content.isspace() == True:
                    space += 1
                elif content.isalnum() == False:
                    no_alpha += 1
 
        # Comprueba si la contraseña cumple con los parametros
        if lower_case >= 1:
            if upper_case >= 1:
                if numeric >= 1:
                    if no_alpha >= 1:
                        if space >= 1:
                            print ("La contraseña no puede contener espacio en blancos")
                        else:
                            return True
                    else:
                        print ("La contraseña debe tener como minimo un caracter no alfanumerico")
                else:
                    print ("La contraseña debe tener como minimo un caracter numerico")
            else:
                print ("La contraseña debe tener como minimo un caracter en mayuscula")
        else:
            print ("La contraseña debe tener como minimo un caracter en minuscula")


# Funcion para el nombre de usuario
def user(usuario):
 
    # Cuenta la cantidad de letras
    letters = len(usuario)
    answer = usuario.isalnum()
 
    # Comprueba que el nombre cumple lo especificado
    if letters < 6:
        print ("El nombre de usuario debe contener al menos 6 caracteres")
    elif letters > 12:
        print ("El nombre de usuario no puede contener mas de 12 caracteres")
    elif answer == False:
        print ("El nombre de usuario puede contener solo letras y numeros")
        print ("Nota: Evita los espacios en blanco")
    else:
        return True
# Funcion para simular el registro

def register():
	persona1=usuario()
    persona1.name = input("Ingrese un nombre de usuario:")
    while 1:
        answer01 = user(name)
        if answer01 == True and not(name in personas):
            break
        else:
            name = input("Usuario ya existente, ingrese un nombre de usuario:")
    listatemp.append(name)

    persona1.key=getpass.getpass("Ingrese una contraseña:")
    while 1:
        answer02 = password(key)
        if answer02 == True:
            break
        else:
            persona1.key = getpass.getpass("Ingrese una contraseña:")
    listatemp.append(key)
  
    return name


def nombre():
	persona1.nombre = input("Ingresa tu nombre:")
	persona1.apellido = input("Ingresa tu apellido:")
	listatemp.append(nombre)
	listatemp.append(apellido)
	

def edad():
	while True:
		persona1.edad = input("ingresa tu edad:")
		listatemp.append(edad)

		try:
			persona1.edad=int(edad)
			return edad
		except ValueError:
			print("ATENCIÓN: Debe ingresar un número entero")
	
def tarjetacredito():
	while True:
		persona1.tarjeta=input("ingresa tu tarjeta de crédito:")
		listatemp.append(tarjeta)

		try:
			tarjeta=int(tarjeta)
			return int(tarjeta)
		except ValueError:
			print("ATENCIÓN:Debe ingresar tu tarjeta de crédito:")
	
def paypalcuenta():
	while True:
		persona1.correo = input("Ingresa tu correo de paypal en minúsculas:")
		if re.match("^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$",correo.lower()):
			print("Correo correcto")
			break
		else:
			print("Correo incorrecto")
			persona1.correo= input("Ingresa tu correo de paypal en minúsculas:")
	listatemp.append(correo)
	

	persona1.key1=getpass.getpass("Ingrese una contraseña:")
	while 1:
		answer03 = passwordpaypal(key1) 
		if answer03 == True:
			break
		else:
			persona1.key1 = getpass.getpass("Ingrese tu contraseña de paypal:")
	listatemp.append(key1)
	
def ingresar(personas):
    while True:
        persona1.name = input("Ingrese el usuario:")
        persona1.key= input("Ingrese la contraseña:")
        if name in personas and personas[name][1]==key:
            print("Usuario correcto")
            print("Bienvenido:",personas.get(name)[2],personas.get(name)[3],"\nTu edad es:",personas.get(name)[4],"\nTu tarjeta de credito es:",personas.get(name)[5],"\nTu correo de paypal es:",personas.get(name)[6],"\nTu contraseña de paypal es:",personas.get(name)[7])
            #cadenaaux = "Bienvenido"+personas.get(name)[2]+personas.get(name)[3]+"\nTu edad es:"+str(personas.get(name)[4])+"\nTu tarjeta de credito es:"+str(personas.get(name)[5])+"\nTu correo de paypal es:"+personas.get(name)[6]+"\nTu contraseña de paypal es:"+str(personas.get(name)[7])
            #modulos.imprimirarchivo(cadenaaux)
        else:
            print("Datos incorrectos")


def menu():
    while True:
        print("Nuevo usuario-n, Usuario existente-u, Salir-s")
        opcion=input().lower()
        if(opcion=="n"):
            listatemp.clear()
            name = register()
            nombre()
            edad()
            tarjetacredito()
            paypalcuenta()
            personas[listatemp[0]]=listatemp
            print("Usuario registrado")
            cadenaaux = "Bienvenido:"+personas.get(name)[2]+personas.get(name)[3]+"\nTu edad es:"+str(personas.get(name)[4])+"\nTu tarjeta de credito es:"+str(personas.get(name)[5])+"\nTu correo de paypal es:"+personas.get(name)[6]+"\nTu contraseña de paypal es:"+str(personas.get(name)[7])
            modulos.imprimirarchivo(cadenaaux)
            
        elif(opcion=="u"):
            ingresar(personas)
        elif(opcion=="s"):
            break
        else:
            print("opción invalida")
menu()





