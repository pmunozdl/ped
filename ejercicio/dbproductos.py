from productos import Productos
from datoscsv import DBbyCSV
import csv

SCHEMA = {
    'ID': {
        'type': 'autoincrement',
    }, 
    'NOMBRE': {
        'type': 'string',
        'min_length': 3,
        'max_length': 50
    }, 
    'PRECIO': {
        'type': 'int'
    }, 
}

class DBProductos(DBbyCSV):

    def __init__(self):
        super().__init__(SCHEMA, 'productos')
    def insert(self, data):

        id_producto = self.get_last_id() + 1
        line = [id_producto] + data

        with open(self._filename, mode='a', encoding='utf-16') as csv_file:
            data_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            data_writer.writerow(line)

        return True


    def get_last_id(self):
        
        list_ids = []
        with open(self._filename, mode='r', encoding='utf-16') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            is_header = True
            for row in csv_reader:
                if is_header:
                    is_header = False
                    continue

                if row:
                    list_ids.append(row[0])

        if not list_ids:
            return 0
        
        # Ordenamos la lista de mayor a menor y retornamos el elemento de mayor tamaño
        list_ids.sort(reverse = True) 
        return int(list_ids[0])
        
    def save_product(self, Productos):
        data = [Productos.nombre, Productos.precio]
        return self.insert(data)
    def list_products(self, Productos):
        list_products = self.get_all()
        return self._create_object_products(list_products)
    
    def get_schema(self):
        return SCHEMA
    def search_contacts(self, filters):
        if 'NOMBRE' not in filters:
            raise ValueError('Debes envíar al menos un filtro')

        list_products = self.get_by_filters(filters)
        return self._create_object_contacts(list_products)


    def _create_object_products(self, list_products):

        if not list_products:
            return None

        object_products = []
        # Convertimos los datos a objectos de tipo contact
        for productos in list_products:
            c = Productos(productos['ID'], productos['NOMBRE'],productos['PRECIO'])
            object_products.append(c)

        return object_products

    def search_products(self, filters):
        if 'NOMBRE' not in filters:
            raise ValueError('Debes envíar al menos un filtro')

        list_products = self.get_by_filters(filters)
        return self._create_object_products(list_products)

    def update_product(self, id_product, data):
        if not id_product:
            raise ValueError('Debes enviar el id del contacto')
        if not data:
            raise ValueError('Debes enviar al menos un parámetro a actualizar')
        self.update(id_product, data)