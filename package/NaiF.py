# coding:utf-8

import NetControl


# 奈菲影视

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'https://www.nfmovies.com/search.php?page=' + str(page) + '&searchtype=5&order=time'
        fileUrl = 'https://www.nfmovies.com'
        soup = NetControl.sendRequest(baseUrl)
        for tag in soup.find('ul', class_='myui-vodlist clearfix').find_all('li'):
            title = tag.find('a', class_='myui-vodlist__thumb lazyload').get('title')
            url = fileUrl + tag.find('a', class_='myui-vodlist__thumb lazyload').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('奈菲影视  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    if None == soup.find('ul', class_='myui-vodlist clearfix'):
        return
    for tag in soup.find('ul', class_='myui-vodlist clearfix').find_all('li'):
        title = tag.find('a', class_='myui-vodlist__thumb lazyload').get('title')
        img = fileUrl + tag.find('a', class_='myui-vodlist__thumb lazyload').get('data-original')
        url = fileUrl + tag.find('a', class_='myui-vodlist__thumb lazyload').get('href')
        des = ''
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + str(title) + "   " + img + "  " + url + '   ' + des)


# 执行程序
def run():
    page = 778
    maxPage = 1207
    source = 8
    file_handle = open('dev/奈菲影视.txt', mode='w')
    while page <= maxPage:
        url = 'https://www.nfmovies.com/search.php?page=' + str(page) + '&searchtype=5&order=time'
        fileUrl = 'https://www.nfmovies.com'
        soup = NetControl.sendRequest(url)
        checkFilms(page, fileUrl, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
