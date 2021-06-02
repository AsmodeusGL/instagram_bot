from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth import username, password
import time
import random


def hashtag_search(log, pas, hashtag):

    len_urls = input('Enter the number of repetitions')
    while not len_urls.isdigit():
        len_urls = input('Enter the number of repetitions')

    urls = []
    browser = webdriver.Chrome()

    try:
        browser.get('https://www.instagram.com/')
        time.sleep(4)
        username_input = browser.find_element_by_name(name="username")
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(random.randint(2, 4))

        password_input = browser.find_element_by_name(name="password")
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(4)

        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(4)
            hrefs = browser.find_elements_by_tag_name('a')
            [urls.append(item.get_attribute('href')) for item in hrefs if '/p/' in item.get_attribute('href')]

            while len(urls) < int(len_urls):
                browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                time.sleep(random.randint(2, 4))
                hrefs = browser.find_elements_by_tag_name('a')
                [urls.append(item.get_attribute('href')) for item in hrefs if '/p/' in item.get_attribute('href')]

            for url in urls:
                with open('posts_links.txt', 'r+', encoding='utf-8') as links:
                    read_file_links = links.read().splitlines()

                    if url not in read_file_links:
                        try:
                            links.write(url + '\n')
                            browser.get(url)
                            time.sleep(4)
                            browser.find_element_by_css_selector('#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg').click()

                            with open('users.txt', 'r+', encoding='utf-8') as users:
                                read_file_users = users.read().splitlines()

                                user = browser.find_element_by_css_selector('#react-root > section > main > div > div.ltEKP > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > span > a').text
                                if user not in read_file_users:
                                    time.sleep(random.randint(2, 4))
                                    browser.find_element_by_css_selector('#react-root > section > main > div > div.ltEKP > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button').click()
                                    users.write(user + '\n')

                            time.sleep(random.randrange(15, 20))

                        except Exception as ex:
                            print(ex)

            browser.close()
            browser.quit()

        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


def unsub_users():

    len_users = input('Enter the number of repetitions')
    while not len_users.isdigit():
        len_users = input('Enter the number of repetitions')



hashtag_search(username, password, 'minsk')
