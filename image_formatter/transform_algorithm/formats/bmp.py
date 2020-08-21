from PIL import Image

img = Image.open('C:/Python27/image.bmp')
new_img = img.resize( (256, 256) )
new_img.save( 'C:/Python27/image.png', 'png')