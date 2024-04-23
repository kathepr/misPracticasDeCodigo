string = input("Introduce un string para invertirlo: ")
string_invertida=""

for character in string:
    string_invertida = character + string_invertida
   
print (f"String invertida: ",(string_invertida))