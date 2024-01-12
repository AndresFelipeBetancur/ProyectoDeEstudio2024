"""
Aquí se va a escribir el codigo del programa.
"""

#LISTAS Y VARIABLES PARA EL PROGRAMA
valorTarifas  = [0,0,0]

#FUNCIONES DEL PROGRAMA 

def menuPrincipal():
    print("""
¡Bienvenid@ al sistema de gestión del parqueadero!

SELECIONE UNA OPCIÓN

Menú Principal
1. Tarifas
2. Ingresar vehículo
3. Buscar vehículo
4. Mostrar Registros
5. Salida vehículo
6. Buscar Factura
7. Cuadre de Caja
8. Salir""")
    opcion = int(input("Selecione una opción "))
    if opcion == 1:
        return tarifas()
        

def tarifas():
    print("""
APARTADO DE TARIFAS
          
1. Ingresar Tarifas
2. Mostrar Tarifas
3. Modificar Tarifas
4. Regresar al Menú principal
""")
    opcion = int(input("Selecione una opción "))
    
    if opcion == 1:
        print("""
1. Ingresar Tarifa de Automóvil
2. Ingresar Tarifa de Motocicleta
3. Ingresar Tarifa de Bicicleta
4. Regresar al sub Menú Tarifas""")
        opcion = int(input("Selecione una opción "))
        if opcion == 1:
            valorTarifas[0] = int(input("Ingrese la tarifa para automoviles "))
            return tarifas()
        elif opcion == 2:
            valorTarifas[1] = int(input("Ingrese la tarifa para motocicletas "))
            return tarifas()
        elif opcion == 3:
            valorTarifas[2] = int(input("Ingrese la tarifa para bicibletas "))
            return tarifas()
        elif opcion == 4:
            return tarifas()
        else:
            print("Lo siento el valor ingresado no corresponde a una opcion valida")
            tarifas()
    if opcion == 2:
        print(f"""El valor de la tarifa de automovil es: {valorTarifas[0]},
El valor de la tarifa de motocicletas es: {valorTarifas[1]},
El valor de la tarifa de bicicletas es {valorTarifas[2]}.""")
        opcion = int(input("¿Desea regresar el sub modulo tarifas? 1=si 2=no "))
        if opcion == 1:
            return tarifas()
        elif opcion == 2: 
            return menuPrincipal()
        else:
            print("La opcion ingresada no es valida.")
    if opcion == 3:
        print(""" MODIFICAR TARIFAS:
1. Modificar Tarifa Automóvil
2. Modificar Tarifa Motocicleta
3. Modificar Tarifa Bicicleta
4. Regresar al sub Menú Tarifas""")
        opcion = int(input("Selecione una opción "))
        if opcion == 1:
            valorTarifas[0] = int(input("Ingrese el nuevo valor de la tarifa para automoviles "))
            return tarifas()
        elif opcion == 2:
            valorTarifas[1] = int(input("Ingrese el nuevo valor de la tarifa para motocicletas "))
            return tarifas()
        elif opcion == 3:
            valorTarifas[2] = int(input("Ingrese el nuevo valor de la tarifa para bicibletas "))
            return tarifas()
        elif opcion == 4:
            return tarifas()
        else:
            print("La opción selecionada no es valida.")
            return tarifas()
    elif opcion == 4:
        return menuPrincipal() 
    
#APARTADO DE LLAMADA DE LA FUNCIÓN PRINCIPAL
menuPrincipal()