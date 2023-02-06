import csv
import re
from tempfile import NamedTemporaryFile
import shutil


class DBbyCSV:

    def __init__(self, schema, filename):
        self._filename = f'./{filename}.csv'
        try:
            # Verificamos si ya existe el archivo
            f = open(self._filename)
            f.close()
        except IOError:
            # Si el archivo no existe creamos la cabecera
            with open(self._filename, mode='w', encoding='utf-16') as csv_file:
                data_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
                data_writer.writerow(schema.keys())


    def get_all(self):

        list_data = []
        list_header = []
        with open(self._filename, mode='r', encoding='utf-16') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            is_header = True
            for row in csv_reader:
                if is_header:
                    list_header = row
                    is_header = False
                    continue

                if row:
                    file = {}
                    for key, value in enumerate(row):
                        file[list_header[key]] = value

                    list_data.append(file)

        return list_data
    def get_by_filters(self, filters):

        list_data = []
        list_header = []
        with open(self._filename, mode='r', encoding='utf-16') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            is_header = True
            for row in csv_reader:
                if is_header:
                    list_header = row
                    is_header = False
                    continue

                if row:
                    file = {}

                    for key, value in enumerate(row):
                        file[list_header[key]] = value
                    
                    for key_filter, value_filter in filters.items():
                        matches = re.search(rf"{value_filter}", file[key_filter], re.IGNORECASE)
                        if matches:
                            list_data.append(file)
                            break

        return list_data
    
    def get_by_id(self, id_product):
        list_header = []
        with open(self._filename, mode = 'r', encoding='utf=16') as csv_file:
            csv_reader = csv_reader(csv_file, delimiter = ';')
            is_header = True
            for row in csv_reader:
                if is_header:
                    list_header = row
                    is_header = False
                    continue
                if row:
                    file = {}
                    for key, value in enumerate(row):
                        file[list_header[key]] == value
                    if file['ID'] == id_product:
                        return file
        return {}
    
    def update(self, id_product, data):
        data_csv = self.get_by_id(id_product)

        if not data_csv:
            raise Exception('No se ha encontrado el objeto con el id enviado')
        
        for key, value in data.items():
            data_csv[key] = value
        tempfile = NamedTemporaryFile(mode='w', delete=False, encoding='utf-16')

        list_header = []
        with open(self._filename, mode='r', encoding='utf-16') as csv_file, tempfile:
            csv_reader = csv_reader(csv_file, delimeter = ';')
            data_writer = csv_writer(tempfile, delimeter =';', quotechar='"', quoting = csv.QUOTE_MINIMAL, lineterminator = '\n')

            is_header = True
            for row in csv_reader:
                if is_header:
                    list_header= row
                    is_header = False
                    data_writer.writerow(row)
                    continue
                if row:
                    file = {}
                    for key, value in enumerate(row):
                        file[list_header[key]] = value
                    if file['ID'] != data_csv['ID']:
                        data_writer.writerow(row)
                        continue
                    for key, value in data_csv.items():
                        file[key] = value
                    data_writer.writerow(file.values())
        shutil.move(tempfile.name, self._filename)´
        return True 