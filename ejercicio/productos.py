class Productos:

    def __init__ (self, id_producto,nombre, precio):
        self._id_producto = id_producto
        self._nombre = nombre
        self._precio = precio
    @property
    def id_producto(self):
        return self._id_producto
    @id_producto.setter
    def nombre(self, id_producto):
        self._id_producto = id_producto
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, precio):
        self._precio = precio
    
