import base64

def image_to_base64(file_path, output_file_path):
    try:
        with open(file_path, "rb") as file:
            encoded_image = base64.b64encode(file.read()).decode("utf-8")
        with open(output_file_path, "w") as output_file:
            output_file.write(encoded_image)
        print("Base64 Encoded Image saved to:", output_file_path)
    except Exception as e:
        print("Error:", str(e))

def base64_to_image(base64_data, output_file_path):
    try:
        decoded_image = base64.b64decode(base64_data)
        with open(output_file_path, "wb") as output_file:
            output_file.write(decoded_image)
        print("Decoded Image saved to:", output_file_path)
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    jpg_file_path = "Image.jpg"                
    base64_output_file = "encoded_image.txt"        # Output file to save the base64 encoding
    decoded_output_file = "decoded_image.jpg"       # Output file to save the decoded image

    # Convert JPG image to base64 encoding and save it to a file
    image_to_base64(jpg_file_path, base64_output_file)

    # Read the base64 data from the file and decode it back to image
    with open(base64_output_file, "r") as encoded_file:
        base64_data = encoded_file.read()
        base64_to_image(base64_data, decoded_output_file)
