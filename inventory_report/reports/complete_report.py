from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data):
        report = SimpleReport.generate(data)
        company_products = Counter(
            [company["nome_da_empresa"] for company in data]
        ).most_common()

        most_products = ""
        for company, count in company_products:
            most_products += f"- {company}: {count}\n"

        return (
            f"{report}\n"
            f"Produtos estocados por empresa:\n"
            f"{most_products}"
        )
