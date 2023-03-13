from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.json_importer import JsonImporter


def test_decorar_relatorio():
    products = JsonImporter.import_data(
        "./inventory_report/data/inventory.json"
    )
    colored_report = ColoredReport(SimpleReport())
    oldest_fab = ("Data de fabricação mais antiga:", "2020-09-06")
    closest_exp = ("Data de validade mais próxima:", "2023-09-17")
    appearence = ("Empresa com mais produtos:", "Target Corporation")

    assert colored_report.generate(products) == (
        f"\x1b[32m{oldest_fab[0]}\x1b[0m \x1b[36m{oldest_fab[1]}\x1b[0m\n"
        f"\x1b[32m{closest_exp[0]}\x1b[0m \x1b[36m{closest_exp[1]}\x1b[0m\n"
        f"\x1b[32m{appearence[0]}\x1b[0m \x1b[31m{appearence[1]}\x1b[0m"
    )
