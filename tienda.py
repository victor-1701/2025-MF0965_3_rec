class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):

       return f"{self.codigo}, {self.nombre}, {self.precio} €"

        


def buscar_producto(inventario, codigo_buscar):

    pass


def mostrar_inventario(inventario):

    print("\n--- INVENTARIO ACTUAL ---")
    
    if not inventario:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
                print(producto)



def calcular_valor_total(inventario):
    """
    COMPLETAR 5:
    Calcula y devuelve la suma de los precios de todos los productos en el inventario.
    """
    total = 0.0

    return total


def main():
    inventario = [
        Producto("PROD001", "Teclado Mecánico", 75.50),
        Producto("PROD002", "Mouse Inalámbrico", 25.00)
    ]

    while True:
        print("\n===============================")
        print("  MENÚ DE GESTIÓN DE INVENTARIO")
        print("===============================")
        print("1. Mostrar inventario")
        print("2. Buscar producto")
        print("3. Calcular valor total del inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            mostrar_inventario(inventario)
        elif opcion == '2':
            codigo_buscar = input("Ingrese el código del producto a buscar: ")
            producto_encontrado = buscar_producto(inventario, codigo_buscar)
            if producto_encontrado != None:
                print("Producto encontrado: ",  )

        elif opcion == '3':
            valor_total = calcular_valor_total(inventario)
            print(f"\n>> El valor total del inventario es: {valor_total:.2f} €")
        elif opcion == '4':
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija entre 1 y 4.")


if __name__ == "__main__":
    main()
