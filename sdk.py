import base64
import requests

image_path = "test_image.jpg"
url = "http://localhost:5000/denoise"

with open(image_path, 'rb') as image_file:
    # Prepare the image file for the POST request
    files = {'image': image_file}
    
    try:
        response = requests.post(url, files=files)
        if response.status_code == 200:
            denoised_image_base64 = response.json().get('denoised_image')
            denoised_image_data = base64.b64decode(denoised_image_base64)

            with open("denoised_output.jpg", "wb") as f:
                f.write(denoised_image_data)
            print("Denoised image saved as 'denoised_output.jpg'.")
        else:
            print(f"Error: status code {response.status_code}")
            print("Response:", response.json())
    
    except Exception as e:
        print(f"Failed to send the image or decode the response: {e}")