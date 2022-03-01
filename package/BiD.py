# coding:utf-8

import NetControl


# 哔滴影视

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'https://bde4.com/s/all/' + str(page)
        fileUrl = 'https://bde4.com'
        soup = NetControl.sendRequest(baseUrl)
        for tag in (soup.find('div', class_='ui eight doubling cards').find_all('div')):
            if None == tag.find('span', class_='header').string:
                return
            title = tag.find('span', class_='header').string.encode('UTF-8')
            url = fileUrl + tag.find('a', class_='image').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('哔滴影视  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    for tag in soup.find('div', class_='ui eight doubling cards').find_all('div', class_='card'):
        if None == tag.find('span', class_='header').string:
            return
        title = tag.find('span', class_='header').string.encode('UTF-8')
        img = tag.find('img').get('src')
        url = fileUrl + tag.find('a', class_='image').get('href')
        des = ''
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + str(title) + "   " + img + "  " + url)


# 执行程序
def run():
    page = 15
    maxPage = 751
    source = '12'
    file_handle = open('dev/哔滴影视.txt', mode='a+')
    while page <= maxPage:
        url = 'https://bde4.com/s/all/' + str(page)
        fileUrl = 'https://bde4.com'
        soup = NetControl.sendRequest(url)
        checkFilms(page, fileUrl, soup, file_handle,source)
        page += 1


if __name__ == '__main__':
    run()
