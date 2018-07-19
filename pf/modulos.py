def imprimirarchivo(cadena):
	archivousuario = open("archivousuario.txt","a")
	archivousuario.write("\n"+cadena)
	archivousuario.close()
def imprimirticket(productos):
	archivousuario = open("Ticketcompras.txt","a")
	archivousuario.write("\n"+productos)
	archivousuario.close()
