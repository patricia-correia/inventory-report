import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(url, type):
        complete_list = Inventory.read_file_csv(url)
        if type == 'simples':
            return SimpleReport.generate(complete_list)
        return CompleteReport.generate(complete_list)

    def read_file_csv(url):
        with open(url, "r") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(reader)
