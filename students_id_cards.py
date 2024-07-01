from PIL import Image, ImageDraw, ImageFont

def create_id_card(student_name, student_id, school_name, output_path):
    # Dimensions of the ID card
    width, height = 400, 250
    background_color = (255, 255, 255)  # white
    text_color = (0, 0, 0)  # black

    # Create a blank image with white background
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 20)
        font_bold = ImageFont.truetype("arialbd.ttf", 24)
    except IOError:
        font = ImageFont.load_default()
        font_bold = ImageFont.load_default()

    # Define positions for the text
    school_name_position = (20, 20)
    student_name_position = (20, 80)
    student_id_position = (20, 140)
    logo_position = (300, 20)

    # Draw the text onto the image
    draw.text(school_name_position, school_name, font=font_bold, fill=text_color)
    draw.text(student_name_position, f"Name: {student_name}", font=font, fill=text_color)
    draw.text(student_id_position, f"ID: {student_id}", font=font, fill=text_color)

    # Add a placeholder for the logo (assuming a 100x100 area for the logo)
    draw.rectangle([logo_position, (logo_position[0]+100, logo_position[1]+100)], outline=text_color, width=2)
    draw.text((logo_position[0] + 10, logo_position[1] + 40), "Logo", font=font, fill=text_color)

    # Save the image
    image.save(output_path)
    print(f"ID card created for {student_name} and saved to {output_path}")

# Example usage:
students = [
    {"name": "John Doe", "id": "123456", "school": "XYZ High School"},
    {"name": "Jane Smith", "id": "789012", "school": "XYZ High School"}
]

for student in students:
    output_file = f"id_card_{student['id']}.png"
    create_id_card(student['name'], student['id'], student['school'], output_file)
