from PIL import Image

def multipleUp(pil_img, n, type="generate"):
    if (n == 2):
        twoUp(pil_img, type)
    elif (n == 4):
        fourUp(pil_img, type)
    elif (n == 8):
        eightUp(pil_img, type)
    else:
        print("Multiple-up documents require a 2^n number.")

def proofUp(pil_img, n, type="proof"):
    if (n == 2):
        twoUp(pil_img, type)
    elif (n == 4):
        fourUp(pil_img, type)
    elif (n == 8):
        eightUp(pil_img, type)
    else:
        print("Multiple-up documents require a 2^n number.")


def twoUp(pil_img, type):
    # get source image
    source = pil_img
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

def fourUp(pil_img, type):
    # get source image
    source = pil_img
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

def eightUp(pil_img, type):
    fourUp(pil_img, type="generate")
    twoUp("mUp.jpg", type)
