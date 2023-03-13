from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path):
        if path.endswith(".xml"):
            with open(path) as file:
                reader = file.read()

                return xmltodict.parse(reader)["dataset"]["record"]

        raise ValueError("Arquivo inválido")
