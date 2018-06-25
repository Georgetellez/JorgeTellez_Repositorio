from e3 import nombre,edad,tarjetacredito,paypalcuenta

archivousuario = open("archivousuario.txt","w")
cadena=nombre()+str(edad()+tarjetacredito()+paypalcuenta())
archivousuario.write(cadena)
archivousuario.close()