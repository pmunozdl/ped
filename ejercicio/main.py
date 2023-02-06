import os
import time 
from validaciones import Validaciones
from productos import Productos
from dbproductos import DBProductos
#from prettytable import PrettyTable
validator = Validaciones()
db = DBProductos()

def print_options():
    print('Selecciona una opción:')
    print('[C]rear contacto')
    print('[L]istado de contactos')
    print('[M]odificar contacto')
    print('[E]liminar contacto')
    print('[B]uscar contacto')
    print('[S]ALIR')

def run():
    print_options()

    command = input()
    command = command.upper()
    #crear
    if command == 'C':
        crear_contacto()
    #leer
    elif command == 'L':
        list_products()
    #modificar
    elif command == 'M':
        update_product()
    #borrar
    elif command == 'E':
        pass
    #buscar
    elif command == 'B':
        search_product()
    elif command == 'S':
        os._exit(1)
    else:
        print('Comando inválido')
        time.sleep(1)
        run()

def crear_contacto():
    nombre = comprobar_contacto()
    precio = comprobar_precio()

def comprobar_precio():
    precio = input()
    try:
        validator.validatePrecio(precio)
        return precio
    except ValueError as err:
        print(err)
        comprobar_precio()

def comprobar_contacto():
    nombre = input()
    try:
        validator.validateName(nombre)
        return nombre
    except ValueError as err:
        print(err)
        comprobar_contacto()
def comprobar_datos_contacto(message, data_name):
    print(message)
    input_data = input()
    try:
        getattr(validator, f'validate{data_name.capitalize()}')(input_data)
        return input_data
    except ValueError as err:
        print(err)
        comprobar_datos_contacto(message, data_name)

def crear_contacto():
    nombre = comprobar_datos_contacto('name')
    precio = comprobar_datos_contacto('precio')
    producto = Productos(None, nombre, precio)
    if db.save_contact(producto):
        print('Contacto insertado con éxito')
    else:
        print('Error al guardar el contacto')
def list_products():
    list_products = db.list_products()

    if not list_products:
        return print('Todavía no hay contactos guardados')

    table = (db.get_schema().keys())
    for productos in list_products:
        table.add_row([
            productos.id_contact,
            productos.nombre,
            productos.precio
        ])

    print(table)
    print('Pulsa intro para salir')
    command = input()

def search_product():
        filters = {}
        print('Introduce un nombre (vacío para usar otro filtro):')
        nombre = input()
        if nombre:
            filters['NOMBRE'] = nombre
        precio = input()
        if precio:
            filters['PRECIO'] = precio

        try:
            list_products = db.search_(filters)
            if not list_products:
                return print('No hay ningún contacto con esos criterios de búsqueda')

            _print_table_products(list_products)
        except ValueError as err:
            print(err)
            time.sleep(1)
            search_product()


def _print_table_products(list_products):
    table = (db.get_schema().keys())
    for product in list_products:
        table.add_row([
            product.id_contact,
            product.name,
            product.precio,
        ])

    print(table)
    print('Pulsa cualquier letra para continuar')
    command = input()
def check_contact_data(message, data_name, force = True):
    input_data = input
    if not force and not input_data:
        return
    try:
        getattr(validator, f'validate{data_name.capitalize()}')(input_data)
        return input_data
    except ValueError as err:
        print(err)
        check_contact_data(message, data_name)
if __name__ == "__main__":
    run()