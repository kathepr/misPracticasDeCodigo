#------------------------------------------------------------------
#                              VALIDACIONES
#------------------------------------------------------------------
def validar_input(patron, mensaje):
    while True: 
        entrada = input(mensaje)
        if patron.match(entrada):
            confirmacion = input(f"¿Confirma el ingreso de este dato '{entrada}'? (S/N) ").strip().lower()
            if confirmacion == "s":
                return entrada
        else:
            print("El dato no cumple con los parametros establecidos. Vuelva a intentarlo.")