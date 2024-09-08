
from PIL import Image, ImageDraw
from functools import cache

@cache
def draw_penguin_logo(width,height):

# Create a blank image with a transparent background, at a higher resolution
    image_size = (1000, 1000)  # Increased resolution for clarity
    background_color = (255, 255, 255, 0)  # RGBA with alpha for transparency
    image = Image.new('RGBA', image_size, background_color)
    draw = ImageDraw.Draw(image)

# Calculate the center position
    center_x, center_y = image_size[0] // 2, image_size[1] // 2

# Draw the body (simple black circle)
    body_radius = 500# Scaled to match the larger canvas
    body_color = (0, 0, 0)
    draw.ellipse(
        [(center_x - body_radius, center_y - body_radius), 
        (center_x + body_radius, center_y + body_radius)], 
        fill=body_color
    )

# Draw the belly (smaller white circle inside the body)
    belly_radius = 312# Scaled to match the larger canvas
    belly_color = (255, 255, 255)
    draw.ellipse(
        [(center_x - belly_radius, center_y - belly_radius), 
        (center_x + belly_radius, center_y + belly_radius)], 
        fill=belly_color
    )

# Draw the beak (small orange triangle)
    beak_color = (255, 165, 0)
    beak_size = 125  # Scaled to match the larger canvas
    draw.polygon(
        [(center_x - beak_size, center_y), 
        (center_x + beak_size, center_y), 
        (center_x, center_y + beak_size)], 
        fill=beak_color
    )

# Draw the eyes (two small black circles)
    eye_radius = 62  # Scaled to match the larger canvas
    eye1_position = (center_x - 187, center_y - 125)
    eye2_position = (center_x + 187, center_y - 125)
    eye_color = (0, 0, 0)
    draw.ellipse(
        [(eye1_position[0] - eye_radius, eye1_position[1] - eye_radius), 
        (eye1_position[0] + eye_radius, eye1_position[1] + eye_radius)], 
        fill=eye_color
    )
    draw.ellipse(
        [(eye2_position[0] - eye_radius, eye2_position[1] - eye_radius), 
        (eye2_position[0] + eye_radius, eye2_position[1] + eye_radius)], 
        fill=eye_color
    )

# Save the image
    #image.save('simple_penguin_logo_high_res.png')

# Optionally resize for final use (e.g., downscale to 200x200 for smaller icons)
    final_image = image.resize((width, height))
    final_image.save('simple_penguin_logo_high_res_resized.png')

    return final_image

if __name__ == "__main__":
    draw_penguin_logo(2000, 2000)
