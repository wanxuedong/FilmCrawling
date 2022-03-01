# coding:utf-8

import NetControl


# 美剧网

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'https://91mjw.com/category/all_mj/page/' + str(page)
        fileUrl = 'https://91mjw.com/category'
        soup = NetControl.sendRequest(baseUrl)
        for tag in soup.find('ul', class_='m-movies clearfix').find_all('li'):
            title = tag.find('h2').string.encode('UTF-8')
            url = fileUrl + tag.find('a').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('美剧网  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    for tag in soup.find('div', class_='m-movies clearfix').find_all('article'):
        title = tag.find('h2').string.encode('UTF-8')
        img = tag.find('img').get('data-original')
        url = tag.find('a').get('href')
        des = ''
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + title + "   " + img + "  " + url + '   ' + des)


# 执行程序
def run():
    page = 2
    source = 16
    maxPage = 73
    file_handle = open('dev/美剧网.txt', mode='w')
    while page <= maxPage:
        url = 'https://91mjw.com/category/all_mj/page/' + str(page)
        fileUrl = 'https://91mjw.com/category'
        soup = NetControl.sendRequest(url)
        checkFilms(page, fileUrl, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
