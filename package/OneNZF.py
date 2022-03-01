# coding:utf-8

import NetControl


# 1905电影网

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'https://www.1905.com/vod/list/n_1/o1p' + str(page) + '.html'
        soup = NetControl.sendRequest(baseUrl)
        for tag in (soup.find('section', class_='mod row search-list').find_all('div')):
            title = tag.find('h3').string.encode('UTF-8')
            url = tag.find('a', class_='pic-pack-outer').get('target').encode('UTF-8')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('1905电影网  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, soup, file_handle, source):
    for tag in (soup.find('section', class_='mod row search-list').find_all('div')):
        if None == tag.find('h3').string:
            return
        title = tag.find('h3').string.encode('UTF-8')
        img = tag.find('img').get('src')
        url = tag.find('a', class_='pic-pack-outer').get('href').encode('UTF-8')
        des = ''
        if None != tag.find('p').string:
            des = tag.find('p').string.encode('UTF-8')
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + str(title) + "   " + img + "  " + url + "  " + des)


# 执行程序
def run():
    page = 1
    maxPage = 317
    source = 3
    file_handle = open('dev/1905电影网.txt', mode='w')
    while page <= maxPage:
        url = 'https://www.1905.com/vod/list/n_1/o1p' + str(page) + '.html'
        soup = NetControl.sendRequest(url)
        checkFilms(page, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
