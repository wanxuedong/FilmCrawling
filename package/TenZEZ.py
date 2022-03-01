# coding:utf-8

import NetControl


# 1080影视

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'https://www.k1080.net/vodshow/1--------' + str(
            page) + '---.html'
        fileUrl = 'https://www.k1080.net'
        soup = NetControl.sendRequest(baseUrl)
        for tag in soup.find('ul', class_='stui-vodlist clearfix').find_all('li'):
            title = tag.find('h4', class_='title text-overflow').find('a').string.encode('UTF-8')
            url = fileUrl + tag.find('a', class_='stui-vodlist__thumb lazyload').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('1080影视  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    for tag in soup.find('ul', class_='stui-vodlist clearfix').find_all('li'):
        title = tag.find('h4', class_='title text-overflow').find('a').string.encode('UTF-8')
        img = tag.find('a', class_='stui-vodlist__thumb lazyload').get('data-original')
        if tag.find('a', class_='stui-vodlist__thumb lazyload').get('data-original').startswith('/upload'):
            img = fileUrl + tag.find('a', class_='stui-vodlist__thumb lazyload').get('data-original')
        url = fileUrl + tag.find('a', class_='stui-vodlist__thumb lazyload').get('href')
        des = ''
        if None != tag.find('p', class_='text text-overflow text-muted hidden-xs').string:
            des = tag.find('p', class_='text text-overflow text-muted hidden-xs').string.encode('UTF-8')
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + title + "   " + img + "  " + url + '   ' + des)


# 执行程序
def run():
    page = 1
    maxPage = 615
    source = 11
    file_handle = open('dev/1080影视.txt', mode='w')
    while page <= maxPage:
        url = 'https://www.k1080.net/vodshow/1--------' + str(
            page) + '---.html'
        fileUrl = 'https://www.k1080.net'
        soup = NetControl.sendRequest(url)
        checkFilms(page, fileUrl, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
