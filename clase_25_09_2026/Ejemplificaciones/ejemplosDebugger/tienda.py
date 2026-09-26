class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

def calcular_total(carrito):
    suma = 0.0
    descuento_aplicado = False

    for producto in carrito:
        subtotal = producto.precio * producto.cantidad
        
        # Simulamos una condición de descuento
        if subtotal > 100:
            descuento_aplicado = True
            
        # Acumulamos el precio
        suma += subtotal
        

    # Aplicamos un 10% de descuento si aplica
    if descuento_aplicado:
        suma *= 0.90
          
    #  bug SIMULADO: Reasignación errónea que reinicia el valor a 0.0
    # En un código real, esto suele ser una reasignación accidental 
    # de variable dentro de un bloque 'if' o función de formateo.
    if descuento_aplicado:
        suma = 0.0  # O un reseteo directo: suma = 0.0 

    return suma

def main():
    print("--- INICIANDO SISTEMA DE TIENDA ---")
    
    carrito = [
        Producto("Camisa", 25.0, 2),   # Subtotal: 50.0
        Producto("Pantalón", 60.0, 2), # Subtotal: 120.0
        Producto("Zapatos", 80.0, 1),  # Subtotal: 80.0
    ]
    
    total = calcular_total(carrito)
    
    print(f"\nEl total a cobrar es: ${total:.2f}")

if __name__ == "__main__":
    main()