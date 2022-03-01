# coding:utf-8

import NetControl


# 天尊影视

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'https://www.tianzun.net/vod/show/id/1/page/' + str(page) + '.html'
        fileUrl = 'https://www.tianzun.net'
        soup = NetControl.sendRequest(baseUrl)
        for tag in (soup.find('ul', class_='panel-list clearfix').find_all('li')):
            title = tag.find('a',
                             class_='mo-situ-name mo-fsxs-14px mo-coxs-center mo-comd-left mo-wrap-arow').string.encode(
                'UTF-8')
            url = fileUrl + tag.find('a',
                                     class_='mo-situ-name mo-fsxs-14px mo-coxs-center mo-comd-left mo-wrap-arow').get(
                'href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('天尊影视  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    if None == soup.find('div', class_='mo-cols-lays mo-back-white mo-part-round'):
        return
    for tag in soup.find('div', class_='mo-cols-lays mo-back-white mo-part-round').find('ul',
                                                                                        class_='mo-cols-rows').find_all(
            'li'):
        title = tag.find('a',
                         class_='mo-situ-name mo-fsxs-14px mo-coxs-center mo-comd-left mo-wrap-arow').string.encode(
            'UTF-8')
        img = fileUrl + tag.find('a',
                                 class_='mo-situ-pics mo-situ-lazy mo-lazy-color mo-bord-round mo-cols-rows mo-lazy-highs mo-byxs-2by3').get(
            'data-original')
        url = fileUrl + tag.find('a', class_='mo-situ-name mo-fsxs-14px mo-coxs-center mo-comd-left mo-wrap-arow').get(
            'href')
        des = tag.find('span',
                       class_='mo-situ-desc mo-fsxs-12px mo-wrap-arow mo-text-muted mo-coxs-none mo-comd-block').string.encode(
            'UTF-8')
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + str(title) + "   " + img + "  " + url + '   ' + des)


# 执行程序
def run():
    page = 1
    maxPage = 576
    source = 6
    file_handle = open('dev/天尊影视.txt', mode='w')
    while page <= maxPage:
        url = 'https://www.tianzun.net/vod/show/id/1/page/' + str(page) + '.html'
        fileUrl = 'https://www.tianzun.net'
        soup = NetControl.sendRequest(url)
        checkFilms(page, fileUrl, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
