from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if path.endswith(".json"):
            with open(path) as file:
                reader = file.read()

                return json.loads(reader)

        raise ValueError("Arquivo inválido")
