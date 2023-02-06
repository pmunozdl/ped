import csv


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
    