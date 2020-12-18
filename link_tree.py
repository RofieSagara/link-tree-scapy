from bs4 import BeautifulSoup
import requests as req


class Content:
    def __init__(self, name, content):
        self._name = name
        self._content = content

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value


def main():
    file = open("result.txt", 'r')
    lines = file.readlines()
    for line in lines:
        print('Start crawling with link ', line)
        response = req.get(line)
        soup = BeautifulSoup(response.content, 'html.parser').find(id="__next")
        if len(soup.contents) != 3:
            print('Check the style probably unique or website already change the view')
            return -1

        try:
            data = soup.contents[2].contents[0].contents[0]
            result = [Content('link', line.replace('\n', ''))]
            for it in data.contents[2:]:
                if len(it.contents) != 0:
                    if len(it.contents[0].contents) != 0:
                        item = it.contents[0].contents[0]
                        href = item.get('href')
                        if href is not None:
                            result.append(Content(item.text, href))
            write_file = open('link_tree_result.csv', 'a')
            for item in result:
                write_file.write(item.content + ',')
            write_file.write('\n')
            write_file.close()
        except KeyError:
            print('KeyError check the website probably unique or website already change the view.')
        except AttributeError:
            print('AttributeError check the website probably unique or website already change the view.')
        print('Done')


if __name__ == '__main__':
    main()
