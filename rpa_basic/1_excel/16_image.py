from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

img = Image("img.png")
ws.add_image(img, "C3")

wb.save("simple_img.xlsx")

# ImportError : You must install Pillow to fetch image ...
# pip install Pillow
