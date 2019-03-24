from lxml import etree
import webbrowser
def listar_provincia(doc):
	listaP=doc.xpath("//RADAR/../../NOMBRE/text()")
	return listaP
def contar_radares(doc):
	cuenta=doc.xpath("count(//CARRETERA/RADAR)")
	return cuenta
def pedirycarreteraradares(doc,provincia):
	indicador=False
	contador=1
	lista=doc.xpath("//PROVINCIA/NOMBRE/text()")
	for provincias in lista:
		if provincias.upper()==provincia.upper():
			indicador=True
	if indicador:
		print("Provincia detectada.")
		input("Pulse Enter para continuar.")
		dic=doc.xpath("//PROVINCIA[NOMBRE='%s']/CARRETERA/DENOMINACION/text()"%(provincia.title()))
		for estadisticas in dic:
			print("Carretera",contador,"-->",estadisticas)
			contador+=1
		dic2=doc.xpath("count(//PROVINCIA[NOMBRE='%s']//CARRETERA/RADAR)"%(provincia.title()))
		print("Hay",int(dic2),"radares.")
	else:
		print("Esta provincia no esta en nuestra base de datos.")
def pediryprovinciayradares(doc,carretera):
	indicador=False
	lista=doc.xpath("//CARRETERA/DENOMINACION/text()")
	for carreteras in lista:
		if carretera.upper()==carreteras.upper():
			indicador=True
	if indicador:
		print("Carretera detectada.")
		input("Presione Enter para continuar.")
		rad=doc.xpath("count(//CARRETERA[DENOMINACION='%s']/RADAR)"%(carretera.upper()))
		prov=doc.xpath("//CARRETERA[DENOMINACION='%s']/../NOMBRE/text()"%(carretera.upper()))
		for nombre in prov:
			print("Pasa por",nombre)
		print("Hay",int(rad),"radares.")
	else:
		print("Esta carretera no esta en nuestra base de datos.")
def pedirycoordenadas(doc,carretera):
	lista=doc.xpath("//CARRETERA/DENOMINACION/text()")
	indicador=False
	for carreteras in lista:
		if carretera.upper()==carreteras.upper():
			 indicador=True
	if indicador:
		print("Carretera detectada.")
		input("Pulse Enter para continuar.")
		rad=doc.xpath("count(//CARRETERA[DENOMINACION='%s']/RADAR)"%(carretera.upper()))
		print("Hay",int(rad),"radares.")
		LatitudesI=doc.xpath("//CARRETERA[DENOMINACION='%s']/RADAR/PUNTO_INICIAL/LATITUD/text()"%(carretera.upper()))
		LongitudesI=doc.xpath("//CARRETERA[DENOMINACION='%s']/RADAR/PUNTO_INICIAL/LONGITUD/text()"%(carretera.upper()))
		LatitudesF=doc.xpath("//CARRETERA[DENOMINACION='%s']/RADAR/PUNTO_FINAL/LATITUD/text()"%(carretera.upper()))
		LongitudesF=doc.xpath("//CARRETERA[DENOMINACION='%s']/RADAR/PUNTO_FINAL/LONGITUD/text()"%(carretera.upper()))
		for i in range(0,int(rad)):
			print("Radar",i,":")
			print("Latitud Inicial:",LatitudesI[i])
			print("Longitud Inicial:",LongitudesI[i])
			print("Latitud Final:",LatitudesF[i])
			print("Longitud Final:",LongitudesF[i])
			url='https://www.openstreetmap.org/directions?engine=graphhopper_car&route='+LatitudesI[i]+'%2C'+LongitudesI[i]+'%3B'+LatitudesF[i]+'%2C'+LongitudesF[i]+'#map=12/39.0407/-1.8079&layers=N'
			print(url)

	else:
		print("Esa carretera no esta en nuestra base de datos.")
opciones='''1.Listar Provincias
2.Cantidad Radares
3.Pedir Provincia y dar cantidad de radares y carreteras
4.Pedir Carretera y mostrar las provincias y radares
5.Pedir Carretera y contar radares,coordenadas y URL
0.Salir'''
doc=etree.parse('radares.xml')
opcion=int
while opcion!=0:
	print(opciones)
	try:
		opcion=int(input("Dime la opción. "))
	except:
		print("Debes introducir un numero entero.")
	else:
		if opcion==1:
			for provincias in listar_provincia(doc):
				print(provincias)
		elif opcion==2:
			print("Hay",int(contar_radares(doc)),"radares")
		elif opcion==3:
			provincia=str(input("¿Cual es la provincia? "))
			pedirycarreteraradares(doc,provincia)
		elif opcion==4:
			lista=doc.xpath("//CARRETERA/DENOMINACION/text()")
			for carreteras in lista:
				print(carreteras)
			carretera=str(input("¿Cual es la carretera? "))
			pediryprovinciayradares(doc,carretera)
		elif opcion==5:
			lista=doc.xpath("//CARRETERA/DENOMINACION/text()")
			for carreteras in lista:
				print(carreteras)
			carretera=str(input("¿Cual es la carretera? "))
			pedirycoordenadas(doc,carretera)
		elif opcion==0:
				print("Fin del programa.")
