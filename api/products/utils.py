import openpyxl
from .models import Product

def process_product_file(file):
    wb = openpyxl.load_workbook(file)
    sheet = wb.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        row = row[:5]
        nome, preco, unidade, disponibilizado, recebido = row

        existing_product = Product.objects.filter(name=nome).first()

        if not existing_product:
            Product.objects.create(
                name                = nome,
                price               = preco,
                unit                = unidade,
                likely_stock        = disponibilizado,
                garanteed_stock     = recebido
            ) 
        else: 
            if existing_product.price != preco:
                existing_product.price = preco  

            if existing_product.garanteed_stock != recebido:  
                existing_product.garanteed_stock = recebido;
            
            if existing_product.likely_stock != disponibilizado:  
                existing_product.likely_stock = disponibilizado;
            
            existing_product.save();
        
