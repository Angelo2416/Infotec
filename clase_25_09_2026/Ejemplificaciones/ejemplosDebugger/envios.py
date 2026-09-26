class Paquete:
    def __init__(self, peso_kg, zona_destino):
        self.peso_kg = peso_kg        # Peso en kilogramos
        self.zona_destino = zona_destino  # "Nacional", "Regional", "International"

def calcular_costo_envio(paquete):
    TARIFA_BASE = 30.0
    costo_por_kg = 0.0

    #Determinamos la tarifa por kilogramo según la zona
    if paquete.zona_destino == "Regional":
        costo_por_kg = 10.0
    elif paquete.zona_destino == "Nacional":
        costo_por_kg = 15.0
    elif paquete.zona_destino == "Internacional":
        costo_por_kg = 40.0

    #Calculamos el costo del peso del paquete
    costo_peso = paquete.peso_kg * costo_por_kg

    # Se intentó aplicar un recargo por sobrepeso (> 3 kg),
    # pero en lugar de SUMAR al costo total, se redefinió la variable 'total'
    # usando solo la 'TARIFA_BASE' o sobreescribiendo el cálculo del peso.
    total = TARIFA_BASE + costo_peso

    if paquete.peso_kg > 3:
        recargo = 25.0

        # En lugar de hacer 'total += recargo', el programador escribió:
        #total = TARIFA_BASE  # Se olvidó de incluir 'costo_peso' y el 'recargo'
        total += recargo

    return total

def main():
    print("--- SISTEMA DE LOGÍSTICA DE ENVÍOS ---")

    # Paquete de 5 kg enviado a nivel "Nacional"
    # - Tarifa Base: $30.0
    # - Costo por Peso: 5 kg * $15.0 = $75.0
    # - Recargo por sobrepeso (>3 kg): $25.0
    # TOTAL ESPERADO: $30 + $75 + $25 = $130.0 (o mínimo $105.0 sin recargo)
    paquete_cliente = Paquete(peso_kg=5, zona_destino="Nacional")

    costo_final = calcular_costo_envio(paquete_cliente)

    # El cliente o el sistema reciben una tarifa errónea de solo $30.00
    print(f"\nCosto total de envío calculado: ${costo_final:.2f}")

if __name__ == "__main__":
    main()