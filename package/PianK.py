# coding:utf-8

import NetControl


# 片库网

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'https://www.pianku.tv/mv/------' + str(page) + '.html'
        fileUrl = 'https://www.pianku.tv'
        soup = NetControl.sendRequest(baseUrl)
        for tag in soup.find('ul', class_='content-list').find_all('li'):
            title = tag.find('a').get('title')
            url = fileUrl + tag.find('a').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('片库网  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    for tag in soup.find('ul', class_='content-list').find_all('li'):
        title = tag.find('a').get('title')
        img = tag.find('div', class_='li-img cover').find('img').get('data-funlazy')
        url = fileUrl + tag.find('a').get('href')
        des = ''
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + title + "   " + img + "  " + url + '   ' + des)


# 执行程序
def run():
    page = 1
    source = 20
    maxPage = 360
    file_handle = open('dev/片库网.txt', mode='w')
    while page <= maxPage:
        url = 'https://www.pianku.tv/mv/------' + str(page) + '.html'
        fileUrl = 'https://www.pianku.tv'
        soup = NetControl.sendRequest(url)
        checkFilms(page, fileUrl, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
