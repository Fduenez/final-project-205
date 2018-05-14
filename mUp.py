from PIL import Image

def multipleUp(filename, n, type="generate"):
    if (n == 2):
        twoUp(filename, type)
    elif (n == 4):
        fourUp(filename, type)
    elif (n == 8):
        eightUp(filename, type)
    else:
        print("Multiple-up documents require a 2^n number.")

def proofUp(filename, n, type="proof"):
    if (n == 2):
        twoUp(filename, type)
    elif (n == 4):
        fourUp(filename, type)
    elif (n == 8):
        eightUp(filename, type)
    else:
        print("Multiple-up documents require a 2^n number.")


def twoUp(filename, type):
    # get source image
    source = Image.open(filename)
    # set target width and target height
    targetWidth = source.width
    targetHeight = source.height * 2
    # create the template for the new image
    target = Image.new('RGB', (targetWidth, targetHeight))
    # duplicate the source image into the new image
    for x in range(source.width):
        for y in range(source.height):
            sourcePixel = source.getpixel((x, y))
            # put pixel on top half of page
            target.putpixel((x, y), sourcePixel)
            #put pixel on bottom half of page
            target.putpixel((x, y+source.height), sourcePixel)
    if (type == "generate"):
        target.save("mUp.jpg")
    elif (type == "proof"):
        target.show()

def fourUp(filename, type):
    # get source image
    source = Image.open(filename)
    # set target width and target height
    targetWidth = source.width * 2
    targetHeight = source.height * 2
    # create the template for the new image
    target = Image.new('RGB', (targetWidth, targetHeight))
    # duplicate the source image into the new image
    for x in range(source.width):
        for y in range(source.height):
            sourcePixel = source.getpixel((x, y))
            # put pixel in 1st quadrant
            target.putpixel((x, y), sourcePixel)
            # put pixel in 2nd quadrant
            target.putpixel((x, y+source.height), sourcePixel)
            # put pixel in 3rd quadrant
            target.putpixel((x+source.width, y), sourcePixel)
            # put pixel in 4th quadrant
            target.putpixel((x+source.width, y+source.height), sourcePixel)
    if (type == "generate"):
        target.save("mUp.jpg")
    elif (type == "proof"):
        target.show()

def eightUp(filename, type):
    fourUp(filename, type="generate")
    twoUp("mUp.jpg", type)
