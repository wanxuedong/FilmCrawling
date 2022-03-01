# coding:utf-8

import NetControl


# 9亿看看

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'http://www.9ekk.com/vodshow/dianying/page/' + str(page) + '.html'
        fileUrl = 'http://www.9ekk.com'
        soup = NetControl.sendRequest(baseUrl)
        for tag in soup.find('ul', class_='myui-vodlist clearfix').find_all('li'):
            title = tag.find('a', class_='myui-vodlist__thumb lazyload').get('title')
            url = fileUrl + tag.find('a', class_='myui-vodlist__thumb lazyload').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('9亿看看  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    for tag in soup.find('ul', class_='myui-vodlist clearfix').find_all('li'):
        title = tag.find('a', class_='myui-vodlist__thumb lazyload').get('title')
        img = tag.find('a', class_='myui-vodlist__thumb lazyload').get('data-original')
        if img.startswith('/upload/'):
            img = fileUrl + img
        url = fileUrl + tag.find('a', class_='myui-vodlist__thumb lazyload').get('href')
        des = tag.find('p', class_='text text-overflow text-muted hidden-xs').string.encode('UTF-8')
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + title + "   " + img + "  " + url + '   ' + des)


# 执行程序
def run():
    page = 1
    source = 14
    maxPage = 994
    file_handle = open('dev/9亿看看.txt', mode='w')
    while page <= maxPage:
        url = 'http://www.9ekk.com/vodshow/dianying/page/' + str(page) + '.html'
        fileUrl = 'http://www.9ekk.com'
        soup = NetControl.sendRequest(url)
        checkFilms(page, fileUrl, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
