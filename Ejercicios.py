print("\n##############################  'Creacion'  ##########################\n")
#Ejercicio 01
nombre = "Luis"
edad =19
registro={nombre:edad}
print("1. Registro es : ",registro)
#ejercicio 02
alimentos = dict({"fruta":"naranja","carne":"res","verdura":"apio"})
print("2. Alimento es : ",alimentos)
#ejercicio 03
nro_examen = [1,2,3]
calificacion = [15,16,17]
notas_finales=dict(zip(nro_examen,calificacion))
print("3. Las Notas Finales son : ",notas_finales)
#ejercicio 04
apellido = "Baldera"
codigo =182141
cod_univ={apellido:codigo}
print("4. Dni Universitario es : ",cod_univ)
#ejercicio 05
equip = dict({"inglaterra":"Liverpool","España":"RealMadrid","Alemania":"BayerMunich"})
print("5. Los mejores equipos de cada pais son : ",equip)
#Ejercicio 06
nro_partido = [1,2,3,4,5,6,7]
pntos_obt = [0,3,3,1,1,0,1]
fixture=dict(zip(nro_partido,pntos_obt))
print("6. Puntos obtenidos cada partido : ",fixture)
#Ejercicio 07
distr = "Tucume"
vid_hist =110
regist={distr:vid_hist}
print("7. Cuidad de las Piramides - Año de vida historica : ",regist)
#Ejercicio 08
equip_sud = dict({"Peru":"Universitario","Argentina":"Boca Juniors","Chile":"U de Chile","Brasil":"Flamengo"})
print("8. Mejor equipo de cada pais sudamericano : ",equip_sud)
#Ejercicio 09
gramy = ["Regueton","Bachata","Salsa","Regue"]
ganadores = ["Kevin Roldan","Romeo Santos","Mayimbe","Cultura  Profetica"]
gram_2019=dict(zip(gramy,ganadores))
print("9. Los Ganadores en cada Genero Musical son : ",gram_2019)
#Ejercicio 10
nom_art = "Arcangel"
nom_Real="Ostin Dos Santos Aveiro"
reg={nom_art:nom_Real}
print("10. Cantante y su nombre artistico : ",reg)
print("\n######################  'Pertenencia de Clave'  ########################\n")
#Ejercicio 1
notas = {"Juan": 20 , "Ana": 15, "Rosa":14}
texto = "Carlos"
if(texto in notas):
    print("1. El nombre '",texto,"' si existe en dic notas")
else:
    print("1. El nombre '",texto,"' no existe en dic notas")
#Ejercicio 2
equip = {"Peru":"Universitario" , "Brasil":"Corinthians", "Argentina":"Boca Juniors"}
tex= "Alianza Lima"
if(tex not in  equip):
    print("2. El equipo '",tex,"' no existe en el dicionario de mejores equipos de sudamerica")
else:
    print("2. El equipo '",tex,"' si existe en el dicionario de mejores equipos de sudamerica")
#Ejercicio 3
copas = {"Universitario": 25 , "Alianza Lima": 20, "Sporting Cristal":17}
text = "Sport Boys"
if(texto in copas):
    print("3. El nombre '",text,"' si existe en dic  de equipos mas coperos del Peru")
else:
    print("3. El nombre '",text,"' no existe en dic  de equipos mas coperos del Peru")
#Ejercicio 04
meritos = {"Eduardo": "Primer puesto" , "Alvaro": "Segundo Puesto", "Rosa":"Tercer puesto"}
texto = "Carlos"
if(texto not in meritos):
    print("4. El nombre '",texto,"' No existe en dic  de meritos")
else:
    print("4. El nombre '",texto,"' Si existe en dic de meritos")
#Ejercicio 05
regiones= {"Costa":"PERU" , "Sierra":"PERU", "Selva":"PERU" , "Mar Peruano":"Peru"}
texto = "zona Iceberg"
if(texto in regiones):
    print("5. La Region '",texto,"' es una de la regiones del Peru")
else:
    print("5. La Region '",texto,"' No es una de a regiones del Peru")
#Ejercicio 06
estad_animo= {"triste":"Luis" , "enojado":"Luis", "Feliz":"Luis" , "Pensativo":"Luis"}
tex = "Rebelde"
if(tex in estad_animo):
    print("6. '",tex,"' Es uno de los estados de animo de Luis")
else:
    print("6. '",tex,"' No es uno de los estados de animo de Luis")
#Ejercicio 07
sabores= {"Dulce":"sabor" , "Amargo":"sabor", "Acido":"sabor" , "Agrio":"sabor"}
text = "Salado"
if(text not in sabores):
    print("7. El Sabor'",text,"' No se encontro en el diccionario de sabores preferidos")
else:
    print("7. El Sabor'",text,"' Se encuentra en el diccionario de sabores preperidos")
#Ejercicio 08
deport_pref= {"Futbol":"Eduardo" , "Natacion":"Eduardo", "Atletismo":"Eduardo" , "Taekwondo":"Eduardo"}
tex = "Basquet"
if(tex in deport_pref):
    print("8. El '",tex,"' es uno de los deportes preferidos de Eduardo")
else:
    print("8. El '",tex,"' No es uno de lo deportes preferidos de Eduardo")
#Ejercicio 09
cursos_pref= {"Fisica":"Luis E." , "Programacion":"Luis E.", "Calculo con Aplicaiones":"Luis E."}
texto = "Circuitos Electricos"
if(texto in cursos_pref):
    print("9. El curso '",texto,"' es uno de los cursos preferidos de Luis")
else:
    print("9. El curso '",texto,"' No es uno de los cursos preferidos de Luis")
#Ejercicio 10
dia_disp= {"Lunes":"disponible" , "Miercoles":"disponible", "Viernes":"disponible" , "Sabado":"disponible"}
texto = "Martes"
if(texto in dia_disp):
    print("10. El '",texto,"' se encuentra disponible")
else:
    print("10. El '",texto,"' no se encuentra disponible")
print("\n######################  'Comparacion'  ########################\n")
#Ejercicio 01
GrupoA={1:10, 2:20, 3:15}
GrupoB={1:10, 2:20, 3:15}
print("1. GrupoA==GrupoB =>",GrupoA==GrupoB)
#Ejercicio 02
menu_casa={"Ceviche":"Edu", "Arroz Chaufa":"Edu", "Bisteq":"Edu"}
menu_calle={"Bisteq":"Edu", "Ceviche":"Edu","Arroz Chaufa":"Edu"}
print("2. Almuerzos en casa==Almuerzos en la Calle =>",menu_casa==menu_calle)
#Ejercicio 03
cev={"Cebolla picada":"Ceviche", "pesc. toyo":"Ceviche", "camote":"Ceviche"}
cev2={"Cebolla picada":"Ceviche", "pesc. Bonito":"Ceviche", "yuca frita":"Ceviche"}
print("3. Ceviche en tucume==ceviche en jayanca =>",cev!=cev2)
#Ejercicio 04
lapt_China={"Colores bajos":"Laptop", "bateria menos durablilidad":"Laptop", "garantia 1 año":"Laptop"}
lapt_Rusa={"Colores intesos":"Laptop", "bateria maxima durablilidad":"Laptop", "garantia 3 años":"Laptop"}
print("4. calidad de una laptop china==calidad de una laptop rusa =>",lapt_China==lapt_Rusa)
#Ejercicio 05
notas1={1:10, 2:20, 3:15}
notas2={1:10, 2:20, 3:15}
print("5. Resultados notas 1== Resultados notas 2 =>",notas1==notas2)
#Ejercicio 06
num_ingl={"two":2,"tree":3,"one":1}
num_ingl2={"one":1,"two":2,"tree":3}
print("6. Numeros en ingles==Numeros en ingles2  =>",num_ingl==num_ingl2)
#Ejercicio 07
Capit={"Peru":"Lima","Chile":"Santiago", "Argentina":"Buenos Aires"}
Capit2={"Peru":"Lima","Chile":"Arica", "Argentina":"Buenos Aires"}
print("7. Capitales==Capitales2 =>",Capit!=Capit2)
#Ejercicio 08
frutas_cost={"Platano":"Fruta de la costa","Naranja":"Fruta de la costa","Manzana":"Fruta de la costa"}
frutas_selv={"Mango":"Fruta de la selva","Papaya":"Fruta de la selva","Manzano":"Fruta de la selva"}
print("8. Frutas de la costa==Frutas de la selva =>",frutas_cost==frutas_selv)
#Ejercicio 09
costa={"Trigueño":"piel","Moreno":"piel","Blanco":"piel"}
sierra={"Moreno":"piel","Blanco":"piel","Trigueño":"piel"}
print("9. Colores de piel en la costa== Colores de piel en la Sierra =>",costa!=sierra)
#Ejercicio 10
pirkas={"Motocros":"juegos","Salto 3metros":"juegos","turcos":"juegos"}
Conoaqui={"Motocros":"juegos","Salto 3metros":"juegos","turcos":"juegos"}
print("10. Juegos en Pirkas==Juegos en Conoaqui =>",pirkas==Conoaqui)
print("\n######################  'Indexacion'  ########################\n")
#Ejercicio 1
candidatos={1:"samuel", 2:"patric", 3:"edu","color":"rojo"}
print("1. El Candidato numero 1 es para : ",candidatos[1])
#Ejercicio 2
cand_pres={"Peru2020":"Viscarra", "APRA":"Figuretti","Alianzapara el Retroceso":"payaso Acuña"}
print("2. El mejor presidente para el Peru es :",cand_pres["Peru2020"])
#Ejercicio 3
nota={"Nota primer examen":20, "Nota segundo examen":17, "Nota tercer examen":16.3}
print("3. La Mejor Nota de este semestre fue :",nota["Nota primer examen"])
#Ejercicio 4
pntos={"1ra sem":6, "2da sem":9, "3ra semana":4, "4ta semana":10}
print("4. Puntos obtenidos en la segunda semana de programacion:",pntos["2da sem"],"puntos")
#Ejercicio 5
simb={"paloma":"Paz","Plomo":"desierto","Azul":"mar","Celeste":"Cielo"}
print("5. La Paloma simboliza La",simb["paloma"])
#Ejercicio 6
gan={"15mil":"Franck","25mil":"Martin","pozomillonario":"Eduardo"}
print("6. El ganador del pozo Millonario es para:",gan["pozomillonario"])
#Ejercicio 7
cred={"Analisis Matematrico":4, "Programacion":5, "Matematica Basica":4,"Cuicuitos Electricos":2}
print("7. El curso de Programacion tiene :",cred["Programacion"],"Creditos")
#Ejercicio 8
gastos={"univ":25, "Comida":15, "Hospedaje":35,"pasajes":12}
print("8. El gasto diario en Hospedaje es:",gastos["Hospedaje"],"soles")
#Ejercicio 9
comedor={"lunes":"saltado de pollo","Martes":"Sudado de pescado","Miercoles":"Carne estofada","Viernes":"tallarines"}
print("9. Martes en el comedor de la Pedro se servira de cena:",comedor["Martes"])
#Ejercicio 10
partidos={"1er":"Estrella Roja", "2do":"Municipal", "3er":"Victoria","4to":"Racing"}
print("10. Arsenal enfrentara en la segunda fecha a:",partidos["2do"])
print("\n######################  'Longitud'  ########################\n")
#Ejercicio 1
candidatos={1:"samuel", 2:"patric", 3:"edu",4:"Matias"}
print("1. len=>",len(candidatos))
#Ejercicio 2
cand_pres={"Peru2020":"Viscarra", "APRA":"Figuretti","Alianzapara el Retroceso":"payaso Acuña"}
print("2. Len=>",len(cand_pres))
#Ejercicio 3
nota={"Nota primer examen":20, "Nota segundo examen":17, "Nota tercer examen":16.3}
print("3. len=>",len(nota))
#Ejercicio 4
pntos={"1ra sem":6, "2da sem":9, "3ra semana":4, "4ta semana":10}
print("4. len=>",len(pntos))
#Ejercicio 5
simb={"paloma":"Paz","Plomo":"desierto","Azul":"mar","Celeste":"Cielo"}
print("5. len=>",len(simb))
#Ejercicio 6
gan={"15mil":"Franck","25mil":"Martin","pozomillonario":"Eduardo"}
print("6. len=>",len(gan))
#Ejercicio 7
cred={"Analisis Matematrico":4, "Programacion":5, "Matematica Basica":4,"Cuicuitos Electricos":2}
print("7. len=>",len(cred))
#Ejercicio 8
gastos={"univ":25, "Comida":15, "Hospedaje":35,"pasajes":12}
print("8. len=>",len(gastos))
#Ejercicio 9
comedor={"lunes":"saltado de pollo","Martes":"Sudado de pescado","Miercoles":"Carne estofada","Viernes":"tallarines"}
print("9. len=>",len(comedor))
#Ejercicio 10
partidos={"1er":"Estrella Roja", "2do":"Municipal", "3er":"Victoria","4to":"Racing"}
print("10. len=>",len(partidos))
print("\n######################  'Iteracion'  ########################\n")
#Ejercicio 1
simb={"paloma":"Paz","Plomo":"desierto","Azul":"mar","Celeste":"Cielo"}
for key in simb:
    print("1. ",key)
#Ejercicio 2
gan={"15mil":"Franck","25mil":"Martin","pozomillonario":"Eduardo"}
for key in gan:
    print("2. ",key)
#Ejercicio 3
cred={"Analisis Matematrico":4, "Programacion":5, "Matematica Basica":4,"Cuicuitos Electricos":2}
for key in gan:
    print("3. ",key)
#Ejercicio 4
gastos={"univ":25, "Comida":15, "Hospedaje":35,"pasajes":12}
for key in gastos:
    print("4. ",key)
#Ejercicio 5
frutas={"Platano":"Fruta de la costa","Naranja":"Fruta de la costa","Manzana":"Fruta de la costa"}
for key in frutas:
    print("5. ",key)
#Ejercicio 6
candidatos={"Peru2020":"Viscarra", "APRA":"Figuretti","Alianza para el Retroceso":"payaso Acuña"}
for key in candidatos:
    print("6. ",key)
#Ejercicio 7
frutas_selv={"Mango":"Fruta de la selva","Papaya":"Fruta de la selva","Manzano":"Fruta de la selva"}
for key in frutas_selv:
    print("7. ",key)
#Ejercicio 8
Capit={"Peru":"Lima","Chile":"Santiago", "Argentina":"Buenos Aires"}
for k,v in zip(Capit.keys(), Capit.values()):
    print("8. ",k,v)
#Ejercicio 9
cred={"Analisis Matematrico":4, "Programacion":5, "Matematica Basica":4,"Circuitos Electricos":2}
for k,v in zip(cred.keys(), cred.values()):
    print("9. ",k,v)
#Ejercicio 10
nota={"Nota primer examen":20, "Nota segundo examen":17, "Nota tercer examen":16.3}
for k,v in nota.items():
    print("10.",k,v)
print("\n######################  'Busqueda'  ########################\n")
#Ejercicio 1
dni={"nombre":"Eduardo","apellido":"baldera","direccion":"calle 16 de febrero","distrito":"tucume"}
print("1. Mi nombre es: ",dni.get("nombre"))
#Ejercicio 2
equip = {"Inglaterra":"Liverpool","España":"RealMadrid","Alemania":"BayerMunich"}
print("2. El mejor equipo de Inglaterra es: ",equip.get("Inglaterra"))
#Ejercicio 3
alimentos = {"fruta":"Naranja","carne":"res","verdura":"apio"}
print("3. Mi fruta preferida  es la: ",alimentos.get("fruta"))
#Ejercicio 4
sud = {"Peru":"Universitario de Deportes","Argentina":"Boca Juniors","Chile":"U de Chile","Brasil":"Flamengo"}
print("4. El mejor equipo del Peru es: ",sud.get("Peru"))
#Ejercicio 5
sud = {"Peru":"Alianza Lima","Argentina":"River Plate","Chile":"Colo Colo","Brasil":"Atlt. Mineiro"}
print("5. El peor equipo del Peru es: ",sud.get("Peru"))
#Ejercicio 6
comedor={"lunes":"Saltado de pollo","Martes":"Sudado de pescado","Miercoles":"Carne estofada","Viernes":"tallarines"}
print("6. Lunes se cenara:",comedor.get("lunes"))
#Ejercicio 7
copas = {"Universitario": 25 , "Alianza Lima": 20, "Sporting Cristal":17}
print("7. Sporting Cristal",copas.get("Sporting Cristal"),"Copas Ganadas")
#Ejercicio 8
cred={"Analisis Matematico":4, "Programacion":5, "Matematica Basica":4,"Cuicuitos Electricos":2}
print("8. Analisis Matematico tiene",cred.get("Analisis Matematico"),"creditos disponibles")
#Ejercicio 9
gastos={"univ":25, "Comida":15, "Hospedaje":35,"pasajes":12}
print("9. El gasto diario en comida es:",gastos.get("Comida"),"soles")
#Ejercicio 10
menu={"Desayuno":"tortitas de maiz","Almuerzo":"Arroz Chaufa","lonche":"Bisteq"}
print("10.El desayuno en mi caa sera:",menu.get("Desayuno"))
print("\n######################  'Eliminacion'  ########################\n")
#Ejercicio 1
candidatos={1:"samuel", 2:"patric", 3:"edu",4:"Matias"}
del candidatos[1]
print("1.",candidatos)
#Ejercicio 2
cand={"Peru2020":"Viscarra", "APRA":"Figuretti","Alianzapara el Retroceso":"payaso Acuña"}
del cand["Peru2020"]
print("2.",cand)
#Ejercicio 3
nota={"Nota primer examen":20, "Nota segundo examen":17, "Nota tercer examen":16.3}
del nota["Nota primer examen"]
print("3.",nota)
#Ejercicio 4
pntos={"1ra sem":6, "2da sem":9, "3ra semana":4, "4ta semana":10}
del pntos["4ta semana"]
print("4.",pntos)
#Ejercicio 5
simb={"paloma":"Paz","Plomo":"desierto","Azul":"mar","Celeste":"Cielo"}
del simb["Azul"]
print("5.",simb)
#Ejercicio 6
gan={"15mil":"Franck","25mil":"Martin","pozomillonario":"Eduardo"}
del gan["25mil"]
print("6.",gan)
#Ejercicio 7
cred={"Analisis Matematrico":4, "Programacion":5, "Matematica Basica":4,"Circuitos Electricos":2}
del cred["Circuitos Electricos"]
print("7.",cred)
#Ejercicio 8
gastos={"univ":25, "Comida":15, "Hospedaje":35,"pasajes":12}
del gastos["Hospedaje"]
print("8.",gastos)
#Ejercicio 9
comedor={"lunes":"saltado de pollo","Martes":"Sudado de pescado","Miercoles":"Carne estofada","Viernes":"tallarines"}
del comedor["Miercoles"]
print("9.",comedor)
#Ejercicio 10
partidos={"1er":"Estrella Roja", "2do":"Municipal", "3er":"Victoria","4to":"Racing"}
del partidos["3er"]
print("10.",partidos)
print("\n######################  'Reemplazo'  ########################\n")
#Ejercicio 1
dni={"nombre":"eduardo","apellido":"baldera","direccion":"calle 16 de febrero","distrito":"tucume",}
print("1.1",dni)
dni["nombre"]="Carlos"
print("1.2",dni)
#Ejercicio 2
cand={"Peru2020":"Viscarra", "APRA":"Figuretti","Alianza para el Retroceso":"payaso Acuña"}
print("2.1",cand)
cand["Alianza para el retroceso"]="Payasita Araos"
print("2.2",cand)
#Ejercicio 3
nota={"Nota primer examen":20, "Nota segundo examen":17, "Nota tercer examen":16.3}
print("3.1",nota)
nota["Nota primer examen"]=00
print("3.2",nota)
#Ejercicio 4
pntos={"1ra sem":6, "2da sem":9, "3ra semana":4, "4ta semana":10}
print("4.1",pntos)
pntos["4ta semana"]=2
print("4.2",pntos)
#Ejercicio 5
simb={"paloma":"Paz","Plomo":"desierto","Azul":"mar","Celeste":"Cielo"}
print("5.1",simb)
simb["Azul"]="Nublado"
print("5.2",simb)
#Ejercicio 6
gan={"15mil":"Franck","25mil":"Martin","pozomillonario":"Eduardo"}
print("6.1",gan)
gan["pozomillonario"]="Luis"
print("6.2",gan)
#Ejercicio 7
cred={"Analisis Matematrico":4, "Programacion":5, "Matematica Basica":4,"Circuitos Electricos":2}
print("7.1",cred)
cred["Matematica Basica"]=6
print("7.2",cred)
#Ejercicio 8
gastos={"univ":25, "Comida":15, "Hospedaje":35,"pasajes":12}
print("8.1",gastos)
gastos["Hospedaje"]=50
print("8.2",gastos)
#Ejercicio 9
comedor={"lunes":"saltado de pollo","Martes":"Sudado de pescado","Miercoles":"Carne estofada","Viernes":"tallarines"}
print("9.1",comedor)
comedor["lunes"]="Chuleta"
print("9.2",comedor)
#Ejercicio 10
partidos={"1er":"Estrella Roja", "2do":"Municipal", "3er":"Victoria","4to":"Racing"}
print("10.1",partidos)
partidos["1er"]="Carlos Stein"
print("10.2",partidos)
print("\n######################  'Agregado'  ########################\n")
#Ejercicio 1
dni={"nombre":"eduardo","apellido":"baldera","direccion":"calle 16 de febrero","distrito":"tucume",}
print("1.1",dni)
dni.setdefault("donacion de organos","no")
print("1.2",dni)
#Ejercicio 2
cand={"Peru2020":"Viscarra", "APRA":"Figuretti","Alianza para el Retroceso":"payaso Acuña"}
print("2.1",cand)
cand.setdefault("Creciendo Peru","Urresti")
print("2.2",cand)
#Ejercicio 3
nota={"Nota primer examen":20, "Nota segundo examen":17, "Nota tercer examen":16.3}
print("3.1",nota)
nota.setdefault("Sustitutorio",14)
print("3.2",nota)
#Ejercicio 4
pntos={"1ra sem":6, "2da sem":9, "3ra semana":4, "4ta semana":10}
print("4.1",pntos)
pntos.setdefault("5ta semana",5)
print("4.2",pntos)
#Ejercicio 5
simb={"paloma":"Paz","Plomo":"desierto","Azul":"mar","Celeste":"Cielo"}
print("5.1",simb)
simb.setdefault("calavera","Peligro")
print("5.2",simb)
#Ejercicio 6
gan={"15mil":"Franck","25mil":"Martin","pozomillonario":"Eduardo"}
print("6.1",gan)
gan.setdefault("5mil","Luis")
print("6.2",gan)
#Ejercicio 7
cred={"Analisis Matematrico":4, "Programacion":5, "Matematica Basica":4,"Circuitos Electricos":4}
print("7.1",cred)
cred.setdefault("Identidad Nacional",1)
print("7.2",cred)
#Ejercicio 8
gastos={"univ":25, "Comida":15, "Hospedaje":35,"pasajes":12}
print("8.1",gastos)
gastos.setdefault("copias",3)
print("8.2",gastos)
#Ejercicio 9
comedor={"lunes":"saltado de pollo","Martes":"Sudado de pescado","Miercoles":"Carne estofada","Viernes":"tallarines"}
print("9.1",comedor)
comedor.setdefault("Jueves","Chancho a la Parrilla")
print("9.2",comedor)
#Ejercicio 10
partidos={"1er":"Estrella Roja", "2do":"Municipal", "3er":"Victoria","4to":"Racing"}
print("10.1",partidos)
partidos.setdefault("5to","Estudiantes")
print("10.2",partidos)
print("\n######################  'Anulacion'  ########################\n")
dni={"nombre":"eduardo","apellido":"baldera","direccion":"calle 16 de febrero","distrito":"tucume",}
print("1.1",dni)
dni.clear()
print("1.2",dni)
#Ejercicio 2
cand={"Peru2020":"Viscarra", "APRA":"Figuretti","Alianza para el Retroceso":"payaso Acuña"}
print("2.1",cand)
cand.clear()
print("2.2",cand)
#Ejercicio 3
nota={"Nota primer examen":20, "Nota segundo examen":17, "Nota tercer examen":16.3}
print("3.1",nota)
nota.clear()
print("3.2",nota)
#Ejercicio 4
pntos={"1ra sem":6, "2da sem":9, "3ra semana":4, "4ta semana":10}
print("4.1",pntos)
pntos.clear()
print("4.2",pntos)
#Ejercicio 5
simb={"paloma":"Paz","Plomo":"desierto","Azul":"mar","Celeste":"Cielo"}
print("5.1",simb)
simb.clear()
print("5.2",simb)
#Ejercicio 6
gan={"15mil":"Franck","25mil":"Martin","pozomillonario":"Eduardo"}
print("6.1",gan)
gan.clear()
print("6.2",gan)
#Ejercicio 7
cred={"Analisis Matematrico":4, "Programacion":5, "Matematica Basica":4,"Circuitos Electricos":4}
print("7.1",cred)
cred.clear()
print("7.2",cred)
#Ejercicio 8
gastos={"univ":25, "Comida":15, "Hospedaje":35,"pasajes":12}
print("8.1",gastos)
gastos.clear()
print("8.2",gastos)
#Ejercicio 9
comedor={"lunes":"saltado de pollo","Martes":"Sudado de pescado","Miercoles":"Carne estofada","Viernes":"tallarines"}
print("9.1",comedor)
comedor.clear()
print("9.2",comedor)
#Ejercicio 10
partidos={"1er":"Estrella Roja", "2do":"Municipal", "3er":"Victoria","4to":"Racing"}
print("10.1",partidos)
partidos.clear()
print("10.2",partidos)
print("\n######################  'Clonado'  ########################\n")
#Ejercicio 1
dni={"nombre":"eduardo","apellido":"baldera","direccion":"calle 16 de febrero","distrito":"tucume",}
print("1.1",dni)
nuevo_dni=dni.copy()
print("1.2",nuevo_dni)
#Ejercicio 2
cand={"Peru2020":"Viscarra", "APRA":"Figuretti","Alianza para el Retroceso":"payaso Acuña"}
print("2.1",cand)
nuev_cand=cand.copy()
print("2.2",nuev_cand)
#Ejercicio 3
nota={"Nota primer examen":20, "Nota segundo examen":17, "Nota tercer examen":16.3}
print("3.1",nota)
list_notas=nota.copy()
print("3.2",list_notas)
#Ejercicio 4
pntos={"1ra sem":6, "2da sem":9, "3ra semana":4, "4ta semana":10}
print("4.1",pntos)
pntos2=pntos.copy()
print("4.2",pntos2)
#Ejercicio 5
simb={"paloma":"Paz","Plomo":"desierto","Azul":"mar","Celeste":"Cielo"}
print("5.1",simb)
icon=simb.copy()
print("5.2",icon)
#Ejercicio 6
gan={"15mil":"Franck","25mil":"Martin","pozomillonario":"Eduardo"}
print("6.1",gan)
suert=gan.copy
print("6.2",suert)
#Ejercicio 7
cred={"Analisis Matematrico":4, "Programacion":5, "Matematica Basica":4,"Circuitos Electricos":4}
print("7.1",cred)
cred_ing=cred.copy()
print("7.2",cred_ing)
#Ejercicio 8
gastos={"univ":25, "Comida":15, "Hospedaje":35,"pasajes":12}
print("8.1",gastos)
costos=gastos.copy()
print("8.2",costos)
#Ejercicio 9
comedor={"lunes":"saltado de pollo","Martes":"Sudado de pescado","Miercoles":"Carne estofada","Viernes":"tallarines"}
print("9.1",comedor)
com_popul=comedor.copy()
print("9.2",com_popul)
#Ejercicio 10
partidos={"1er":"Estrella Roja", "2do":"Municipal", "3er":"Victoria","4to":"Racing"}
print("10.1",partidos)
encuentros=partidos.copy()
print("10.2",encuentros)
print("\n######################  'Inserción'  ########################\n")
#Ejercicio 1
dni={"nombre":"eduardo","apellido":"baldera","direccion":"calle 16 de febrero","distrito":"tucume",}
print("1.1",dni)
dni["nombre"]="Daniel"
print("1.2",dni)
#Ejercicio 2
cand={"Peru2020":"Viscarra", "APRA":"Figuretti","Alianza para el Retroceso":"payaso Acuña"}
print("2.1",cand)
cand["Fuerza Popular"]="Chibolin"
print("2.2",cand)
#Ejercicio 3
nota={"Nota primer examen":20, "Nota segundo examen":17, "Nota tercer examen":16.3}
print("3.1",nota)
nota["Nota primer examen"]=7
print("3.2",nota)
#Ejercicio 4
pntos={"1ra sem":6, "2da sem":9, "3ra semana":4, "4ta semana":10}
print("4.1",pntos)
pntos["4ta semana"]=7
print("4.2",pntos)
#Ejercicio 5
simb={"paloma":"Paz","Plomo":"desierto","Azul":"mar","Celeste":"Cielo"}
print("5.1",simb)
simb["Azul"]="lluvia"
print("5.2",simb)
#Ejercicio 6
gan={"15mil":"Franck","25mil":"Martin","pozomillonario":"Eduardo"}
print("6.1",gan)
gan["pozomillonario"]="Daniel"
print("6.2",gan)
#Ejercicio 7
cred={"Analisis Matematrico":4, "Programacion":5, "Matematica Basica":4,"Circuitos Electricos":2}
print("7.1",cred)
cred["Matematica Basica"]=10
print("7.2",cred)
#Ejercicio 8
gastos={"univ":25, "Comida":15, "Hospedaje":35,"pasajes":12}
print("8.1",gastos)
gastos["Hospedaje"]=90
print("8.2",gastos)
#Ejercicio 9
comedor={"lunes":"saltado de pollo","Martes":"Sudado de pescado","Miercoles":"Carne estofada","Viernes":"tallarines"}
print("9.1",comedor)
comedor["lunes"]="Aeropuerto"
print("9.2",comedor)
#Ejercicio 10
partidos={"1er":"Estrella Roja", "2do":"Municipal", "3er":"Victoria","4to":"Racing"}
print("10.1",partidos)
partidos["5to"]="Cantolao"
print("10.2",partidos)
print("\n######################  'Extraccion'  ########################\n")
#Ejercicio 1
dni={"nombre":"eduardo","apellido":"baldera","direccion":"calle 16 de febrero","distrito":"tucume",}
print("1.1",dni)
iden={dni.pop("nombre"),dni.pop("apellido")}
print("1.2",iden)
#Ejercicio 2
cand={"Peru2020":"Viscarra", "APRA":"Figuretti","Alianza para el Retroceso":"payaso Acuña"}
print("2.1",cand)
ex_pres={cand.pop("peruposible","Toledo")}
print("2.2",ex_pres)
#Ejercicio 3
nota={"Nota primer examen":20, "Nota segundo examen":17, "Nota tercer examen":16.3}
print("3.1",nota)
grup=nota.popitem()
print("3.2",grup)
#Ejercicio 4
pntos={"1ra sem":6, "2da sem":9, "3ra sem":4, "4ta sem":10}
print("4.1",pntos)
extras={pntos.pop("1ra sem"),pntos.pop("3ra sem")}
print("4.2",extras)
#Ejercicio 5
simb={"paloma":"Paz","Plomo":"desierto","Azul":"mar","Celeste":"Cielo"}
print("5.1",simb)
icon={simb.pop("calavera","peligro")}
print("5.2",icon)
#Ejercicio 6
gan={"15mil":"Franck","25mil":"Martin","pozomillonario":"Eduardo"}
print("6.1",gan)
tink=gan.popitem()
print("6.2",tink)
#Ejercicio 7
cred={"Analisis Matematrico":4, "Programacion":5, "Matematica Basica":4,"Circuitos Electricos":2}
print("7.1",cred)
val={cred.pop("Matematica Basica")}
print("7.2",val)
#Ejercicio 8
gastos={"univ":25, "Comida":15, "Hospedaje":35,"pasajes":12}
print("8.1",gastos)
gas_ex={gastos.pop("copias","tmbn copias")}
print("8.2",gas_ex)
#Ejercicio 9
comedor={"lunes":"saltado de pollo","Martes":"Sudado de pescado","Miercoles":"Carne estofada","Viernes":"tallarines"}
print("9.1",comedor)
ahorro=comedor.popitem()
print("9.2",ahorro)
#Ejercicio 10
partidos={"1er":"Estrella Roja", "2do":"Municipal", "3er":"Victoria","4to":"Racing"}
print("10.1",partidos)
w_over={partidos.pop("2do")}
print("10.2",w_over)
print("\n######################  'Ver Claves'  ########################\n")
#Ejercicio 1
dni={"nombre":"eduardo","apellido":"baldera","direccion":"calle 16 de febrero","distrito":"tucume",}
print("1.",dni.keys())
#Ejercicio 2
cand={"Peru2020":"Viscarra", "APRA":"Figuretti","Alianza para el Retroceso":"payaso Acuña"}
print("2.",cand.keys())
#Ejercicio 3
nota={"Nota primer examen":20, "Nota segundo examen":17, "Nota tercer examen":16.3}
print("3.",nota.keys())
#Ejercicio 4
pntos={"1ra sem":6, "2da sem":9, "3ra sem":4, "4ta sem":10}
print("4.",pntos.keys())
#Ejercicio 5
simb={"paloma":"Paz","Plomo":"desierto","Azul":"mar","Celeste":"Cielo"}
print("5.",simb.keys())
#Ejercicio 6
gan={"15mil":"Franck","25mil":"Martin","pozomillonario":"Eduardo"}
print("6.",gan.keys())
#Ejercicio 7
cred={"Analisis Matematrico":4, "Programacion":5, "Matematica Basica":4,"Circuitos Electricos":2}
print("7.",cred.keys())
#Ejercicio 8
gastos={"univ":25, "Comida":15, "Hospedaje":35,"pasajes":12}
print("8.",gastos.keys())
#Ejercicio 9
comedor={"lunes":"saltado de pollo","Martes":"Sudado de pescado","Miercoles":"Carne estofada","Viernes":"tallarines"}
print("9.",comedor.keys())
#Ejercicio 10
partidos={"1er":"Estrella Roja", "2do":"Municipal", "3er":"Victoria","4to":"Racing"}
print("10.",partidos.keys())
print("\n######################  'Ver valores'  ########################\n")
#Ejercicio 1
dni={"nombre":"eduardo","apellido":"baldera","direccion":"calle 16 de febrero","distrito":"tucume",}
print("1.",dni.values())
#Ejercicio 2
cand={"Peru2020":"Viscarra", "APRA":"Figuretti","Alianza para el Retroceso":"payaso Acuña"}
print("2.",cand.values())
#Ejercicio 3
nota={"Nota primer examen":20, "Nota segundo examen":17, "Nota tercer examen":16.3}
print("3.",nota.values())
#Ejercicio 4
pntos={"1ra sem":6, "2da sem":9, "3ra sem":4, "4ta sem":10}
print("4.",pntos.values())
#Ejercicio 5
simb={"paloma":"Paz","Plomo":"desierto","Azul":"mar","Celeste":"Cielo"}
print("5.",simb.values())
#Ejercicio 6
gan={"15mil":"Franck","25mil":"Martin","pozomillonario":"Eduardo"}
print("6.",gan.values())
#Ejercicio 7
cred={"Analisis Matematrico":4, "Programacion":5, "Matematica Basica":4,"Circuitos Electricos":2}
print("7.",cred.values())
#Ejercicio 8
gastos={"univ":25, "Comida":15, "Hospedaje":35,"pasajes":12}
print("8.",gastos.values())
#Ejercicio 9
comedor={"lunes":"saltado de pollo","Martes":"Sudado de pescado","Miercoles":"Carne estofada","Viernes":"tallarines"}
print("9.",comedor.values())
#Ejercicio 10
partidos={"1er":"Estrella Roja", "2do":"Municipal", "3er":"Victoria","4to":"Racing"}
print("10.",partidos.values())
print("\n######################  'Coversión'  ########################\n")
#Ejercicio 1
dni={"nombre":"eduardo","apellido":"baldera","direccion":"calle 16 de febrero","distrito":"tucume",}
L=list(dni)
T=tuple(dni)
S=set(dni)
l=list(dni.values())
t=tuple(dni.values())
s=set(dni.values())
print("1.1",L)
print("1.2",T)
print("1.3",S)
print("1.4",l)
print("1.5",t)
print("1.6",s)
#Ejercicio 2
cand={"Peru2020":"Viscarra", "APRA":"Figuretti","Alianza para el Retroceso":"payaso Acuña"}
L=list(cand)
T=tuple(cand)
S=set(cand)
l=list(cand.values())
t=tuple(cand.values())
s=set(cand.values())
print("2.1",L)
print("2.2",T)
print("2.3",S)
print("2.4",l)
print("2.5",t)
print("2.6",s)
#Ejercicio 3
nota={"Nota primer examen":20, "Nota segundo examen":17, "Nota tercer examen":16.3}
L=list(nota)
T=tuple(nota)
S=set(nota)
l=list(nota.values())
t=tuple(nota.values())
s=set(nota.values())
print("3.1",L)
print("3.2",T)
print("3.3",S)
print("3.4",l)
print("3.5",t)
print("3.6",s)
#Ejercicio 4
pntos={"1ra sem":6, "2da sem":9, "3ra sem":4, "4ta sem":10}
L=list(pntos)
T=tuple(pntos)
S=set(pntos)
l=list(pntos.values())
t=tuple(pntos.values())
s=set(pntos.values())
print("4.1",L)
print("4.2",T)
print("4.3",S)
print("4.4",l)
print("4.5",t)
print("4.6",s)
#Ejercicio 5
simb={"paloma":"Paz","Plomo":"desierto","Azul":"mar","Celeste":"Cielo"}
L=list(simb)
T=tuple(simb)
S=set(simb)
l=list(simb.values())
t=tuple(simb.values())
s=set(simb.values())
print("5.1",L)
print("5.2",T)
print("5.3",S)
print("5.4",l)
print("5.5",t)
print("5.6",s)
#Ejercicio 6
gan={"15mil":"Franck","25mil":"Martin","pozomillonario":"Eduardo"}
L=list(gan)
T=tuple(gan)
S=set(gan)
l=list(gan.values())
t=tuple(gan.values())
s=set(gan.values())
print("6.1",L)
print("6.2",T)
print("6.3",S)
print("6.4",l)
print("6.5",t)
print("6.6",s)
#Ejercicio 7
cred={"Analisis Matematrico":4, "Programacion":5, "Matematica Basica":4,"Circuitos Electricos":2}
L=list(cred)
T=tuple(cred)
S=set(cred)
l=list(cred.values())
t=tuple(cred.values())
s=set(cred.values())
print("7.1",L)
print("7.2",T)
print("7.3",S)
print("7.4",l)
print("7.5",t)
print("7.6",s)
#Ejercicio 8
gastos={"univ":25, "Comida":15, "Hospedaje":35,"pasajes":12}
T=tuple(gastos)
S=set(gastos)
l=list(gastos.values())
t=tuple(gastos.values())
s=set(gastos.values())
print("8.1",L)
print("8.2",T)
print("8.3",S)
print("8.4",l)
print("8.5",t)
print("8.6",s)
#Ejercicio 9
comedor={"lunes":"saltado de pollo","Martes":"Sudado de pescado","Miercoles":"Carne estofada","Viernes":"tallarines"}
L=list(comedor)
T=tuple(comedor)
S=set(comedor)
l=list(comedor.values())
t=tuple(comedor.values())
s=set(comedor.values())
print("9.1",L)
print("9.2",T)
print("9.3",S)
print("9.4",l)
print("9.5",t)
print("9.6",s)
#Ejercicio 10
partidos={"1er":"Estrella Roja", "2do":"Municipal", "3er":"Victoria","4to":"Racing"}
L=list(partidos)
T=tuple(partidos)
S=set(partidos)
l=list(partidos.values())
t=tuple(partidos.values())
s=set(partidos.values())
print("10.1",L)
print("10.2",T)
print("10.3",S)
print("10.4",l)
print("10.5",t)
print("10.6",s)
