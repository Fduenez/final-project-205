from PIL import Image

def color_Multiply(img):
    color = "wrongcolor"
    while color != "increase red" and color != "increase green" and color != "increaseblue":
        color = input("Input the color you want to modify (red, green or blue): ")
    value = input("Input the value by which you want the color to be multiplied: ")       
    if color == "red":
        return red_Multiply(img, value)##
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
        temp = (255, p[1], p[2])#Fix the math
        new_list.append(temp)
    new_img.putdata(new_list)
    #new_img.save('new_pic.jpg')
    return new_img#Finish this

#mulitply green value
def green_Multiply(img, value):
    img = Image.open(img)
    img_size = img.size
    new_img = Image.new('RGB', (img_size[0], img_size[1]))
    new_list = []
    for p in img.getdata():
        temp = (p[0], p[1],255)
        new_list.append(temp)
    new_img.putdata(new_list)
    return new_img
    
#mulitply blue value
def blue_Multiply(img, value):
    img = Image.open(img)
    img_size = img.size
    new_img = Image.new('RGB', (img_size[0], img_size[1]))
    new_list = []
    for p in img.getdata():
        temp = (p[0], 255, p[2])
        new_list.append(temp)
    new_img.putdata(new_list)
    return new_img