from lxml import etree
import webbrowser
def listar_provincia(doc):
	listaP=doc.xpath("//RADAR/../../NOMBRE/text()")
	return listaP
def contar_radares(doc):
    lista=doc.xpath("count(//RADAR")
    return lista
def pediryestadisticas(doc,campeon):
    indicador=False
    listavar=['range','moveSpeed','armorBase','armorLevel','manaBase','manaLevel','criticalChanceBase','criticalChanceLevel','manaRegenBase','manaRegenLevel','healthRegenBase','healthRegenLevel','magicResistBase','magicResistLevel','healthBase','healthLevel','attackBase','attackLevel','ratingDefense','ratingMagic','ratingDifficulty','ratingAttack']
    lista=doc.xpath("//Champion/name/text()")
    listaE=doc.xpath("//Champion/estadisticas/range/text()")
    for campeones in lista:
        if campeon.upper()==campeones.upper():
            indicador=True
    if indicador:
        print("Campeon detectado.")
        input("Pulse Enter para continuar.")
        for var in listavar:
            print(var,end="")
            dic=doc.xpath("//Champion[name='%s']/estadisticas/%s/text()"%(campeon.capitalize(),var))
            for estadisticas in dic:
                print("-->",estadisticas)
    else:
        print("Ese campeon no esta en nuestra base de datos.")
def pedirhabilidad(doc,habilidad):
    lista=doc.xpath("//Champion/abilities/Ability/name/text()")
    indicador=False
    for habilidades in lista:
        if habilidad.upper()==habilidades.upper():
            indicador=True
    if indicador:
        print("Habilidad detectada.")
        input("Presione Enter para averiguar de que campeon se trata.")
        dic=doc.xpath("//Champion/abilities/Ability[name='%s']/../../name/text()"%habilidad.capitalize())
        for champion in dic:
            return champion
    else:
        print("Esa habilidad no esta en nuestra base de datos.")

def guiacampeon(doc,campeon):
    lista=doc.xpath("//Champion/name/text()")
    indicador=False
    for campeones in lista:
         if campeon.upper()==campeones.upper():
            indicador=True
    if indicador:
        print("Campeon detectado.")
        input("Pulse Enter para continuar.")
        webbrowser.open_new("https://euw.op.gg/champion/%s"%campeon.capitalize())
        system('echo "" && clear')
    else:
        print("Este campeon no esta en nuestra base de datos.")
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
			print("Hola")
		elif opcion==3:
			print("Adios")
		elif opcion==4:
			print("Jeje")
		elif opcion==5:
			print("Bye")
		elif opcion==0:
				print("Fin del programa.")

