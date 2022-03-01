# coding:utf-8

import NetControl


# 怡萱动漫

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'http://www.yxdm.me/category.html?channel=17&totalresult=3180&pageno=' + str(page)
        fileUrl = 'http://www.yxdm.me'
        soup = NetControl.sendRequest(baseUrl)
        for tag in soup.find('div', class_='dhnew search-cnt adj').find_all('li'):
            title = tag.find('a').get('title')
            url = fileUrl + tag.find('a').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('怡萱动漫  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    for tag in soup.find('div', class_='dhnew search-cnt adj').find_all('li'):
        title = tag.find('a').get('title')
        img = fileUrl + tag.find('img').get('src')
        url = fileUrl + tag.find('a').get('href')
        des = ''
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + title + "   " + img + "  " + url + '   ' + des)


# 执行程序
def run():
    page = 1
    source = 17
    maxPage = 133
    file_handle = open('dev/怡萱动漫.txt', mode='w')
    while page <= maxPage:
        url = 'http://www.yxdm.me/category.html?channel=17&totalresult=3180&pageno=' + str(page)
        fileUrl = 'http://www.yxdm.me'
        soup = NetControl.sendRequest(url)
        checkFilms(page, fileUrl, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
