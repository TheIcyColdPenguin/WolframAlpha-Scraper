from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_equation():
    raw_eq = input('Enter any question: ').strip()
    # clean_eq = quote(raw_eq)
    return raw_eq


def get_page_answers(user_input):
    URL = 'https://www.wolframalpha.com'

    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument('--diable-gpu')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    # search for input box
    input_box = driver.find_element_by_class_name('_2oXzi')
    input_box.send_keys(user_input+Keys.ENTER)

    from time import sleep
    sleep(10)  # wait for results to load

    # find all images
    results = driver.find_elements_by_class_name('_3vyrn')
    images = [i.get_attribute('src') for i in results]
    text_data = [i.get_attribute('alt') for i in results]

    driver.quit()
    return images, text_data


def save_data(image_source_list, image_text_list):
    import requests
    from os import mkdir, chdir
    from shutil import rmtree

    image_data = [requests.get(image_source).content
                  for image_source in image_source_list]

    data_dir_name = 'result-data'
    try:
        rmtree(data_dir_name)
    except FileNotFoundError:
        pass
    finally:
        mkdir(data_dir_name)
        chdir(data_dir_name)

    for i in range(len(image_source_list)):
        with open(f'result-image-{str(i).zfill(3)}.gif', 'wb') as image_file:
            image_file.write(image_data[i])

    print(f'Images have been saved at ./{data_dir_name}')

    with open('Result-text-data.txt', 'wb') as file:
        file.write('\r\n'.join(image_text_list).encode('utf8'))

    print(f'Text data has been saved at ./{data_dir_name}')


def main():
    eq = get_equation()
    answer_images, answer_text = get_page_answers(eq)
    save_data(answer_images, answer_text)


if __name__ == '__main__':
    main()
