from PIL import Image
#Open image using Image module
im = Image.open("X.PNG")
#Show actual Image
im.show()
#Show rotated Image
im = im.transpose(45)
im.show()
