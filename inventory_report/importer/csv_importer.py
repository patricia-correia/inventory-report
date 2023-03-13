import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_path, type):
        report_list = Inventory.read_file_csv(file_path)
        if type == 'simples':
            return SimpleReport.generate(report_list)
        return CompleteReport.generate(report_list)

    def read_file_csv(file_path):
        with open(file_path, "r") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(reader)
