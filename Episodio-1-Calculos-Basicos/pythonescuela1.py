#Escuela De Python Primer Episodio!
print("Escuela de Python Primer Episodio!")
# Variables
coches = 90
espacio_en_un_coche = 4.0 #Caven 4.0 personas en un coche
conductores = 40
turistas = 100
#Detalles Más avanzados sobre mis Variables! Expressiones avanzadas!
coches_conducidos = conductores
coches_no_conducidos = coches - conductores # 50 coches se quedaron en el garaje fuera de servicio
todas_las_personas_cuales_pueden_viajar = espacio_en_un_coche * coches_conducidos # Esto es igual a 160 personas
turistas_que_caven_en_solo_un_coche = turistas / conductores
turistas_en_un_coche = espacio_en_un_coche - 1
turistas_en_1_coche = turistas_en_un_coche
turistas_en_un_coche = turistas_que_caven_en_solo_un_coche
maximo_turistas_que_pueden_viajar = todas_las_personas_cuales_pueden_viajar - conductores # Esto es igual a 120
#Preguntas cuales deben ser respondidos
# 1) Cuantos coches hay total hoy?
# 2) Cuantos conductores hay hoy?
# 3) Cuantos coches quedan en el garaje?
# 4) Cuantas personas caven en los coches con los conductores contados?
# 5) Cuantas turistas viajan hoy maximo?
# 6) Cuantas turistas caven en un solo coche sin el conductor contado?
# Respuestas
print("Respuestas")
print("Hoy hay un total de", coches, "choches")
print("Pero solamente hay", conductores, "Personas trabajando como conductores!")
print("Por eso", coches_no_conducidos, "Coches quedan en el garaje hoy!")
print("Hoy maximo", todas_las_personas_cuales_pueden_viajar, "caven en los viajes con los conductores contados!")
print("Hoy solamente", maximo_turistas_que_pueden_viajar, "turistas viajan con nosotros!")
print("En un coche maximo caven", (turistas_que_caven_en_solo_un_coche + turistas_que_caven_en_solo_un_coche%1), "personas en un coche")