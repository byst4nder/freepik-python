# -*- coding: utf-8 -*-  

from requests_html import HTMLSession
import pymysql
import hashlib
import re
import base64
from PIL import Image
from io import BytesIO
from tomorrow3 import threads

def htmldown(url):
    html = HTMLSession().get(url).html
    return html

def img_to_base64(url):
    html = HTMLSession().get(url).content
    im = Image.open(BytesIO(html))
    im = str(base64.b64encode(BytesIO(html).read()),encoding='utf8')
    im = 'data:image/jpeg;base64,'+ im
    return im

def liebiao():
    pagenumber = 0
    liebiao_list = []
    while(pagenumber<=100):
        url = 'https://www.freepik.com/search?dates=any&format=search&page='+str(pagenumber)+'&sort=recent&type=vector%2Cpsd'
        liebiao_list.append(url)
        pagenumber += 1
    return liebiao_list

@threads(20)
def post_mysql(page_url,md5_mm,down_url,img_url):
    print(page_url+'\n'+md5_mm+'\n'+down_url+'\n'+img_url)
    # img_url = img_to_base64(img_url)

    db = pymysql.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '',
        db = 'freepik',
        charset = 'utf8'
    )
    cursor = db.cursor()
    sql = """INSERT INTO `freepik` (`ID`,`page_url`,`down_url`,`img_url`,`md5`,`zt`) VALUES (NULL, '%s','%s','%s','%s','0')""" % (pymysql.escape_string(page_url),pymysql.escape_string(down_url),pymysql.escape_string(img_url),pymysql.escape_string(md5_mm))
    cursor.execute(sql)
    db.commit()

def get_url(liebiao_url):
    html = htmldown(liebiao_url)
    page_urls = html.find('a.showcase__link')
    for i in page_urls:
        page_url = str(i.attrs['href'])

        m2 = hashlib.md5()
        m2.update(str(page_url).encode("utf8"))
        md5_mm = str(m2.hexdigest())
        md5_mm = str(md5_mm)

        db = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            passwd = '',
            db = 'freepik',
            charset = 'utf8'
        )
        cursor = db.cursor()
        sql = 'SELECT * FROM freepik WHERE md5="'+(str(md5_mm))+'"'
        cursor.execute(sql)
        res = cursor.fetchall()
        db.commit()
        db.close()
        if len(res):
            print('存在')
        else:
            print('不存在，采集入库。')

            down_id = re.findall(r'_([\d]+)\.htm',page_url)[0]
            down_url = 'https://www.freepik.com/download-file/'+str(down_id)

            img_url = i.find('img')[0].attrs['data-src']
            size = str(re.findall(r'size=([\d]+)\&',img_url)[0])
            img_url = re.sub(size,'140',img_url)
            
            post_mysql(page_url,md5_mm,down_url,img_url)

        print('\n')

for i in liebiao():
    get_url(i)