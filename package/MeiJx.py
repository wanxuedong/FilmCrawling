# coding:utf-8

import NetControl


# 美剧虾

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'http://www.meijuxia.net/video/type/2------hits-' + str(page) + '.html'
        fileUrl = 'http://www.meijuxia.net'
        soup = NetControl.sendRequest(baseUrl)
        for tag in (soup.find('ul', class_='panel-list clearfix').find_all('li')):
            title = tag.find('a', class_='video-title ellipsis-1').string.encode('UTF-8')
            url = fileUrl + tag.find('a', class_='video-item lazy-img').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('美剧虾  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle,source):
    for tag in (soup.find('ul', class_='panel-list clearfix').find_all('li')):
        title = tag.find('a', class_='video-title ellipsis-1').string.encode('UTF-8')
        img = fileUrl + tag.find('img',class_='ff-img').get('data-original')
        url = fileUrl + tag.find('a', class_='video-item lazy-img').get('href')
        des = tag.find('span', class_='video-actor ellipsis-1').string.encode('UTF-8')
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + str(title) + "   " + img + "  " + url + '   ' + des)


# 执行程序
def run():
    page = 1
    maxPage = 308
    source = 4
    file_handle = open('dev/美剧虾.txt', mode='w')
    while page <= maxPage:
        url = 'http://www.meijuxia.net/video/type/2------hits-' + str(page) + '.html'
        fileUrl = 'http://www.meijuxia.net'
        soup = NetControl.sendRequest(url)
        checkFilms(page, fileUrl, soup, file_handle,source)
        page += 1


if __name__ == '__main__':
    run()
