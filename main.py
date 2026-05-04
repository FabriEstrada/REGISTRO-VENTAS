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