"""
Aquí se va a escribir el codigo del programa.
"""

#LISTAS Y VARIABLES PARA EL PROGRAMA
valorTarifas  = [0,0,0]
vehiculosIngresados = []
motosIngresadas = []
bicicletasIngresadas = []
consecutivoBicicleta = 000000
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
    elif opcion == 2:
        return ingresoVehiculos()
    elif opcion == 3:
        return buscarVehiculo()
    elif opcion == 4:
        return mostrarRegistros()

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
        placa = f"{tresLetras+ f'{tresNumeros}'}"
        
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
            consecutivoFactura = f"veh{vehiculosIngresados[-1][-1]+1}"
            infoVehiculo = [placa,horaDeIngreso,nombreCliente,salida,consecutivoFactura]
            vehiculosIngresados.append(infoVehiculo)
            print("El vehiculo se ha ingresado correctamente.")
            return menuPrincipal()
    elif opcion == "m" or opcion == "M":
        placa = input("Ingrese la placa de la moto, (tres letras seguida de dos números, seguida de una letra): ")  
        if len(placa)<6 or len(placa)>6:
            print("La longitud de la placa no es valida.")
            return ingresoVehiculos()
        for i in range(0,len(motosIngresadas)):
            valor = motosIngresadas[i][0]
            if valor==placa:
                print("La placa ya esta registrada.")
                return ingresoVehiculos()
        horaDeIngreso = int(input("Ingrese la hora de ingreso en formato hhmm (horas,minutos) "))
        nombreCliente = input("Ingrese el nombre del cliente: ")
        salida = False
        if len(motosIngresadas) == 0:
            consecutivoFactura = 0
            infoMoto = [placa,horaDeIngreso,nombreCliente,salida,consecutivoFactura]
            motosIngresadas.append(infoMoto)
            print("La moto se ha ingresado correctamente.")
            print(f"El consecutivo es: {consecutivoFactura}")
            return menuPrincipal() 
                
        else: 
            consecutivoFactura = motosIngresadas[-1][-1]+1
            infoMoto = [placa,horaDeIngreso,nombreCliente,salida,consecutivoFactura]
            motosIngresadas.append(infoMoto)
            print("La moto se ha ingresado correctamente.")
            print(f"El consecutivo es: {consecutivoFactura}")
            return menuPrincipal()
    elif opcion == "b" or opcion == "B":
        if len(bicicletasIngresadas)<1:
            consecutivoBicicleta = 111111 + 1
        else:
            consecutivoBicicleta = bicicletasIngresadas[-1][0]+1
        horaDeIngreso = int(input("Ingrese la hora de ingreso en formato hhmm (horas,minutos) "))
        nombreCliente = input("Ingrese el nombre del cliente: ")
        salida = False
        if len(bicicletasIngresadas) == 0:
            consecutivoFactura = 0
            infoBici = [f"{consecutivoBicicleta}",horaDeIngreso,nombreCliente,salida,consecutivoFactura]
            bicicletasIngresadas.append(infoBici)
            print("La bicicleta se ha ingresado correctamente.")
            print(f"Su consecutivo es {infoBici[0]}")
            return menuPrincipal() 
                
        else: 
            consecutivoFactura = bicicletasIngresadas[-1][-1]+1
            infoBici= [f"{consecutivoBicicleta}",horaDeIngreso,nombreCliente,salida,consecutivoFactura]
            bicicletasIngresadas.append(infoBici)
            print("La bicicleta se ha ingresado correctamente.")
            print(f"Su consecutivo es {infoBici[0]}")
            return menuPrincipal()


def buscarVehiculo():
    print("""1. Buscar motos
2. Buscar automóviles
3. Buscar bicicletas
4. Regresar al menú principal""")
    opcion = input("Selecione una opción: ")
    if opcion=="1":
        placa = input("Ingrese la placa de la moto: ") 
        for i in range(0,len(motosIngresadas)):
            valor = motosIngresadas[i][0].index(placa)
            if len(f"{valor}")>0:
                #print(motosIngresadas[i])
                print(f"""Factura No: {motosIngresadas[i][-1]}
Num Placa: {motosIngresadas[i][0]}
Vehículo tipo: Moto
Hora de ingreso: {motosIngresadas[i][1]}
Hora de salida: 1235
Nombre: {motosIngresadas[i][2]}
Numero minutos : 60
Total: 1800""")
                opcion = input("¿Desea regresar? si=1, no=2 ")
                if opcion == "1":
                    return buscarVehiculo()
                else:
                    return menuPrincipal()
            else:
                print("la placa ingresada no esta registrada.")
                return menuPrincipal()
           
    elif opcion=="2":
        placa = input("Ingrese la placa del automovil: ") 
        
        for i in range(0,len(vehiculosIngresados)):
            valor = vehiculosIngresados[i][0].index(placa)
            if len(f"{valor}")>0:
                
                print(f"""Factura No: {vehiculosIngresados[i][-1]}
Num Placa: {vehiculosIngresados[i][0]}
Vehículo tipo: Moto
Hora de ingreso: {vehiculosIngresados[i][1]}
Hora de salida: 1235
Nombre: {vehiculosIngresados[i][2]}
Numero minutos : 60
Total: 1800""")
                opcion = input("¿Desea regresar? si=1, no=2 ")
                if opcion == "1":
                    return buscarVehiculo()
                else:
                    return menuPrincipal()
            else:
                print("la placa ingresada no esta registrada.")
                return menuPrincipal()
        
    elif opcion=="3":
        consecutivo = input("Ingrese el consecutivo de la bicicleta: ")
        
        for i in range(0,len(bicicletasIngresadas)):
            valor = bicicletasIngresadas[i][0].index(f"{consecutivo}")
            if len(f"{valor}")>0:
                
                print(f"""Factura No: {bicicletasIngresadas[i][-1]}
Consecutivo bicibleta: {bicicletasIngresadas[i][0]}
Vehículo tipo: bicicleta
Hora de ingreso: {bicicletasIngresadas[i][1]}
Hora de salida: 1235
Nombre: {bicicletasIngresadas[i][2]}
Numero minutos : 60
Total: 1800""")
                opcion = input("¿Desea regresar? si=1, no=2 ")
                if opcion == "1":
                    return buscarVehiculo()
                else:
                    return menuPrincipal()
            else:
                print("la placa ingresada no esta registrada.")
                return menuPrincipal()
        
        
    elif opcion=="4":
        return menuPrincipal()
    else:
        print("La opción no esta disponible.") 
        return menuPrincipal()
        
def mostrarRegistros():
    print("""1. Mostrar todos los automóviles .
2. Mostrar todas las motocicletas.
3. Mostrar todas las bicicletas
4. Regresar al menú principal.""")
    opcion = input("Selecione una opción: ")
    if opcion == "1":
        if len(vehiculosIngresados)<1:
            print("No se encontrarón registros.")
            return mostrarRegistros()
        print("FACTURA  PLACA   INGRESO   SALIDA   MINUTOS  TOTAL")
        for i in range(0,len(vehiculosIngresados)):
            
            print(f"""{i}        {vehiculosIngresados[i][0]}  {vehiculosIngresados[i][1]}      1200     120      4800""")
        
        opcionSalida = input("¿Desea regresar al submenu mostrar registros? si=1, no=2.")
        if opcionSalida == "1":
            mostrarRegistros()
        else: 
            menuPrincipal()
            
    elif opcion == "2":
        print("m")
    elif opcion == "3":
        print("m")
    elif opcion == "4":
        return menuPrincipal()
    else:
        print("Opción no valida.")
        return menuPrincipal()
    
#APARTADO DE LLAMADA DE LA FUNCIÓN PRINCIPAL
menuPrincipal()

