# coding:utf-8

import NetControl


# 81影院

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'http://www.bayiyy.com/dianying/list_0_伦理_0_0_2_' + str(page) + '.html'
        fileUrl = 'http://www.bayiyy.com'
        soup = NetControl.sendRequest(baseUrl)
        for tag in (soup.find('ul', class_='v_picTxt v_pic_187_249 v_limit_width clearfix').find_all('li')):
            title = tag.find('a', class_='v_playBtn').get('title').encode('UTF-8')
            url = fileUrl + tag.find('a', class_='v_playBtn').get('href').encode('UTF-8')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('81影院  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(fileUrl, soup, file_handle, source):
    for tag in (soup.find('ul', class_='v_picTxt v_pic_187_249 v_limit_width clearfix').find_all('li')):
        title = tag.find('a', class_='v_playBtn').get('title').encode('UTF-8')
        img = tag.find('img').get('data-original').encode('UTF-8')
        score = '0'
        # 没有评分的需要添加判断
        if None != tag.find('span', class_='v_bottom_tips'):
            if None != tag.find('span', class_='v_bottom_tips').find('em').string:
                score = tag.find('span', class_='v_bottom_tips').find('em').string.encode('UTF-8')
        url = fileUrl + tag.find('a', class_='v_playBtn').get('href').encode('UTF-8')
        des = ''
        # 迭代span下的内容，表示描述
        for info in tag.find('div', class_='v_txt').find_all('span', class_='s_des'):
            des += info.string.encode('UTF-8')
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + source + '---0' + "\n")
        print (str(title) + "   " + img + "   " + score + "  " + url + "  " + des)


# 执行程序
def run():
    page = 1
    maxPage = 3
    source = 5
    file_handle = open('dev/81影院.txt', mode='w')
    while page <= maxPage:
        url = 'http://www.bayiyy.com/dianying/list_0_伦理_0_0_2_' + str(page) + '.html'
        fileUrl = 'http://www.bayiyy.com'
        soup = NetControl.sendRequest(url)
        checkFilms(fileUrl, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
