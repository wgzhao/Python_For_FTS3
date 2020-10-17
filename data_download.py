# coding=utf-8

import requests
import os
from bs4 import BeautifulSoup
import gzip

base_url = r'https://faculty.chicagobooth.edu/ruey.tsay/teaching/fts3/'


def get_list():
    r = requests.get(base_url)
    soup = BeautifulSoup(r.content, 'html5lib')
    links = soup.findAll('a')
    file_names = [link.string for link in links if link['href'][:4] == 'file']
    for ii, filename in enumerate(file_names):
        start = 0
        for index, i in enumerate(filename):
            if i != ' ':
                start = index
                break
        file_names[ii] = filename[start:]
    file_links = [base_url + name for name in file_names]
    return file_links


def request_url(strurl):
    try:
        r = requests.get(strurl)
    except:
        try:
            r = requests.get(strurl)
        except:
            r = None
    return r


def download():
    try:
        downloadlist = get_list()
        down_cnt = len(downloadlist)
    except Exception as e:
        print('列表获取失败')
        return
    success = 0
    print('下载开始,共%d个文件' % len(downloadlist))
    for i, file_url in enumerate(downloadlist):
        file_name = 'data/' + file_url.split('/')[-1] + '.gz'
        print('进度{}%'.format(100 * i / down_cnt))
        print('{}下载开始'.format(file_url))
        if not os.path.exists(file_name):
            try:
                for try_count in range(3):
                    rt = request_url(file_url)
                    if rt is not None:
                        break
                with gzip.open(file_name, 'wb') as f:
                    f.write(rt.content)
                    f.close()
                    print('%s下载完成' % file_url)
                    success += 1
            except Exception as e:
                print('{}下载失败:{}'.format(file_url, e))
        else:
            success += 1
            print('{}已存在'.format(file_name))
        print('进度{}%'.format(100 * (i + 1) / len(downloadlist)))
    print('下载结束，共{}个文件，成功{}个，失败{}个'.format(down_cnt, success, down_cnt - success))


if __name__ == '__main__':
    download()
