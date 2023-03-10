from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(data):
        oldest_date = min([
            product["data_de_fabricacao"] for product in data
        ])
        nearest_expiry_list = []

        for product in data:
            date_expiration = datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d"
            ).date()

            if date_expiration > datetime.now().date():
                nearest_expiry_list.append(product["data_de_validade"])
        closest_date = min(nearest_expiry_list)

        company_more_item = Counter(
            [company["nome_da_empresa"] for company in data]
        ).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company_more_item}"
        )
