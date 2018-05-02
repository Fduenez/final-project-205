from PIL import Image

def resize(img):
	resize = "wronginput"
	while resize != "enlarge" and resize != "reduce":
		resize = input("Input if you want to reduce or enlarge the size of the image (reduce, enlarge): ")
	if resize == "reduce":
		value = input("Input the value by which you want your image to be reduced: ")
		reduce_size(img, value)
	if resize == "enlarge":
		value = input("Input the value by which you want your image to be enlarged: ")
		enlarge_size(img, value)

def enlarge_size(pic, value):
	img = Image.open(pic)
	img_size = img.size
	#new_tuple = ((img_size[0]*int(value)), (img_size[1]*int(value)))
	#img.thumbnail(new_tuple, Image.ANTIALIAS)
	
	"""new_img = Image.new('RGB', (img_size[0]*int(value), img_size[1]*int(value)))
	new_list = []
	for p in img.getdata():
		for i in range(int(value)):
			temp = (p[0], p[1], p[2])
			new_list.append(temp)
			"""
	baseheight = img_size[0]*int(value)
	hpercent = (baseheight / float(img.size[1]))
	wsize = int((float(img.size[0]) * float(hpercent)))
	img = img.resize((wsize, baseheight), Image.ANTIALIAS)
	img.save('resized_image.jpg')
	"""new_img.putdata(new_list)

	img.save('new_pic.jpg')"""

def reduce_size(pic, value):

    img = Image.open(pic)
    img_size = img.size
    new_tuple = ((img_size[0]/int(value)), (img_size[1]/int(value)))

    img.thumbnail(new_tuple, Image.ANTIALIAS)
    img.save('new_pic.jpg')

img = input("Input the name of the picture you want to modify: ")
resize(img)