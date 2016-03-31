
#!/usr/bin/python
#-*- coding: utf-8 -*-

# Paso 1: Almacenar nuestros datos
nombres=[
	["Juan Lago", "juan.l33@gmail.com"],
	["Ericka Morales", "erymor@yahoo.com.mx"],["Diana Morales", 		"dmorales58@yahoo.com.mx"],["Margarita Calderon", 		"cavamaga2708@gmail"],	["Fernando Contreras", "fernandok@gmail.com"]]
print (nombres)

print

print("lista ordenada")

#paso2: Imprima la lista en orden alfabetico
#con nombre y email

#ordenamos la lista  con la instruccion .sort()
nombres.sort()

#paso 3: Imprima la lista con solo el nombre
# pero indique cuantas letras tiene cada nombre
print("")
print("Cantidad de letras")
print("")
for dato in nombres:
	caracteres = len (dato[0])-1
	print (dato[0] + " " + str(caracteres))


#paso 4:Imprima la lista con solo el dominio del email en otras palabras

print("")
print("Dominios")
print()

for nom in nombres:
	
	dominio = nom[1].split("@")[1]
	print (dominio) 


LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10 = True





