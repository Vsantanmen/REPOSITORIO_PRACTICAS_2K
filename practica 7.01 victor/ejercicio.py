import sys

class Producto:
    def __init__(self, codigo, nombre, precio):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor >= 0:
            self._precio = valor
        else:
            self._precio = 0

    def calcular_total(self, unidades):
        return self._precio * unidades


class Pedido:
    def __init__(self):
        self._productos = []
        self._cantidades = []

    def añadir_producto(self, producto, cantidad):
        if cantidad > 0:
            self._productos.append(producto)
            self._cantidades.append(cantidad)

    def total_pedido(self):
        total = 0
        for i in range(len(self._productos)):
            producto = self._productos[i]
            cantidad = self._cantidades[i]
            total += producto.calcular_total(cantidad)
        return total

    def mostrar_productos(self):
        if not self._productos:
            print("El pedido no tiene productos.")
            return
        
        for i in range(len(self._productos)):
            producto = self._productos[i]
            cantidad = self._cantidades[i]
            print(f"Producto: {producto.nombre} | Código: {producto.codigo} | Precio Unitario: {producto.precio}€ | Cantidad: {cantidad}")


p1 = Producto("001", "Ratón Óptico", 15.50)
p2 = Producto("002", "Teclado Mecánico", 45.00)
p3 = Producto("003", "Monitor 24'", 120.00)

mi_pedido = Pedido()

mi_pedido.añadir_producto(p1, 2)
mi_pedido.añadir_producto(p2, 1)
mi_pedido.añadir_producto(p3, 1)

print("--- DETALLE DEL PEDIDO ---")
mi_pedido.mostrar_productos()

print("--------------------------")
total_final = mi_pedido.total_pedido()
print(f"Precio final del pedido: {total_final}€")
