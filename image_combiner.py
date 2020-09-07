from PIL import Image
import os


def createImg(width, height, extra):
    return Image.new(
        "RGBA",
        (width, height + extra),
        color=(255, 255, 255, 255),
    )


def pasteImgs(main_img, imgs, padding):
    paste_y = 0
    paste_x = 0
    for img in imgs:
        paste_x = int(main_img.width / 2 - img.width / 2)
        main_img.paste(img, (paste_x, paste_y))
        paste_y += img.height + padding


def combine_images(img_name_list):
    folder_path = "result-data"
    os.chdir(folder_path)

    # load images
    imgs = [Image.open(img_name) for img_name in img_name_list]

    # calculate max width
    max_width = max(img.width for img in imgs)
    total_height = sum(img.height for img in imgs)

    padding_y = 20
    final_img = createImg(max_width, total_height, padding_y * len(imgs))
    pasteImgs(final_img, imgs, padding_y)

    final_img.save("final-result.png", quality=95, subsampling=0)

    os.chdir("../")
