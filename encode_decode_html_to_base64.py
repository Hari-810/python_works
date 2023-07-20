# convert html file to base64 file and vice versa


import base64

def html_to_base64(file_path, output_file_path):
    try:
        with open(file_path, "rb") as file:
            encoded_file = base64.b64encode(file.read()).decode("utf-8")
        
        # Save base64 encoded data to a file
        with open(output_file_path, "w") as output_file:
            output_file.write(encoded_file)
        print("Base64 Encoded Data has been saved to:", output_file_path)
        
        # Decode base64 data back to HTML file
        with open(output_file_path, "r") as encoded_file:
            decoded_file = base64.b64decode(encoded_file.read())
        with open("decoded_html_file.html", "wb") as decoded_output_file:
            decoded_output_file.write(decoded_file)
        print("Base64 Decoded Data has been saved to: decoded_html_file.html")
        
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    html_file_path = "html_file_name.html"      
    output_file_path = "encoded_html_file.txt"  
    
    html_to_base64(html_file_path, output_file_path)
