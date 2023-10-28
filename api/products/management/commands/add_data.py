import pandas as pd

from django.core.management.base import BaseCommand
from products.models import Product
from sqlalchemy import create_engine

class Command(BaseCommand):
    help = "A command to add data_product from an Excel file to the database"

    def handle(self, *args, **options):

        excel_file = 'ENCOMENDAS.xlsx'
        df = pd.read_excel(excel_file)

        db_url = 'postgresql://mmigu:mmigu@localhost:5432/db_comuna'
        engine  = create_engine(db_url)

        for index, row in df.iterrows():
            name = row['NAME']
            existing_product = Product.objects.filter(name=name).first()

            if existing_product is None:
                new_product = Product(name=name, price=row['PRICE'], unit=row['UNIT'])
                new_product.save()
                self.stdout.write(self.style.SUCCESS(f"Produto adicionado: {name}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Produto já existe: {name}"))

            self.stdout.write(self.style.SUCCESS("Importação concluída"))


        df.to_sql(Product._meta.db_table, if_exists='replace', con=engine, index=False)
        print(df)