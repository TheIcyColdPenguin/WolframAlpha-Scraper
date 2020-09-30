# imports
from PIL import Image
import os


def create_img(width, height, extra):
    '''
    create and return an image object
    with specified width and height, plus a bit of padding
    '''
    return Image.new(
        "RGBA",
        (width, height + extra),
        color=(255, 255, 255, 255),
    )


def paste_imgs(main_img, imgs, padding):
    '''
    pastes all the images in the list of images onto
    the blank base image
    '''
    paste_y = 0
    paste_x = 0
    for img in imgs:
        paste_x = int(main_img.width / 2 - img.width / 2)
        main_img.paste(img, (paste_x, paste_y))
        paste_y += img.height + padding


def combine_images(img_name_list):
    '''
    takes a list of image names, and combines and saves them as a single image
    '''

    folder_path = "./result-data"
    os.chdir(folder_path)

    # load images
    imgs = [Image.open(img_name) for img_name in img_name_list]

    # calculate width and height of the combined image
    max_width = max(img.width for img in imgs)
    total_height = sum(img.height for img in imgs)

    padding_y = 20

    # create an image with the right dimensions
    final_img = create_img(max_width, total_height, padding_y * len(imgs))

    # paste all the images onto the base image
    paste_imgs(final_img, imgs, padding_y)

    # save the base image
    final_img.save("./final-result.png", quality=95, subsampling=0)

    for img in imgs:
        img.close()

    for filename in os.listdir():
        if filename.endswith(".gif") or filename.endswith(".txt"):
            os.remove(filename)

    os.chdir("../")
