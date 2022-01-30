# 人生苦短，我学Python
# 2021年10月14日




from PIL import Image
    image = Image.open('./res/browers.jpg')
    image.format, image.size, image.mode
    ('JPEG', (500, 750), 'RGB')
    image.show()