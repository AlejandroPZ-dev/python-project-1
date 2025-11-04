def py0016():
    print("\n=== PY0016: Bucles y rangos de números ===")

    print("Del 0 al 20:")
    for i in range(0, 21):
        print(i, end=" ")
    print("\n")

    print("Pares del 0 al 20:")
    for i in range(0, 21, 2):
        print(i, end=" ")
    print("\n")

    print("Impares del 0 al -20:")
    for i in range(1, -21, -2):
        print(i, end=" ")
    print("\n")


def py0017():
    print("\n=== PY0017: Sumar números pares del 0 al 100 ===")
    pares = range(0, 101, 2)
    suma_pares = sum(pares)
    print(f"La suma de los números pares del 0 al 100 es: {suma_pares}")


def py0019():
    print("\n=== PY0019: Número impar con control de errores ===")
    while True:
        try:
            numero = int(input("Introduce un número impar: "))
            if numero % 2 != 0:
                print("Correcto, el número es impar.")
                break
            else:
                print("El número es par. Introduce un número impar.")
        except ValueError:
            print("Error: debes introducir un número entero impar.")


def py0014():
    print("\n=== PY0014: Media ponderada ===")
    try:
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        n3 = float(input("Introduce el tercer número: "))

        media = n1 * 0.15 + n2 * 0.35 + n3 * 0.50
        print(f"La media ponderada es: {media:.2f}")

    except ValueError:
        print("⚠️ Error: debes introducir valores numéricos válidos.")


def py0020():
    print("\n=== PY0020: Calculadora con menú ===")
    while True:
        print("\n--- Calculadora ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip().lower()

        if opcion in ["5", "salir"]:
            print("Saliendo de la calculadora...")
            break

        try:
            n1 = int(input("Introduce el primer número: "))
            n2 = int(input("Introduce el segundo número: "))

            if opcion in ["1", "sumar"]:
                resultado = n1 + n2
                operacion = "suma"
            elif opcion in ["2", "restar"]:
                resultado = n1 - n2
                operacion = "resta"
            elif opcion in ["3", "multiplicar"]:
                resultado = n1 * n2
                operacion = "multiplicación"
            elif opcion in ["4", "dividir"]:
                if n2 == 0:
                    raise ZeroDivisionError
                resultado = n1 / n2
                operacion = "división"
            else:
                print("Opción no válida. Intenta de nuevo.")
                continue

            print(f"✅ El resultado de la {operacion} es: {resultado:.2f}")

        except ValueError:
            print("Error: debes introducir números enteros válidos.")
        except ZeroDivisionError:
            print("Error: no se puede dividir entre cero.")
def py0003():
    import sys

    asistentes = []
    print("--- Parte A: Llenado de la lista ---")
    print("Introduce nombres de asistentes (escribe 'fin' para terminar):")

    while True:
        try:
            nombre = input("Nombre: ").strip()
        except EOFError:
            print("\nEntrada terminada inesperadamente.")
            break

        if nombre.lower() == "fin":
            break
        if nombre:
            asistentes.append(nombre)

    print(f"\nLista de asistentes inicial: {asistentes}")

    if not asistentes:
        print("La lista está vacía. Terminando el programa.")
        sys.exit()


    # Parte B

    print("\n--- Parte B: Conteo de un nombre ---")
    nombre_a_consultar = input("Introduce el nombre que deseas contar: ").strip()

    conteo = asistentes.count(nombre_a_consultar)

    print(f'El nombre "{nombre_a_consultar}" aparece {conteo} veces en la lista.')


    # Parte C

    print("\n--- Parte C: Buscar y Eliminar ---")

    if conteo > 0:
        # 1. Encontrar la primera posición con index()
        try:
            primera_posicion = asistentes.index(nombre_a_consultar)
            print(f'La primera ocurrencia de "{nombre_a_consultar}" está en la posición (índice) {primera_posicion}.')

            asistentes.remove(nombre_a_consultar)
            print(f'Se ha eliminado la primera ocurrencia de "{nombre_a_consultar}".')
            print(f"Lista después de la eliminación: {asistentes}")

        except ValueError:
            print(f'Error: "{nombre_a_consultar}" no se encontró para eliminar.')
    else:
        print(f'El nombre "{nombre_a_consultar}" no está en la lista para buscar o eliminar.')

    # ---

    # Parte D

    print("\n--- Parte D: Inserción VIP ---")

    nombre_vip = "Directora"  # O puedes pedirlo por input

    asistentes.insert(0, nombre_vip)

    print(f'Se ha insertado a "{nombre_vip}" en la posición 0.')

    # Lista Final

    print("\n--- Lista Final ---")
    print(f"Lista final de asistentes: {asistentes}")




# --- Punto de entrada ---
if __name__ == "__main__":
    py0003()

