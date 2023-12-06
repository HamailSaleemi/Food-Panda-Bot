# Food Panda Boot

This a bot for food panda to upload products on resturent portal

## Working
1. It read product from products.xlsx file.
2. Search item using barcode.
3. Enter required information like (sku, qty, price & category).

### How to use
1. Update the **products.xlsx** file with your product according to the format.
2. update your **credentials** in config.ini (email & password).

If you have panda install it's good otherwise use command below to install dependencies.
```bash
pip install -r requirement.txt
```

**Once everything is done run command**
```bash
pytest test_create_product.py --gui --verbose --html=report.html --full-trace
```
> **--gui** = to open browser on frontend and see all the process
>
> **--html=report.html** = to get the report of the test case in report.html file
> 
>**--full-trace** to get extra information in logs while the program is running
