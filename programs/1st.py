from PIL import Image
im_file = "data/hi.png"
im = Image.open(im_file)
print(im.size) #to see the size of my image
#to show the image
#im.show()
# i can also rotate images by calling function rotate(degree)
im1 = im.rotate(45)
# to save the image to this folder from the data folder
im1.save("programs/JS.png")
