from PIL import Image

def encrypt_decrypt_image(image_path, mode):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Process each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            
            # Invert RGB values (simple encryption/decryption)
            new_r = 255 - r
            new_g = 255 - g
            new_b = 255 - b
            
            pixels[x, y] = (new_r, new_g, new_b)

    # Save the result
    output_path = "encrypted_image.png" if mode == "encrypt" else "decrypted.png"
    img.save(output_path)
    print(f"Image saved as {output_path}!")

# Ask the user for input
image_path = input("Enter image path (e.g., cat.png): ")
mode = input("Encrypt (E) or Decrypt (D)? ").lower()

if mode == "e":
    encrypt_decrypt_image(image_path, "encrypt")
elif mode == "d":
    encrypt_decrypt_image(image_path, "decrypt")
else:
    print("Invalid mode. Choose 'E' or 'D'.")