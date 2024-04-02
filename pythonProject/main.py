
from PIL import Image, ImageDraw

# Create a white image
image_size = (2000, 2000)
background_color = "white"
image = Image.new("RGBA", image_size, background_color)

# Load coordinates from text file
with open("trial3Coords.txt", "r") as file:
    coordinates = [tuple(map(float, line.strip().split())) for line in file]

raw_enlarged = [(x*10,y*10) for x,y in coordinates]



# Adjust coordinates to center (0,0) and flip y-axis
adjusted_coordinates = [(x + image_size[0] // 2, -y + image_size[1] // 2) for x, y in raw_enlarged]

# Define circle radius
circle_radius = 165

# Draw circles on the image
draw = ImageDraw.Draw(image)
circle_color = "black"
for coord in adjusted_coordinates:
    # Calculate circle bounding box

    x1 = coord[0] - circle_radius
    y1 = coord[1] - circle_radius
    x2 = coord[0] + circle_radius
    y2 = coord[1] + circle_radius
    bbox = (x1, y1, x2, y2)
    # Draw circle
    draw.ellipse(bbox, fill=circle_color)

    line_color = (0,0,204)
    for i in range(len(adjusted_coordinates) - 1):
        start_point = adjusted_coordinates[i]
        end_point = adjusted_coordinates[i + 1]
        draw.line([start_point, end_point], fill=line_color, width=6)
axis_color = (255,128,0)
#draw.line([(1000, 0),(1000, 2000)], fill =axis_color,width=6)
#draw.line([(0, 1000),(2000, 1000)], fill =axis_color,width=6)


# Save or display the image
image.save("output_image3.png")
image.show()