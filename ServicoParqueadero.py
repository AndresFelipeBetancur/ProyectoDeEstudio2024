"""
Aquí se va a escribir el codigo del programa.
"""

#LISTAS Y VARIABLES PARA EL PROGRAMA
valorTarifas  = [0,0,0]
vehiculosIngresados = []
motosIngresadas = []
bicicletasIngresadas = []
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
    if opcion == 2:
        return ingresoVehiculos()
        

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
    
def ingresoVehiculos():
    opcion = input("Tipo de vehículo (a : automóvil, m: moto, b: bicicleta ): ") 
    if opcion == "a" or opcion == "A":
        tresLetras = input("Ingrese las 3 letras de su placa: ")

        if len(tresLetras) < 3 or len(tresLetras)>3:
            print("Las tres letras de la placa ingresadas no son validas.")
            print("Verifique la longitud y tipo de los valores ingresados.")
            return ingresoVehiculos()
        try:
            tresNumeros = int(input("Ingrese los 3 número de su placa: "))
        except ValueError:
            print("se deben de ingresar números")
            return ingresoVehiculos()
        if len(f"{tresNumeros}") < 3 or type(tresNumeros) != int or len(f"{tresNumeros}")>3:
            print("Los tres números de la placa ingresadas no son validas.")
            print("Verifique la longitud y tipo de los valores ingresados.")
            return ingresoVehiculos()
        placa = f"{tresLetras}+{tresNumeros}"
        
        for i in range(0,len(vehiculosIngresados)):
            valor = vehiculosIngresados[i][0]
            if valor==placa:
                print("La placa ya esta registrada.")
                return ingresoVehiculos()

        horaDeIngreso = int(input("Ingrese la hora de ingreso en formato hhmm (horas,minutos) "))
        if len(f"{horaDeIngreso}")>4:
            print("La hora ingresada no es valida.")
            return ingresoVehiculos()
        
        nombreCliente = input("Ingrese el nombre del cliente: ")
        
        if len(vehiculosIngresados)==0:
            salida = False
            consecutivoFactura = 0
            infoVehiculo = [placa,horaDeIngreso,nombreCliente,salida,consecutivoFactura]
            vehiculosIngresados.append(infoVehiculo)
            print("El vehiculo se ha ingresado correctamente.")
            return menuPrincipal()
        else:
            salida = False
            consecutivoFactura = [-1][-1]+1
            infoVehiculo = [placa,horaDeIngreso,nombreCliente,salida,consecutivoFactura]
            vehiculosIngresados.append(infoVehiculo)
            print("El vehiculo se ha ingresado correctamente.")
            return menuPrincipal()
            
#APARTADO DE LLAMADA DE LA FUNCIÓN PRINCIPAL
menuPrincipal()

"""
for i in placas:
                if placas[i] == placa:
                    print("La placa ingresada corresponde a un vehiculo ya registrado.")
                    return menuPrincipal()"""