

# WHILE LOOP:
# while something_is_true:
#     Do something repeadly


from shutil import move


number_of_hurdels = 1
while number_of_hurdels <= 6:
    print("Hello")
    number_of_hurdels += 1 #Me ayuda a no crear un loop infinito, apenas llega al 6, sale del loop




number_of_hurdels = 6
while number_of_hurdels > 0:
    print("Hello Kath")
    number_of_hurdels -= 1 #Me ayuda a no crear un loop infinito, apenas llega al 6, sale del loop



# Con booleans
# while at_goal() != True:
#     pass_obstacule()

#Otra forma de escribir lo anterior
# while not at_goal():
#     pass_obstacule()



# while not at_goal():
#     if front_is_clear():
#         move()
    
#     else:
#         jump()


