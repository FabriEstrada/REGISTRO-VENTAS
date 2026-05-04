def Registro_Ventas(nombre,cantidad,precio):
    with open('REGISTRO-VENTAS/ventas.txt','a',encoding='utf-8') as archivo:
        total_pago = cantidad *precio
        archivo.write(f"{nombre},{cantidad},{precio},{total_pago}\n")
        print(f"Se introdujo el producto: {nombre}\n")