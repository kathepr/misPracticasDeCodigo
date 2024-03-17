def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
	#La función en la que se puede cometer un error, se mete dentro de un bloque try - except
	try:		
		return num1/num2
	
	except ZeroDivisionError:      #Se escribe el nombre del error. 
		print("No se puede dividir entre cero")
		return None
		
		
	
#Vamos a manejar errores aquí. En casi de que la persona ingrese un valor distinto a un entero

while True:
	try: 	
		op1=(int(input("\nIntroduce el primer numero: ")))
		op2=(int(input("Introduce el segundo numero: ")))
		break	#Al leer el break, saldrá del bucle While, sin pasar por el except. 

	except ValueError: #Como estamos dentro de un bucle infinito y el break no fue leído, volverá a solicitar los valores
		print("Solo se permiten valores númericos enteros. Intentalo de nuevo.")


while True:
	try:
		print("""
		OPERACIONES MATEMATICAS 

		1. Suma
		2. Resta
		3. Multiplicación
		4. División 
			""")
		operacion=int(input("Introduce la operación matematica que deseas realizar: "))
		break
	except ValueError: 
		print("									OJO: Solo se permiten los valores númericos correspondientes con la operación matematica. Intentalo de nuevo.")



if operacion==1:
	print(suma(op1,op2))

elif operacion==2:
	print(resta(op1,op2))

elif operacion==3:
	print(multiplica(op1,op2))

elif operacion==4:
	resultado = divide(op1,op2)
	while resultado is None:
		op2 = int(input("Ingrese un divisor distinto de cero: "))
		resultado = divide(op1,op2)
	print(resultado)

else:
	print ("Operacion no contemplada. Vuela a intentarlo")



print("Operacion ejecutada. Continuacion de ejecucion del programa ")