import pandas as pd



# Xpaths
CATEGORY_BUTTON = "//div[contains(text(),'Categories')]"
APPLY_BUTTON = "//button[normalize-space()='Apply']"
SAVE_BUTTON = "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1k1j1tn']"
FORMAT_CATEGORY = "//span[normalize-space()='{0}']"
FORMAT_CLASS = "//span[normalize-space()='{0}']"
# Product path
product_path = '/home/hamail/Desktop/Projects/Food Panda boot/product2.xlsx'

# Read Products
df = pd.read_excel(product_path)
df_dict = df.to_dict(orient='list')

products = []
for i in range (0, len(df_dict['Product title'])):
    products.append(
        {
    'title': df_dict['Product title'][i],
    'price': df_dict['Price'][i],
    'barcodes': df_dict['Barcodes(Mandatory)'][i],
    'sku': df_dict['SKU'][i],
    'max_sale_qty': df_dict['Maximum Sales Quantity'][i],
    'active': df_dict['Active'][i],
    'category':df_dict['Category '][i],
    'class': df_dict['class'][i]
    }
    )


print(products)
