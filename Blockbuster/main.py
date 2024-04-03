import tabulate
import modules.gestorGeneros as generos
import modules.gestorActores as actores
import modules.gestorFormatos as formatos
import modules.gestorPeliculas as peliculas

def gestorGeneros():
    while True: 
        print("""
          
        *****************************   
             Gestor de Géneros
        *****************************  
          
            1. Crear género
            2. Listar generos
            3. Ir Menu Principal
          
          """)
        
        try: 
            opcion = int(input("\nSeleccione una de las opciones: "))
        
            if opcion>=1 and opcion<4:
                if opcion == 1:
                    print(generos.crearGenero())
                elif opcion == 2:
                    print(generos.listarGeneros())
                elif opcion == 3:
                    break
            else:
                print("\nOJO: No existe esa opción, por favor vuelva a intentarlo")



        except ValueError:
            print("""
                  -----------------------------------------------------------------------------
                  Solo se permiten los NÚMEROS ENTEROS correspondientes a la OPCIÓN ESCOGIDA
                                        Por favor, intentelo de nuevo.
                  -----------------------------------------------------------------------------""")
            

def gestorActores():
    while True: 
        print("""
          
        *****************************   
             Gestor de Actores
        *****************************  
          
            1. Crear actores
            2. Listar actores
            3. Ir Menu Principal
          
          """)
        
        try: 
            opcion = int(input("\nSeleccione una de las opciones: "))
        
            if opcion>=1 and opcion<4:
                if opcion == 1:
                    print(actores.crearActores())
                elif opcion == 2:
                    print(actores.listarActores())
                elif opcion == 3:
                    break
            else:
                print("\nOJO: No existe esa opción, por favor vuelva a intentarlo")



        except ValueError:
            print("""
                  -----------------------------------------------------------------------------
                  Solo se permiten los NÚMEROS ENTEROS correspondientes a la OPCIÓN ESCOGIDA
                                        Por favor, intentelo de nuevo.
                  -----------------------------------------------------------------------------""")


def gestorFormatos():
    while True: 
        print("""
          
        *****************************   
             Gestor de Formatos
        *****************************  
          
            1. Crear formatos
            2. Listar formatos
            3. Ir Menu Principal
          
          """)
        
        try: 
            opcion = int(input("\nSeleccione una de las opciones: "))
        
            if opcion>=1 and opcion<4:
                if opcion == 1:
                    print(formatos.crearFormatos())
                elif opcion == 2:
                    print(formatos.listarFormatos())
                elif opcion == 3:
                    break
            else:
                print("\nOJO: No existe esa opción, por favor vuelva a intentarlo")



        except ValueError:
            print("""
                  -----------------------------------------------------------------------------
                  Solo se permiten los NÚMEROS ENTEROS correspondientes a la OPCIÓN ESCOGIDA
                                        Por favor, intentelo de nuevo.
                  -----------------------------------------------------------------------------""")
            

def gestorPeliculas():
    while True: 
        print("""
          
        *******************************
              Gestor de Peliculas
        *******************************
          
            1. Agregar pelicula
            2. Editar pelicula
            3. Eliminar Pelicula
            4. ELiminar Actor
            5. Buscar Pelicula
            6. Listar todas las peliculas
            7. Menu Principal
          
          """)
        
        try: 
            opcion = int(input("\nSeleccione una de las opciones: "))
        
            if opcion>=1 and opcion<8:
                if opcion == 1:
                    menuCliente()
                elif opcion == 2:
                    menuOficina()
                elif opcion == 3:
                    menuEmpleado()
                elif opcion == 4:
                    menuPedido()
                elif opcion == 5:
                    menuPago()
                elif opcion == 6:
                    menuProducto()
                elif opcion == 7:
                    break
            else:
                print("\nOJO: No existe esa opción, por favor vuelva a intentarlo")



        except ValueError:
            print("""
                  -----------------------------------------------------------------------------
                  Solo se permiten los NÚMEROS ENTEROS correspondientes a la OPCIÓN ESCOGIDA
                                        Por favor, intentelo de nuevo.
                  -----------------------------------------------------------------------------""")
            

def gestorInformes():
    while True: 
        print("""
          
        *******************************
                Gestor de Informes
        *******************************
          
            1. Listar las peliculas de un género en especifico
            2. Listar las peliculas donde la protagonista sea Kate Winslet
            3. Buscar pelicula y mostrar la sinopsis y actores
            4. Menu principal
          
          """)
        
        try: 
            opcion = int(input("\nSeleccione una de las opciones: "))
        
            if opcion>=1 and opcion<5:
                if opcion == 1:
                    menuCliente()
                elif opcion == 2:
                    menuOficina()
                elif opcion == 3:
                    menuEmpleado()
                elif opcion == 4:
                    break
            else:
                print("\nOJO: No existe esa opción, por favor vuelva a intentarlo")



        except ValueError:
            print("""
                  -----------------------------------------------------------------------------
                  Solo se permiten los NÚMEROS ENTEROS correspondientes a la OPCIÓN ESCOGIDA
                                        Por favor, intentelo de nuevo.
                  -----------------------------------------------------------------------------""")
            



if __name__ == "__main__":


    while True: 
        print("""
          
        *********************************************
            Sistema Gestor de Peliculas BlockBuster
        *********************************************
          
            1. Administrador de Generos
            2. Administrador de Actores
            3. Administrador de Formatos
            4. Gestor de Informes
            5. Gestor de Peliculas
            6. Salir
          
          """)
        
        try: 
            opcion = int(input("\nSeleccione una de las opciones: "))
        
            if opcion>=1 and opcion<6:
                if opcion == 1:
                    gestorGeneros()
                elif opcion == 2:
                    gestorActores()
                elif opcion == 3:
                    gestorFormatos()
                elif opcion == 4:
                    gestorInformes()
                elif opcion == 5:
                    gestorPeliculas()
                elif opcion == 6:
                    break
            else:
                print("\nOJO: No existe esa opción, por favor vuelva a intentarlo")



        except ValueError:
            print("""
                  -----------------------------------------------------------------------------
                  Solo se permiten los NÚMEROS ENTEROS correspondientes a la OPCIÓN ESCOGIDA
                                        Por favor, intentelo de nuevo.
                  -----------------------------------------------------------------------------""")
            