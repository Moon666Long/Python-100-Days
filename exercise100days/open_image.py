# 人生苦短，我学Python
# 2021年10月14日




from PIL import Image
def show_image():
    image = Image.open('F:\\Documents\\GitHub\\Python-100-Days\\Day01-15\\res\\browers.jpg')
    image.format, image.size, image.mode
    ('JPEG', (1000, 2000), 'RGB')
    image.save('browers.png')
    ina=Image.open('browers.png')
    print(ina.format)
    #print(image)
    #image.show()
if __name__ == '__main__':
    show_image()


    print(Image._check_size())