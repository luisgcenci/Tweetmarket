import subprocess

#get products that should be filtered
products = subprocess.run("curl -X GET http://localhost:5000/allproducts", shell=True,capture_output=True)
products_str = products.stdout.decode('utf-8')

print(products_str)