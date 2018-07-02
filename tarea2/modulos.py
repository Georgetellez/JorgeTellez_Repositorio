def imprimirarchivo(cadena):
	archivousuario = open("archivousuario.txt","a")
	archivousuario.write("\n"+cadena)
	archivousuario.close()


def leerarchivo(nombrearchivo):
	archivousuario = open(nombrearchivo,"r")
	lineas = archivousuario.readlines
	





