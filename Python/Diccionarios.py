dictionary = {"a":1,
              "e":2
              }

print (dictionary)
print (f"Clave a: {dictionary ['a']}")
print (f"Clave e: {dictionary ['e']}")

print ()

dictionary = {"numeros":[18,20,28],
              "groups":{"a":1, "b":2}}

print (dictionary)

print (f"Clave numeros: {dictionary ['numeros'][1]}")
print (f"Clave groups: {dictionary ['groups']['b']}")