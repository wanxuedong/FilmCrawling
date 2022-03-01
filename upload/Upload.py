#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path
import requests
import hashlib

# 待上传文件路径
FILE_UPLOAD = "/usr/local/etc/nginx/fastcgi_params.default"
# 上传接口地址
UPLOAD_URL = "http://localhost:8080/resumable_upload"
# 单个片段上传的字节数
SEGMENT_SIZE = 1048576


def upload(fp, file_pos, size, file_size):
    session_id = get_session_id()
    fp.seek(file_pos)
    payload = fp.read(size)
    content_range = "bytes {file_pos}-{pos_end}/{file_size}".format(file_pos=file_pos,
                                                                    pos_end=file_pos + size - 1, file_size=file_size)
    headers = {'Content-Disposition': 'attachment; filename="big.TXT"', 'Content-Type': 'application/octet-stream',
               'X-Content-Range': content_range, 'Session-ID': session_id, 'Content-Length': str(size)}
    res = requests.post(UPLOAD_URL, data=payload, headers=headers)
    print(res.text)


# 根据文件名hash获得session id
def get_session_id():
    m = hashlib.md5()
    file_name = os.path.basename(FILE_UPLOAD)
    m.update(file_name)
    return m.hexdigest()


def main():
    file_pos = 0
    file_size = os.path.getsize(FILE_UPLOAD)
    fp = open(FILE_UPLOAD, "r")

    while True:
        if file_pos + SEGMENT_SIZE >= file_size:
            upload(fp, file_pos, file_size - file_pos, file_size)
            fp.close()
            break
        else:
            upload(fp, file_pos, SEGMENT_SIZE, file_size)
            file_pos = file_pos + SEGMENT_SIZE