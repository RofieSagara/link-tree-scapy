import random
import time
import requests as req
from selenium import webdriver
import re
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException


def get_random_scroll_script():
    rand = random.randint(-500, 1000)
    script = 'window.scrollBy(0,'+str(rand)+')'
    print('Get scroll random for the pixel ', rand, ' to emulate person with script ', script)
    return script


def random_sleep():
    rand = random.randint(3, 9)
    print('Do sleep for ', rand, ' seconds to emulate person')
    time.sleep(rand)


def main():
    regex = r"<a href=\"https://linktr.ee/.+?(?=<)"
    browser = webdriver.Firefox(executable_path='./geckodriver/geckodriver')
    browser.get('https://google.com')
    is_auto = False
    while True:
        if not is_auto:
            value = input('Press w if u want to crawling linktr.ee from this website.')
        else:
            value = 'w'

        if value == 'w':
            source = browser.page_source
            print('Start crawling and append to result.txt')
            f = open("result.txt", "a", encoding='utf-8')
            for match in re.finditer(regex, source, re.MULTILINE):
                try:
                    capture_link = BeautifulSoup(source[match.start():match.end()], 'html.parser').contents[0]['href']
                    f.write(capture_link+"\n")
                    print('Capture: ', capture_link)
                except KeyError:
                    print('KeyError check the website probably unique or website already change the view.')
                    is_auto = False
                except AttributeError:
                    print('AttributeError check the website probably unique or website already change the view.')
                    is_auto = False
            print('Try to make next result')
            try:
                # Emulate the person like scrolling before press next button
                button_next = browser.find_element_by_id('pnnext')
                random_sleep()
                random_step = random.randint(3, 10)
                print('Emulate random step for scrolling')
                for i in range(random_step):
                    random_sleep()
                    browser.execute_script(get_random_scroll_script())
                print('Scrolling to end of page')
                browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                print('Click next button')
                button_next.click()
                is_auto = True
            except NoSuchElementException:
                print('Seems like google detects our is robot. please fill the robot field')
                is_auto = False
            f.close()
        elif value == 'c':
            print('Close the program!')
            break
        else:
            print('Command not valid close the program!')
            break


if __name__ == '__main__':
    main()
