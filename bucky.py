from PIL import Image
img=Image.open("712.jpg")
print(img.size)
print(img.format)
img.show()