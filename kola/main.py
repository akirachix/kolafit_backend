from PIL import Image
from pytesseract import pytesseract

img = Image.open("media/rent_receipts/receipt_test.jpeg")
text = pytesseract. image_to_string(img)
print(text)