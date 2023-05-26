from PIL import Image

img = Image.open('src\img\logo.jpg')
largura , altura = img.size
print(largura)
print(altura)