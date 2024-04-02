from PIL import Image

# Open the image
image = Image.open("output_image3.png")

# Get the size of the image
width, height = 2000,2000

# Initialize counters for black and white pixels
black_pixels = 0
white_pixels = 0

# Iterate through each pixel in the image
for y in range(height):
    for x in range(width):
        # Get the pixel value at the current position

        pixel = image.getpixel((x, y))
        #print(pixel)


        # Check if the pixel is black or white
        if pixel == (0,0,0,255) or pixel == (0,0,204,255) or pixel ==(255,128,0,255) :  # Black
            black_pixels += 1
        elif pixel == (255,255,255,255):  # White
            white_pixels += 1



print((black_pixels/(white_pixels+black_pixels)*100))
# Print the counts
print("Black pixels:", black_pixels)
print("White pixels:", white_pixels)