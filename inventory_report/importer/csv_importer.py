import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        if path.endswith(".csv"):
            with open(path, "r") as file:
                reader = csv.DictReader(file, delimiter=",", quotechar='"')

                return list(reader)

        raise ValueError("Arquivo inválido")
