# coding:utf-8
import sys

import NetControl

# ADC影院

reload(sys)
sys.setdefaultencoding('utf8')


# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'https://www.adcmove.com/list/dianying-' + str(page) + '.html'
        fileUrl = 'https://www.adcmove.com/'
        soup = NetControl.sendRequest(baseUrl)
        for tag in soup.find('ul', class_='fed-list-info fed-part-rows').find_all('li'):
            title = tag.find('a',
                             class_='fed-list-title fed-font-xiv fed-text-center fed-text-sm-left fed-visible '
                                    'fed-part-eone').string
            url = fileUrl + tag.find('a', class_='fed-list-pics fed-lazy fed-part-2by3').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('ADC影院  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(fileUrl, soup, file_handle,source):
    for tag in soup.find('ul', class_='fed-list-info fed-part-rows').find_all('li'):
        title = tag.find('a',
                         class_='fed-list-title fed-font-xiv fed-text-center fed-text-sm-left fed-visible fed-part-eone').string
        img = tag.find('a', class_='fed-list-pics fed-lazy fed-part-2by3').get('data-original')
        url = fileUrl + tag.find('a', class_='fed-list-pics fed-lazy fed-part-2by3').get('href')
        des = tag.find('span',
                       class_='fed-list-desc fed-font-xii fed-visible fed-part-eone fed-text-muted fed-hide-xs '
                              'fed-show-sm-block').string
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (title + '   ' + img + '   ' + url + '   ' + des)


# 执行程序
def run():
    page = 1
    maxPage = 1120
    source = 2
    file_handle = open('dev/ADC影院.txt', mode='w')
    while page <= maxPage:
        baseUrl = 'https://www.adcmove.com/list/dianying-' + str(page) + '.html'
        fileUrl = 'https://www.adcmove.com/'
        soup = NetControl.sendRequest(baseUrl)
        checkFilms(fileUrl, soup, file_handle,source)
        page += 1


if __name__ == '__main__':
    run()
