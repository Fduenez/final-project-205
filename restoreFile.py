
from PIL import Image
import random
filename = 'winkled.jpg'
def restore(filename):
    # Create the Pillow image from the imported image
    img = Image.open(filename)
    # Sample 50 random pixel values from the image
    samples = []
    for pixel in range(50):
        sampleX = random.randint(0, img.width)
        sampleY = random.randint(0, img.height)
        samplePixel = img.getpixel((sampleX, sampleY))
        samples.append(samplePixel)
    # Average out the samples to create the new background color
    newBG = createBGPixel(samples)
    replaceBG(filename, newBG)


def createBGPixel(pixelList):
    newBGPixel =[0, 0, 0]
    listSize = len(pixelList)
    for pixel in range(listSize):
        newBGPixel[0] += pixelList[pixel][0]
        newBGPixel[1] += pixelList[pixel][1]
        newBGPixel[2] += pixelList[pixel][2]
    newBGPixel[0] = newBGPixel[0] / listSize
    newBGPixel[1] = newBGPixel[1] / listSize
    newBGPixel[2] = newBGPixel[2] / listSize
    return (int(newBGPixel[0]), int(newBGPixel[1]), int(newBGPixel[2]))

def replaceBG(filename, BGPixel):
    newImg = Image.open(filename)
    for x in range(newImg.width):
        for y in range(newImg.height):
            comparePixel = newImg.getpixel((x, y))
            if (comparePixel[0] > 100 and comparePixel[1] > 100 and comparePixel[2] > 100):
                newImg.putpixel((x, y), (255, 255, 255))
            else:
                newImg.putpixel((x, y), (0, 0, 0))

    newImg.save("good.jpg")

restore(filename)

# For future work: the above code runs and successfully replacest the background of a wrinkled image.
# The next step to make this applicable is to replace only background and avoid text overwriting.
# Maybe the text can be made darker through a function that reads in pixel values and sees if they are close
# to be being what a black pixel is composed of (255, 255, 255)
