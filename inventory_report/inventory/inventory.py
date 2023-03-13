import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        reports_list = Inventory.read_file_csv(path)

        if type == "simples":
            return SimpleReport.generate(reports_list)

        return CompleteReport.generate(reports_list)

    def read_file_csv(path):
        with open(path, "r") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(reader)

    def read_file_json(path):
        with open(path) as file:
            reader = file.read()
            return json.loads(reader)

    def read_file_xml(path):
        with open(path) as file:
            reader = file.read()
            return xmltodict.parse(reader)["dataset"]["record"]

    def verify_type_file(path):
        if path.endswith(".csv"):
            return Inventory.read_file_csv(path)

        if path.endswith(".json"):
            return Inventory.read_file_json(path)

        if path.endswith(".xml"):
            return Inventory.read_file_xml(path)
