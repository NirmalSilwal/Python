from PIL import Image
from PIL import ImageFilter

# img = Image.open('./pokedex/pikachu.jpg')

# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)
# print(img.width,img.height,img.size)
# print(dir(img))
# print(img.__sizeof__)

# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img = img.filter(ImageFilter.SHARPEN)
# print(type(filtered_img))
# filtered_img.save('sharpenPikachu.png','png')

# filtered_img.save('blurPikachu.png','png')
# filtered_img.save('smoothPikachu.png','png')

# filtered_img = img.convert('L')
# rotated = filtered_img.rotate(90)
# rotated.save('rotatedPikachu.png','png')
# rotated.show()

img = Image.open('./pokedex/squirtle.jpg')
# img.show()
#
# grey_img = img.convert('L')
# # grey_img.show()
#
# resized_img = grey_img.resize((200,200))
# # resized_img.show()
# resized_img.save('resizedSquirtle.jpg')

pixel_box = (100,100,400,400)
cropped = img.crop(pixel_box)
cropped.show()
cropped.save('croppedSquirtle.jpg')