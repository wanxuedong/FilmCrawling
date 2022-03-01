# coding:utf-8

import NetControl


# 九九电影网

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'http://www.btzj.cc/vodshow/1--hits------' + str(
            page) + '---.html'
        fileUrl = 'http://www.btzj.cc'
        soup = NetControl.sendRequest(baseUrl)
        for tag in soup.find('ul', class_='list-unstyled').find_all('li'):
            title = tag.find('h6', class_='ff-text-hidden text-left ff-link').string.encode('UTF-8')
            url = fileUrl + tag.find('a').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('九九电影网  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    if None == soup.find('ul', class_='list-unstyled'):
        return
    for tag in soup.find('ul', class_='list-unstyled').find_all('li'):
        title = tag.find('h4', class_='ff-text-hidden text-left').find('a').string.encode('UTF-8')
        img = tag.find('img', class_='img-responsives ff-img').get('data-original')
        url = fileUrl + tag.find('a').get('href')
        des = ''
        if None != tag.find('h6', class_='ff-text-hidden text-left ff-link').string:
            des = tag.find('h6', class_='ff-text-hidden text-left ff-link').string.encode('UTF-8')
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + title + "   " + img + "  " + url + '   ' + des)


# 执行程序
def run():
    page = 1
    maxPage = 480
    source = 10
    file_handle = open('dev/九九电影网.txt', mode='w')
    while page <= maxPage:
        url = 'http://www.btzj.cc/vodshow/1--hits------' + str(
            page) + '---.html'
        fileUrl = 'http://www.btzj.cc'
        soup = NetControl.sendRequest(url)
        checkFilms(page, fileUrl, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
