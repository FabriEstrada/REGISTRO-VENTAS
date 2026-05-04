def Registro_Ventas(nombre,cantidad,precio):
    with open('ventas.txt','a',encoding='utf-8') as archivo:
        total_pago = cantidad *precio
        archivo.write(f"{nombre},{cantidad},{precio},{total_pago}\n")
        print(f"Se introdujo el producto: {nombre}\n")

def Mostrar_Ventas():
    try:
        with open('ventas.txt','r',encoding='utf-8') as archivo:
            contenido = archivo.readlines()
            for linea in contenido:
                if contenido:
                    print(f"{linea.strip()}\n")
                
                else:
                    print("No se ha registrado elementos")
    
    except FileNotFoundError:
        print("El archivo mencionado no se ha encontrado")

def Ingreso_Datos():
    nombre_producto = input("Introduce el nombre del producto:\t")
    
    while True:
        try:
            cantidad_producto = int(input("Introduce la cantidad del producto:\t"))
            precio_producto = float(input("Introduce el precio del producto:\t"))
            break
        
        except ValueError:
            print("Error al ingresar los datos, vuelve a intentarlo")
    
    return nombre_producto, cantidad_producto, precio_producto

while True:
    print("----REGISTRO DE VENTAS----")
    print("1. REGISTRAR VENTAS       ")
    print("2. MOSTRAR VENTAS         ")
    print("3. SALIR DEL PROGRAMA     ")
    
    opcion_usuario = input("Ingrese una opcion:\t")
    
    match opcion_usuario:
        case "1":
            nombre,cantidad,precio = Ingreso_Datos()
            Registro_Ventas(nombre,cantidad,precio)
        
        case "2":
            Mostrar_Ventas()
        
        case "3":
            print("Finalizando el programa")
            break
        
        case _:
            print("Opcion invalida, vuelve a intentarlo\n")
    