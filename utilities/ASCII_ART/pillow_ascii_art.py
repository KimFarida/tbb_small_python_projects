from PIL import Image
WIDTH = 50
HEIGHT = 25

def convertImagetoASCIIart(image_file):

    image = Image.open(image_file)

    gray_image = image.convert('L')

    smaller_image = gray_image.resize((WIDTH, HEIGHT))

    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

    ascii_str = ''
    for pixel in smaller_image.getdata():
        ascii_str+= ASCII_CHARS[pixel // 25]
    
    ascii_str_len = len(ascii_str)

    image_to_ascii_file = image_file.split('.', 1)[0] + '.txt'

    with open(image_to_ascii_file, 'a') as f:
        for i in range(0, ascii_str_len, WIDTH):
            f.write(ascii_str[i:i+WIDTH])
            f.write('\n')



file = "pikachu.png"
convertImagetoASCIIart(file)
