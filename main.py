def Registro_Ventas(nombre,cantidad,precio):
    with open('REGISTRO-VENTAS/ventas.txt','a',encoding='utf-8') as archivo:
        total_pago = cantidad *precio
        archivo.write(f"{nombre},{cantidad},{precio},{total_pago}\n")
        print(f"Se introdujo el producto: {nombre}\n")

def Mostrar_Ventas():
    try:
        with open('REGISTRO-VENTAS/ventas.txt','r',encoding='utf-8') as archivo:
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