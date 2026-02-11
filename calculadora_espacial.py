import math
print ("=== CALCULADORA ESPACIAL ===\n")

#menu
print ("1. Velocidad orbital")
print ("2. Velocidad de escape")
print ("3. Gravedad superficial")
print ("4. Delta-v (Tsiolkovsky)")
print ("5. Tiempo de viaje")

opcion = input("\nElige opción (1-5): ")

G = 6.674e-11 # es la constante de gravitación universal

if opcion == "1":
    masa = float(input("Masa del planeta (kg):"))
    radio = float(input("Radio del planeta (m): "))

    v_orbital = math.sqrt(G * masa / radio)
    print(f"\nVelocidad orbital: {v_orbital/1000:.2f} km/s")

elif opcion == "2":
    masa = float(input("Masa del planeta (kg): "))
    radio = float(input("Radio del planeta (m): "))

    v_escape = math.sqrt(2 * G * masa / radio)
    print(f"\nVelocidad de escape: {v_escape/1000:.2f} km/s")

elif opcion == "3":
    masa = float(input("Masa del planeta (kg):"))
    radio = float(input("Radio del planeta (m):"))

    gravedad = (G * masa) / (radio **2)
    
elif opcion == "4":
    #Delta-v
    masa_i = float(input("Masa inicial cohete (kg):"))
    masa_f = float(input("Masa final cohete (kg):"))
    v_exhaust = float(input("Velocidad gases (m/s):"))

    delta_v = v_exhaust * math.log(masa_i /  masa_f)
    print(f"\nDelta-v disponible: {delta_v/1000:.2f} km/s")

elif opcion == "5":
    distancia = float(input("Distancia (km): "))
    velocidad = float(input("Velocidad (km/s): "))

    tiempo_segundos = (distancia * 1000) / velocidad
    tiempo_horas = tiempo_segundos / 3600
    tiempo_dias = tiempo_horas / 24
    print(f"\nTiempo de viaje:")
    print(f"{tiempo_segundos:.0f} segundos")
    print(f"{tiempo_horas:.1f} horas")
    print(f"{tiempo_dias:.2f} días")


else: print("Opcion no valida")
exit()