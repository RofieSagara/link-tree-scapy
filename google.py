import time

import requests as req
from selenium import webdriver
import re
from bs4 import BeautifulSoup


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
            f = open("result.txt", "a")
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
            browser.find_element_by_id("pnnext").click()
            time.sleep(5)
            f.close()
            is_auto = True
        elif value == 'c':
            print('Close the program!')
            break
        else:
            print('Command not valid close the program!')
            break


if __name__ == '__main__':
    main()
