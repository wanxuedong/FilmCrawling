# coding:utf-8

import NetControl


# 想看剧视频

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'https://www.xiangkanju.cc/list/1/p/' + str(page) + '.html'
        fileUrl = 'https://www.xiangkanju.cc'
        soup = NetControl.sendRequest(baseUrl)
        for tag in soup.find('div', class_='col-xs-12').find_all('div',
                                                                 class_='col-xs-1-5 col-sm-4 col-xs-6 movie-item'):
            title = tag.find('a').get('title')
            url = fileUrl + tag.find('a').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('想看剧视频  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    for tag in soup.find_all('div', class_='col-xs-1-5 col-sm-4 col-xs-6 movie-item'):
        title = tag.find('a').get('title')
        img = tag.find('img', class_='ZsCzLoading').get('src')
        url = fileUrl + tag.find('a').get('href')
        des = ''
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + str(title) + "   " + img + "  " + url + '   ' + des)


# 执行程序
def run():
    page = 1
    maxPage = 488
    source = 7
    file_handle = open('dev/想看剧视频.txt', mode='w')
    while page <= maxPage:
        url = 'https://www.xiangkanju.cc/list/1/p/' + str(page) + '.shtml'
        fileUrl = 'https://www.xiangkanju.cc'
        soup = NetControl.sendRequest(url)
        checkFilms(page, fileUrl, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
