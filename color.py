from PIL import Image

def color_Multiply(img):
    color = "wrongcolor"
    while color != "red" and color != "green" and color != "blue":
        color = input("Input the color you want to modify (red, green or blue): ")
    value = input("Input the value by which you want the color to be multiplied: ")       
    if color == "red":
        red_Multiply(img, value)
    if color == "green":
        green_Multiply(img, value)
    if color == "blue":
        blue_Multiply(img, value)

#mulitply red value
def red_Multiply(img, value):
    img = Image.open(img)
    img_size = img.size
    new_img = Image.new('RGB', (img_size[0], img_size[1]))
    new_list = []
    for p in img.getdata():
        temp = ((p[0]*int(value))%255, p[1], p[2])
        new_list.append(temp)
    new_img.putdata(new_list)
    new_img.save('new_pic.jpg')

#mulitply green value
def green_Multiply(img, value):
    img = Image.open(img)
    img_size = img.size
    new_img = Image.new('RGB', (img_size[0], img_size[1]))
    new_list = []
    for p in img.getdata():
        temp = (p[0], (p[1]*int(value))%255, p[2])
        new_list.append(temp)
    new_img.putdata(new_list)
    new_img.save('new_pic.jpg')

#mulitply blue value
def blue_Multiply(img, value):
    img = Image.open(img)
    img_size = img.size
    new_img = Image.new('RGB', (img_size[0], img_size[1]))
    new_list = []
    for p in img.getdata():
        temp = (p[0], p[1], (p[2]*int(value))%255)
        new_list.append(temp)
    new_img.putdata(new_list)
    new_img.save('new_pic.jpg')

img = input("Input the name of the picture you want to modify: ")
color_Multiply(img)