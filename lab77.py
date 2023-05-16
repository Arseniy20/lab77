from PIL import Image, ImageFilter
def lab1():
    filename = "sobaken.jpg"
    with Image.open(filename) as img:
        img.load()

    img.show()
    width, height = img.size

    format = img.format

    mode = img.mode

    print("Ширина: ", width)
    print("Высота:  ", height)
    print("Формат: ", format)
    print("Цветовая модель:", mode)

lab1()

def lab2():
    filename = "sobaken.jpg"
    with Image.open(filename) as img:
        img.load()

    new_img = img.resize((img.width // 3, img.height // 3))

    new_img.save("resized_sobaken.jpg")

    converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    converted_img.save("image_flipsobaken_top.jpg")
    converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    converted_img.save("image_flip_sobaken.jpg")

lab2()

def lab3():
    filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

    for file in filenames:
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(ImageFilter.CONTOUR)
            new_img.save("new_" + file)


lab3()

def lab4():
    water = "watermark.png"
    with Image.open(water) as img_water:
        img_water.load()

    img_water = Image.open(water)
    img_water = img_water.resize((img_water.width // 2, img_water.height // 2))

    filename = "sobaken.jpg"
    with Image.open(filename) as img:
        img.load()

    img.paste(img_water, (450, 20), img_water)
    img.save("watermark_sobaken.jpg")
lab4()