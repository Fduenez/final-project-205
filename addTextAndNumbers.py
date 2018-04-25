from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def addNumbers(filename, startNum, endNum, location_tuple, color_tuple): # location refers to x and y pixel coordiantes, color_tuple refers to RGB values
    for number in range(startNum, endNum+1):
        addNum = str(number)
        img = Image.open(filename)
        draw = ImageDraw.Draw(img)
        draw.text(location_tuple, addNum, color_tuple)
        img.save("generated_numbers/"+addNum+".jpg")


addNumbers("falcon_heavy.jpg", 1, 11, (200,100), (255, 255, 255))
# img = Image.open("falcon_heavy.jpg")
# draw = ImageDraw.Draw(img)
# draw.text((0, 0), "hello", (255,255,255))
# img.save(num+'.jpg')
