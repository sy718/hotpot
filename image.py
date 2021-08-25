from PIL import Image, ImageTk


# 打开图片并调整大小，给tkinter使用
def get_image(filename, width, height):
    im = Image.open(filename).resize((width, height))
    return ImageTk.PhotoImage(im)


# 裁剪图片
def cut_image(filename, left, upper, right, lower):
    img = Image.open(filename)
    cropped = img.crop((left, upper, right, lower))  # (left, upper, right, lower)
    return ImageTk.PhotoImage(cropped)
