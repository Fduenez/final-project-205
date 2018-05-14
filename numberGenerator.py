from PIL import Image, ImageDraw, ImageFont

def generateNumbers(filename, startNum, endNum, pagesInSet, location, size, color):
    img = Image.open(filename) # read in the image to be modified
    lowercaseLocation = location.lower(); # convert user entered text to lowercase to mitigate case sensitivity

    # determine where the user wants numbers to appear
    if (lowercaseLocation == "top left"):
        coordinates = (50, 50)
    elif (lowercaseLocation == "top right"):
        coordinates = (img.width - 50, 50)
    elif (lowercaseLocation == "bottom left"):
        coordinates = (50, img.height - 50)
    elif (lowercaseLocation == "bottom right"):
        coordinates = (img.width - 50, img.height - 50)
    elif (lowercaseLocation == "middle"):
        coordinates = (img.width/2, img.height/2)
    else: # default location is the middle of the image
        coordinates = (img.width/2, img.height/2)

    # set the font size
    fnt = ImageFont.truetype('/Library/Fonts/Courier New.ttf', size)

    # set font color (red, green, blue, black, white)
    if (color == "red"):
        nColor = (255, 0, 0)
    elif (color == "green"):
        nColor = (0, 255, 0)
    elif (color == "blue"):
        nColor = (0, 0, 255)
    elif (color == "black"):
        nColor = (0, 0, 0)
    elif (color == "white"):
        nColor = (255, 255, 255)

    print(coordinates)

    # Generate the numbers. Also adding one at the end of each range since the second parameter is not included.
    for i in range(startNum, endNum+1):
        for j in range(1, pagesInSet+1):
            imgData = Image.open(filename) # read in the image to be modified
            numbered = ImageDraw.Draw(imgData)
            fileNum = str(i) # keep track of page numbers in file
            fileNumInSet = str(j)
            numbered.text(coordinates, str(i), font=fnt, fill=nColor)
            imgData.save("generated_numbers/" + fileNum + "_" + fileNumInSet + ".jpg")

generateNumbers("falcon_heavy.jpg", 1, 25, 2, "bottom right", 30, "red")
