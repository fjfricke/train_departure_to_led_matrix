import numpy as np


def custom_upper(text):
    # Replace ß with its uppercase version ẞ
    text = text.replace('ß', 'ẞ')
    # Convert the rest of the text to uppercase
    return text.upper()


def text_to_array(text, color, default_color):
    # Define the pixel art representation for each letter in uppercase, including German characters
    pixel_art = {
        'A': np.array([[0, 1, 0], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]]),
        'B': np.array([[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 1], [1, 1, 0]]),
        'C': np.array([[0, 1, 1], [1, 0, 0], [1, 0, 0], [1, 0, 0], [0, 1, 1]]),
        'D': np.array([[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 0]]),
        'E': np.array([[1, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 0], [1, 1, 1]]),
        'F': np.array([[1, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 0], [1, 0, 0]]),
        'G': np.array([[0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 0, 1], [0, 1, 1]]),
        'H': np.array([[1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]]),
        'I': np.array([[1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]),
        'J': np.array([[0, 0, 1], [0, 0, 1], [0, 0, 1], [1, 0, 1], [0, 1, 0]]),
        'K': np.array([[1, 0, 1], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 0, 1]]),
        'L': np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 1]]),
        'M': np.array([[1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]]),
        'N': np.array([[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]]),
        'O': np.array([[0, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0]]),
        'P': np.array([[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 0], [1, 0, 0]]),
        'Q': np.array([[0, 1, 0], [1, 0, 1], [1, 0, 1], [1, 1, 0], [0, 1, 1]]),
        'R': np.array([[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 1], [1, 0, 1]]),
        'S': np.array([[0, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0]]),
        'T': np.array([[1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]),
        'U': np.array([[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 1]]),
        'V': np.array([[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0]]),
        'W': np.array([[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1]]),
        'X': np.array([[1, 0, 1], [1, 0, 1], [0, 1, 0], [1, 0, 1], [1, 0, 1]]),
        'Y': np.array([[1, 0, 1], [1, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0]]),
        'Z': np.array([[1, 1, 1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]),
        'Ä': np.array([[1, 0, 1], [0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 0, 1]]),
        'Ö': np.array([[1, 0, 1], [0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]]),
        'Ü': np.array([[1, 0, 1], [0, 0, 0], [1, 0, 1], [1, 0, 1], [1, 1, 1]]),
        'ẞ': np.array([[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1], [1, 0, 0]]),
        '0': np.array([[0, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0]]),
        '1': np.array([[0, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]),
        '2': np.array([[1, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]),
        '3': np.array([[1, 1, 0], [0, 0, 1], [0, 1, 1], [0, 0, 1], [1, 1, 0]]),
        '4': np.array([[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]]),
        '5': np.array([[1, 1, 1], [1, 0, 0], [1, 1, 0], [0, 0, 1], [1, 1, 0]]),
        '6': np.array([[0, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 0]]),
        '7': np.array([[1, 1, 1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 0, 0]]),
        '8': np.array([[1, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 1], [1, 1, 1]]),
        '9': np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]]),
        ' ': np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]),
    }

    # Convert the text to uppercase
    text = custom_upper(text)

    # Determine the size of the final array
    char_width, char_height = 3, 5
    spacing = 1
    img_width = (char_width + spacing) * len(text) - spacing
    img_height = char_height

    # Initialize the array with a default color (e.g., white or transparent)
    pixel_array = np.full((img_height, img_width, 3), default_color, dtype=np.uint8)

    # Fill in the pixel array
    for i, char in enumerate(text):
        if char in pixel_art:
            for y in range(char_height):
                for x in range(char_width):
                    if pixel_art[char][y, x] == 1:
                        pixel_x = i * (char_width + spacing) + x
                        pixel_array[y, pixel_x] = color  # Set the color for the pixel

    return pixel_array

# # Example usage
# text = "abcdefghijklmnopqrstuvwxyzäöüß0123456789"
# color = (255, 0, 0)  # Red color
# pixel_data = text_to_array(text, color)
# print(pixel_data)

# from PIL import Image, ImageDraw

# def draw_final_image(pixel_data):
#     # Convert the NumPy array to a Pillow Image
#     img = Image.fromarray(pixel_data, 'RGB')
#     return img

# # Drawing the final image using the pixel data
# final_image = draw_final_image(pixel_data)
# final_image.show()