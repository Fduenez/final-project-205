from PIL import Image

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Test of the code in this file using hardcoded arguments.
filename = 'bad2.jpg'
n_up = 2
multipleUp(filename, n_up)
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Description: This function creates a multiple-up image from a source image.
# Required arguments for the function are a string representing a filename and
# an integer value of 2, 4, or 8 that represents the amount of duplicate source
# images. The output is a new file. Exception is thrown for invalid arguments.
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def multipleUp(filename, n):
    if (n == 2):
        twoUp(filename)
    elif (n == 4):
        fourUp(filename)
    else:
        print("Multiple-up documents require a 2^n number.")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Description: This function is a helper to the multipleUp() function. If this
# function is called, it creates a 2-up image from using the source file argument
# from the multipleUp() function.
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def twoUp(filename):
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
    target.save("2up.jpg")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Description: This function is a helper to the multipleUp() function. If this
# function is called, it creates a 2-up image from using the source file argument
# from the multipleUp() function.
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def fourUp(filename):
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
        target.save("2up.jpg")
