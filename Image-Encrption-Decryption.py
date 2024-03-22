def encrypt_image(path, key):
    try:
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()

        image = bytearray(image)

        for index, values in enumerate(image):
            image[index] = values ^ key

        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        print('Encryption Done...')
    except Exception as e:
        print('Error caught:', e)

def decrypt_image(path, key):
    try:
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()

        image = bytearray(image)

        for index, values in enumerate(image):
            image[index] = values ^ key

        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        print('Decryption Done...')
    except Exception as e:
        print('Error caught:', e)

def main():
    while True:
        print("\n1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            path = input(r'Enter path of Image: ')
            key = int(input('Enter Key for encryption of Image: '))
            encrypt_image(path, key)
        elif choice == '2':
            path = input(r'Enter path of Encrypted Image: ')
            key = int(input('Enter Key for decryption of Image: '))
            decrypt_image(path, key)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
