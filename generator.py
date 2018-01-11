from PIL import Image,ImageDraw
import random
import matplotlib.pyplot as plt

def draw_rectangle(draw, coordinates, color, width=1):
	for i in range(width):
		rect_start = (coordinates[0][0] - i, coordinates[0][1] - i)
		rect_end = (coordinates[1][0] + i, coordinates[1][1] + i)
		draw.rectangle((rect_start, rect_end), outline = color)
		
def dataset_generator(imgs_num):
	rotated_images = []
	angles = []
	for _ in range(imgs_num):
		rectag_num = random.randint(1,10)
		random_angle = random.uniform(-10,10)
		img = Image.new('RGB', (128, 128), "white") #создание изображения 128*128
		lineDrawer = ImageDraw.Draw(img)
		drawing = ImageDraw.Draw(img)
		for _ in range(rectag_num):
			width = random.randint(1,5)
			x = random.uniform(0.1,1)*128
			y = random.uniform(0.1,1)*128
			#lineDrawer.rectangle(((x,y),(random.uniform(0,x-0.1*128),random.uniform(0,y-0.1*128))), outline = "black")
			drawing = ImageDraw.Draw(img)
			draw_rectangle(drawing,((x,y),(random.uniform(0.1*128,x-0.1*128),random.uniform(0.1*128,y-0.1*128))), color = "black",width=width)
		
		im2 = img.convert('RGBA')
		rotated = im2.rotate(random_angle, resample=Image.BICUBIC)
		fff = Image.new('RGBA', rotated.size)
		out = Image.composite(rotated, fff, rotated)
		out.convert('RGB')#img.mode
		rotated_images.append(out)
		angles.append(random_angle)
	return  rotated_images,angles

def showImagesHorizontally(list_of_files):
    fig = plt.figure(figsize=(20,10))
    
    number_of_files = len(list_of_files)
    for i in range(number_of_files):
        a=fig.add_subplot(1,number_of_files,i+1)
        image = list_of_files[i]
        image = image.rotate(-predicted[i])
        plt.imshow(image,cmap='Greys_r')
        plt.title(("True= {}   Predicted= {}").format(y_test[i],predicted[i]))
        plt.axis('off')