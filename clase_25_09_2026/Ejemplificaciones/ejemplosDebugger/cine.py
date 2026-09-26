class Entrada:
    def __init__(self, tipo_ticket, precio_base):
        self.tipo_ticket = tipo_ticket  # "adulto", "niño", "tercera_edad"
        self.precio_base = precio_base

def calcular_reserva(lista_entradas, codigo_descuento):
    subtotal = 0.0
    descuento_total = 0.0

    #Aplicar tarifas especiales según el tipo de boleto
    for entrada in lista_entradas:
        precio_final_ticket = entrada.precio_base

        if entrada.tipo_ticket == "niño":
            precio_final_ticket = entrada.precio_base * 0.50  # 50% desc
        elif entrada.tipo_ticket == "tercera_edad":
            precio_final_ticket = entrada.precio_base * 0.60  # 40% desc

        # En lugar de sumar el precio ya rebajado (precio_final_ticket),
        # se está acumulando siempre el precio base del boleto.
        subtotal += precio_final_ticket 
        #subtotal += precio_final_ticket


    if codigo_descuento == "CINEVIP":
        descuento_total = 20.0  # $20 de descuento fijo

    # Resta el descuento general directamente, pero descuida la condición
    # de que el total nunca sea negativo si el descuento supera el subtotal.
    total = subtotal - descuento_total

    return total

def main():
    print("--- SISTEMA DE RESERVAS DE CINE ---")

    # Boletos a comprar:
    # 1 Adulto ($100 base) + 1 Niño ($100 base -> debería ser $50) + 1 Tercera Edad ($100 base -> debería ser $60)
    # Total esperado REAL: $100 + $50 + $60 = $210 - $20 (CINEVIP) = $190.0
    entradas = [
        Entrada("adulto", 100.0),
        Entrada("niño", 100.0),
        Entrada("tercera_edad", 100.0)
    ]

    total_cobrado = calcular_reserva(entradas, "CINEVIP")

    print(f"\nTotal a pagar en caja: ${total_cobrado:.2f}")

if __name__ == "__main__":
    main()