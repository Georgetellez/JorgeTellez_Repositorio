# -*- coding: utf-8 -*-
# Your code goes below this line
import re
import getpass
import modulos
import smtplib, socket, sys, getpass, os, sqlite3
from datetime import date, datetime
personas={}
listatemp=[]
cadenaaux=""
productosaux=""
Tenis = 10
Playera = 20
Pantalon = 30
#El programa de usuario y contraseña lo obtuve de:
#https://www.lawebdelprogramador.com/codigo/Python/3427-Sencillo-programa-de-registro.html
#modificando solo lo de agregarlo a un txt y a una lista
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

def agregar_articulo():
    os.system("cls")
    print("--Agregar artículo--"+"\n")
    nombre = input ("Ingrese el nombre del artículo: ")
    precio = input("Ingrese el precio del artículo: ")
    inventario = input("Ingrese el inventario del artículo: ")
    con = sqlite3.connect("articulos.s3db")
    cursor = con.cursor()
    cursor.execute("insert into articulos (nombre,precio,inventario) values ('"+nombre+"','"+precio+"','"+inventario+"')")
    con.commit()
    con.close()

    while True:
        print("\n[m] Volver al menu"+"\n"+"[s] Salir")
        opcion = input("Elige una opción: ")
        if(opcion == "m"):
            Administrador()
        elif (opcion=="s"):
            sys.exit()
        else:
            print("Digite una opción valida: ")

def ver_articulo():
    os.system("cls")
    print("--Artículos agregados--")
    print("")

    con = sqlite3.connect("articulos.s3db")
    cursor = con.cursor()
    cursor.execute("select * from articulos")

    print("------\t\t\t------\t\t\t------")
    print("nombre\t\t\tprecio\t\t\tinventario")
    print("------\t\t\t------\t\t\t------")

    for articulo in cursor:
        print(articulo[1]+"\t\t\t"+articulo[2]+"\t\t\t"+articulo[3])
        print("")

    con.close()
    while True:
        print("\n[m] Volver al menu"+"\n"+"[s] Salir")
        opcion = input("Elige una opción: ")
        if(opcion == "m"):
            Administrador()
        elif (opcion=="s"):
            sys.exit()
        else:
            print("Digite una opción valida: ")

def modificar_articulo():
    os.system("cls")
    con = sqlite3.connect("articulos.s3db")
    cursor = con.cursor()
    cursor.execute("select * from articulos")

    print("---Modificar articulo---"+"\n")
    print("------\t\t-------\t\t------\t\t------")
    print("Codigo\t\tNombre\t\tPrecio\t\tInventario")
    print("------\t\t-------\t\t------\t\t------")
    print("")

    for articulo in cursor:
        print(str(articulo[0])+"\t\t"+articulo[1]+"\t\t"+articulo[2]+"\t\t"+articulo[3])
        print("")

    while True:
        print("")
        codigo = input("Digite el codigo del artículo que desea modificar: ")
        print("")
        nombre = input("Digite el nuevo nombre: ")
        precio = input("Digite el nuevo precio: ")
        inventario = input("Digite el nuevo inventario: ")
        sql= "update articulos set nombre='"+nombre+"',precio='"+precio+"', inventario='"+inventario+"' where codigo="+codigo

        cursor.execute(sql)
        con.commit()
        con.close()
        print("Artículo modificado"+"\n")
        print("\n[m] Volver al menu"+"\n"+"[s] Salir")
        opcion = input("Elige una opción: ")
        if(opcion == "m"):
            Administrador()
        elif (opcion=="s"):
            sys.exit()
        else:
            print("Digite una opción valida: ")


def eliminar_articulo():
    os.system("cls")
    con = sqlite3.connect("articulos.s3db")
    cursor = con.cursor()
    cursor.execute("select * from articulos")

    print("---Eliminar articulo---"+"\n")
    print("------\t\t-------\t\t------\t\t------")
    print("Codigo\t\tNombre\t\tPrecio\t\tInventario")
    print("------\t\t-------\t\t------\t\t------")
    print("")

    for articulo in cursor:
        print(str(articulo[0])+"\t\t"+articulo[1]+"\t\t"+articulo[2]+"\t\t"+articulo[3])
        print("")
    while True:
        print("")
        odigo = input("Digite el codigo del artículo que desea eliminar: ")
        print("")
        sql= "delete from articulos where codigo="+codigo

        cursor.execute(sql)
        con.commit()
        con.close()
        print("Artículo eliminado"+"\n")
        print("\n[m] Volver al menu"+"\n"+"[s] Salir")
        opcion = input("Elige una opción: ")
        if(opcion == "m"):
            ingresar()
        elif (opcion=="s"):
            sys.exit()
        else:
            print("Digite una opción valida: ")


def comprar_articulo():
    os.system("cls")
    print("Bienvenido a la tienda en linea")
    print("--Artículos disponibles--")
    print("")

    con = sqlite3.connect("articulos.s3db")
    cursor = con.cursor()
    cursor.execute("select * from articulos")

    print("---Articulos---"+"\n")
    print("------\t\t-------\t\t------\t\t------")
    print("Codigo\t\tNombre\t\tPrecio\t\tInventario")
    print("------\t\t-------\t\t------\t\t------")
    print("")

    for articulo in cursor:
        print(str(articulo[0])+"\t\t"+articulo[1]+"\t\t"+articulo[2]+"\t\t"+articulo[3])
        print("")

    query = con.cursor()
    loop = 'true'
    while(loop=='true'):
        codigo = input("Digite el codigo del artículo que desea comprar: ")
        inventario = int(input ("Digite la cantidad: "))
        #if  (query.execute("SELECT codigo, inventario FROM 'ARTICULOS' WHERE 'codigo'='"+codigo+"' AND 'inventario'='"+inventario+"'")):
        if(codigo == "1"):
                tenis =Tenis - inventario
                productos = "update articulos set inventario='"+str(tenis)+"' where codigo="+codigo
                query.execute(productos)
                con.commit()
                tiempoactual=str(datetime.now())
                productosaux="-------FIT PRODUCTS---------"+"\nFecha actual:"+tiempoactual+"\nCompraste:"+"\nTenis: 650"+"\nTotal:$650 \nGracias por su compra"
                modulos.imprimirticket(productosaux)
                sys.exit()
        elif(codigo== "2"):
                playera = Playera - inventario
                productos = "update articulos set inventario='"+str(playera)+"' where codigo="+codigo
                query.execute(productos)
                con.commit()
                tiempoactual=str(datetime.now())
                productosaux="-------FIT PRODUCTS---------"+"\nFecha actual:"+tiempoactual+"\nCompraste:"+"\nPlayera : 200"+"\nTotal:$200 \nGracias por su compra"
                modulos.imprimirticket(productosaux)
                sys.exit()

        elif(codigo=="3"):
                pantalon = Pantalon - inventario
                productos = "update articulos set inventario='"+str(pantalon)+"' where codigo="+codigo
                query.execute(productos)
                con.commit()
                tiempoactual=str(datetime.now())
                productosaux="-------FIT PRODUCTS---------"+"\nFecha actual:"+tiempoactual+"\nCompraste:"+"\nPantalon : 500"+"\nTotal:$500 \nGracias por su compra"
                modulos.imprimirticket(productosaux)
                sys.exit()


        else:
            print("\nDatos erroneos")

    con.close()

def Administrador():
    os.system("cls")
    #Código por parte del canal de youtube https://www.youtube.com/watch?v=h44c1Ev4i2k
    print("--Información de artículos--"+"\n")
    print("1.Agregar artículo"+"\n"+"2. Ver artículo(s)"+"\n"+"3.Modificar artículo"+"\n"+"4.Eliminar artículo"+"\n"+"5.Salir"+"\n")
    while True:
        op1 = input("Elige una opcion: ")
        if (op1 == "1"):
            agregar_articulo()
        elif (op1 == "2"):
            ver_articulo()
        elif (op1 == "3"):
            modificar_articulo()
        elif (op1 == "4"):
            eliminar_articulo()
        elif (op1 == "5"):
            sys.exit()
        else:
            print("Digite una opción valida: ")


def Cliente():
    os.system("cls")
    comprar_articulo()

def register():
    os.system("cls")
    print("---REGISTRO---")
    print("")
    name = input("Ingrese un nombre de usuario:")
    while 1:
        answer01 = user(name)
        if answer01 == True and not(name in personas):
            break
        else:
            name = input("Usuario ya existente, ingrese un nombre de usuario:")
    listatemp.append(name)

    key=getpass.getpass("Ingrese una contraseña:")
    while 1:
        answer02 = password(key)
        if answer02 == True:
            break
        else:
            key = getpass.getpass("Ingrese una contraseña:")
    listatemp.append(key)

    return name
    print("Usuario agregado\n")
    print("\n[m] Volver al menu"+"\n"+"[s] Salir")
    opcion1 = input("Elige una opción: ")
    if(opcion1 == "m"):
        menu()
    elif (opcion1=="s"):
        sys.exit()
    else:
        print("Digite una opción valida: ")


def ingresar():
    os.system("cls")
    while True:
        opc=input("\n1. Administrador  \n2.Cliente  \n3.Salir"+"\n¿Qué perfil vas a escoger?:")
        if(opc=="1"):
            os.system("cls")
            print("----Adminsitrador----")
            name = input("Ingrese el usuario:")
            key= getpass.getpass("Ingrese la contraseña:")
            if name in personas and personas[name][1]==key:
                print("Usuario correcto")
                print("Bienvenido:",name)
                Administrador()

        elif(opc=="2"):
            os.system("cls")
            print("----Cliente----")
            name = input("Ingrese el usuario:")
            key= getpass.getpass("Ingrese la contraseña:")
            if name in personas and personas[name][1]==key:
                print("Usuario correcto")
                print("Bienvenido:",name)
                Cliente()

        elif(opc=="3"):
            break

        else:
            print("Datos incorrectos/ Opción invalida")


def menu():
     while True:
         os.system("cls")
         print("-------FIT PRODUCTS---------")
         print("")
         print("[1].Registrarse"+"\n"+"[2].Ingresar"+"\n"+"[3].Salir\n")
         op = input("Elige una opción: ")
         if op=="1":
             listatemp.clear()
             name = register()
             personas[listatemp[0]]=listatemp
             cadenaaux = "Bienvenido:"+"\nTu nombre es:"+personas.get(name)[0]+"\nTu contraseña es:"+str(personas.get(name)[1])
             modulos.imprimirarchivo(cadenaaux)

         elif op== "2":
             ingresar()
         elif op == "3":
             sys.exit()
         else:
             print("Opción invalida")

menu()
