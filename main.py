from PIL import Image
import numpy as np
from text_to_array import text_to_array

# Define the U-Bahn information
ubahn_info = [
    ('6', 'Sendlinger Tor', 3, True),
    ('3', 'Fürstenried West', 7, True),
    ('6', 'Sendlinger Tor', 13, False),
    (' ', 'Münchner Freiheit', 24, True),
    ('6', 'Garching Forschungszentrum', 33, False),
]

# Define color scheme
color_scheme = {
    'background': (0, 0, 0),  # Black background
    'line_number': {
        '6': (0, 23, 196),   # Blue for U-Bahn line 6
        '3': (228, 142, 51),  # Orange for U-Bahn line 3
        ' ': (100, 100, 100),  # Gray for unknown U-Bahn lines
    },
    'text': (255, 255, 255),    # White for text
    'on_time': (0, 255, 0),     # Green for on time
    'delayed': (255, 0, 0),     # Red for delayed
}


def create_led_matrix_image(ubahn_info, color_scheme):
    img_width, img_height = 32, 32
    led_matrix = np.zeros((img_height, img_width, 3), dtype=np.uint8)

    # Background color fill
    led_matrix[:, :] = color_scheme['background']

    char_height = 5  # Height of each character
    spacing = 1      # Spacing between rows
    row_height = char_height + spacing  # Total height for each row

    for i, (line, station, minutes, on_time) in enumerate(ubahn_info[:5]):
        y_start = i * row_height + 1

        # Get color for the line number
        line_color = color_scheme['line_number'].get(line, color_scheme['line_number'][' '])

        # Create pixel representations separately
        u_pixels = text_to_array('U', line_color, color_scheme['background'])
        line_pixels = text_to_array(line, line_color, color_scheme['background'])
        station_pixels = text_to_array(station[:3], color_scheme['text'], color_scheme['background'])
        minutes_pixels = text_to_array(str(minutes), color_scheme['on_time'] if on_time else color_scheme['delayed'], color_scheme['background'])

        # Create spaces
        space_pixels = np.zeros((char_height, 1, 3), dtype=np.uint8)

        # Concatenate the pixel arrays for U, space, line number, station
        ubahn_line_pixels = np.concatenate((u_pixels, space_pixels, line_pixels, np.zeros((char_height, 2, 3), dtype=np.uint8), station_pixels), axis=1)

        # Determine the start position for the minutes so that they are right-aligned with one space left empty
        minutes_x_start = img_width - len(minutes_pixels[0]) - 1

        # Place the U-Bahn line pixels
        led_matrix[y_start:y_start + char_height, 1:1+len(ubahn_line_pixels[0])] = ubahn_line_pixels

        # Place the minutes pixels
        led_matrix[y_start:y_start + char_height, minutes_x_start:minutes_x_start+len(minutes_pixels[0])] = minutes_pixels

    return Image.fromarray(led_matrix)

# Create the LED matrix image
led_matrix_image = create_led_matrix_image(ubahn_info, color_scheme)
led_matrix_image.show()
