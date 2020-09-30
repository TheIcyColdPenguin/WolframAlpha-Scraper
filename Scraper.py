# imports
from os import chdir, mkdir
from shutil import rmtree

import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from image_combiner import combine_images


def get_equation():
    '''
    Helper function to get input equation from command line
    Useful for debugging.
    '''

    raw_eq = input("Enter any question: ").strip()
    return raw_eq


def get_page_answers(user_input):
    '''
    gets the answer images and text data for the given equation
    '''

    URL = "https://www.wolframalpha.com"

    # set up the web browser
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("--diable-gpu")
    options.add_argument("--ignore-certificate-errors")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(
        executable_path="./assets/chromedriver.exe", options=options)
    driver.get(URL)

    # search for input box
    input_box = driver.find_element_by_class_name("_2oXzi")
    input_box.send_keys(user_input + Keys.ENTER)

    from time import sleep

    # wait for results to load
    sleep(10)

    # find all images
    results = driver.find_elements_by_class_name("_3vyrn")
    images = [i.get_attribute("src") for i in results]
    text_data = [i.get_attribute("alt") for i in results]

    driver.quit()

    return images, text_data


def save_data(img_src_list, image_text_list):
    '''
    takes a list of image urls,
    and a list of all the text found along with the images
    and saves them to disk
    '''

    # load all the images and store them in a list
    image_data = [requests.get(image_source).content
                  for image_source in img_src_list]

    data_dir_name = "./result-data"

    # remove the directory if it exists
    # and then make an empty directory
    try:
        rmtree(data_dir_name)
    except FileNotFoundError:
        pass
    finally:
        mkdir(data_dir_name)
        chdir(data_dir_name)

    # create a list of numbered image names
    image_names = [
        f"result-image-{str(i).zfill(3)}.gif" for i in range(len(img_src_list))
    ]

    # write the image binary data to each corresponding image file
    for i, name in enumerate(image_names):
        with open(name, "wb") as image_file:
            image_file.write(image_data[i])

    # print(f"Images have been saved at {data_dir_name}")

    # write all the text to one file
    with open("./result-text-data.txt", "wb") as file:
        text_data = "\r\n".join(image_text_list).encode("utf8")
        file.write(text_data)

    # print(f"Text data has been saved at {data_dir_name}")

    chdir("../")
    return image_names


def main():
    eq = get_equation()
    answer_images, answer_text = get_page_answers(eq)
    img_names = save_data(answer_images, answer_text)
    combine_images(img_names)


def getimgsize():
    '''
    Returns size of result image
    '''
    img = Image.open("./result-data/final-result.png")
    size = img.size
    img.close()
    return size


if __name__ == "__main__":
    main()
