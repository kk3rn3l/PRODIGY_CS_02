from PIL import Image
import os

def encrypt_image(image_path, operation_key, output_directory):
    img = Image.open(image_path)
    width, height = img.size

    for x in range(width):
        for y in range(height):
            current_pixel = img.getpixel((x, y))
            encrypted_pixel = tuple([pixel ^ operation_key for pixel in current_pixel])
            img.putpixel((x, y), encrypted_pixel)

    encrypted_filename = generate_filename(image_path, "_encrypted")
    encrypted_path = os.path.join(output_directory, encrypted_filename)
    img.save(encrypted_path)
    print(f"Image encrypted and saved as {encrypted_path}")

def decrypt_image(encrypted_image_path, operation_key, output_directory):
    encrypted_img = Image.open(encrypted_image_path)
    width, height = encrypted_img.size

    for x in range(width):
        for y in range(height):
            encrypted_pixel = encrypted_img.getpixel((x, y))
            decrypted_pixel = tuple([pixel ^ operation_key for pixel in encrypted_pixel])
            encrypted_img.putpixel((x, y), decrypted_pixel)

    decrypted_filename = generate_filename(encrypted_image_path, "_decrypted")
    decrypted_path = os.path.join(output_directory, decrypted_filename)
    encrypted_img.save(decrypted_path)
    print(f"Image decrypted and saved as {decrypted_path}")

def generate_filename(original_filename, suffix):
    root, ext = os.path.splitext(original_filename)
    return f"{root}{suffix}{ext}"

def main():
    operation = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()

    if operation not in ['E', 'D']:
        print("Invalid input. Please enter 'E' for encrypt or 'D' for decrypt.")
        return

    input_image_path = input("Enter the path of the image: ")

    if not os.path.isfile(input_image_path):
        print("Error: Image file not found.")
        return

    output_directory = os.path.dirname(os.path.abspath(__file__))

    try:
        operation_key = int(input("Enter the operation key (an integer): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if operation == 'E':
        encrypt_image(input_image_path, operation_key, output_directory)
    else:
        decrypt_image(input_image_path, operation_key, output_directory)

if __name__ == "__main__":
    main()
