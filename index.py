# Menú de operaciones
print("Seleccione la operación:")
print("1. Suma")
print("2. Producto")
print("3. Division")
print("4. Factorial")
print("5. Tablas de multiplicar")
print("6. Calculo de cuadrado y cubo")
print("7. Promedio")
print("8. Maximo y minimo")

# Solicitar al usuario la elección
opcion = int(input("Ingrese el número de la operación deseada: "))

# Realizar la operación seleccionada
if opcion == 1:
    # Código para la suma
    pass
elif opcion == 2:
    # Código para el producto
    pass
elif opcion == 3:
    # Código para la división
    pass
elif opcion == 4:
    # Código para el factorial
    pass
elif opcion == 5:
    # Código para las tablas de multiplicar
    numero_tabla = int(input("Ingrese el número de tabla que desea imprimir: "))
    for i in range(1, 11):
        resultado = numero_tabla * i
        print(f"{numero_tabla} x {i} = {resultado}")
elif opcion == 6:
    # Código para el cálculo de cuadrado y cubo
    pass
elif opcion == 7:
    # Código para el promedio
    pass
elif opcion == 8:
    # Código para máximo y mínimo
    pass
else:
    print("Opción no válida. Por favor, elija una opción del 1 al 8.")


