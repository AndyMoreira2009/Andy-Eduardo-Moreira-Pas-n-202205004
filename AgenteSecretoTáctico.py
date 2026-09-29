print("Bienvenido al juego")
print("Tu misión es acabar con la corrupción de todo el mundo")
print("Elige tu agente")
def elegir_personaje():
    print("\n--- SELECCIÓN DE PERSONAJE ---")
    print("1. Agente Mike (Alta fuerza, baja velocidad)")
    print("2. Agente Y2k (Alto Sigilo, baja defensa)")
    print("3. Agente Lara Croft (Menor daño, ataques a distancia)")
    print("4. Agente Wos (Alta velocidad, baja salud)")
    
    eleccion = input("Elige el número de tu personaje (1-4): ")
    
    personajes = {
        "1": "Agente Mike",
        "2": "Agente Y2k",
        "3": "Agente Lara Croft",
        "4": "Agente Wos"
    }
    if eleccion in personajes:
        print(f"\n¡Has elegido al {personajes[eleccion]}! Preparando la partida...\n")
        # Aquí puedes llamar a la función que inicia la lógica principal de tu juego
    else:
        print("\nOpción no válida. Volviendo al menú principal.\n")

def menu_principal():
    while True:
        print("=== MENÚ PRINCIPAL ===")
        print("1. Iniciar juego")
        print("2. Salir")
        
        opcion = input("Elige una opción (1-2): ")
        
        if opcion == "1":
            elegir_personaje()
        elif opcion == "2":
            print("\n¡Gracias por jugar! Hasta pronto.")
            break
        else:
            print("\nOpción incorrecta. Por favor, ingresa 1 o 2.\n")

import random
import time

def juego_agente_secreto():
    print("=== AGENTE SECRETO TÁCTICO ===")
    print("Objetivo: Completar los 5 Mundos (10 niveles por mundo)\n")

    # Estructura global
    mundos = [
        "Mundo 1: Europa (Italia)",
        "Mundo 2: África",
        "Mundo 3: Rusia",
        "Mundo 4: Corea del Norte",
        "Mundo 5: EE.UU."
    ]

    # 1. Selección de Agente
    agentes = ["Agente Sombra", "Agente Táctico", "Agente Espectro"]
    print("Selección de Agente:")
    for i, agente in enumerate(agentes, 1):
        print(f"{i}. {agente}")
    
    agente_elegido = agentes[0] # Selección por defecto
    print(f"-> Agente seleccionado: {agente_elegido}\n")

    # Bucle principal de mundos (1 a 5)
    for index_mundo, mundo in enumerate(mundos, 1):
        print(f"\n==========================================")
        print(f"INICIANDO {mundo.upper()}")
        print(f"==========================================")

        nivel = 1
        while nivel <= 10:
            print(f"\n--- [ {mundo} | Nivel {nivel} ] ---")

            # Flujo especial para Nivel 10
            if nivel == 10:
                print("¡INICIO NIVEL 10!")
                
                # Generación Procedural de Mapa (Top-Down)
                print("Generando mapa procedural (Top-Down)...")
                
                # Simulación de mapas y minijefe opcional/desafío
                print("- Mapa 1: Estructuras y Objetos Variables (Mejoras de arma)")
                print("- Mapa 2: Mejoras y Enemigos")
                print("- Mapa 3: Desafío Especial con Enemigos")
                
                print("-> Enfrentando Minijefe...")
                if random.random() < 0.2:  # 20% probabilidad de derrota
                    print("❌ DERROTA en el Nivel 10. Reiniciando Nivel 10...")
                    continue  # Reinicia el nivel 10

                print("-> Enfrentando Subjefe del Mundo...")
                if random.random() < 0.2:
                    print("❌ DERROTA contra el Subjefe. Reiniciando Nivel 10...")
                    continue

                print("-> Enfrentando JEFE FINAL DEL MUNDO (Jefe Temático)...")
                if random.random() < 0.25:
                    print("❌ DERROTA contra el Jefe Final. Reiniciando Nivel 10...")
                    continue

                # Victoria en Nivel 10
                print(f"🏆 ¡VICTORIA! {mundo} COMPLETADO.")
                nivel += 1 # Avanza para salir del bucle de niveles
            
            # Flujo para Niveles 1 a 9
            else:
                # Cruzar 3 mapas procedurales
                print("Generando mapa procedural (3 Mapas)...")
                
                # Mapa 1
                print(" [Mapa 1]: Objetos Variables y Mejoras de Arma")
                
                # Mapa 2
                print(" [Mapa 2]: Enemigos y Mejoras")
                
                # Mapa 3
                print(" [Mapa 3]: Desafío Especial")
                if nivel >= 3:
                    print("   ⚠️ Enfrentando Minijefe del Mapa 3...")

                # Evaluación del combate en niveles 1-9
                éxito = random.random() > 0.15 # 85% probabilidad de éxito
                
                if not éxito:
                    print(f"❌ DERROTA en el Nivel {nivel}. Reintentando nivel...")
                    continue # Reintenta el nivel actual
                
                print(f"✅ NIVEL {nivel} COMPLETADO (Victoria).")
                nivel += 1  # Avanza al siguiente nivel (1 a 9)

            time.sleep(0.5)

    print("\n==========================================")
    print("🎉 ¡MUNDO 5 COMPLETADO! 🎉")
    print("🏆 ¡MISIÓN CUMPLIDA! HAS COMPLETADO EL JUEGO 🏆")
    print("==========================================")

# Ejecutar juego
if __name__ == "__main__":
    juego_agente_secreto()