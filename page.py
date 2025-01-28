from ast import Bytes
from dash import html,dcc
import dash
import hashlib
import socket
from Crypto.Cipher import AES
from random import randint as r
from Crypto.Util.Padding import unpad
from easygui import codebox
import json as js
global ip
global port
global json
global s
import chardet
from requests import get
def is_socket_connected(sock):
     try: # 获取socket连接的远程地址 
        sock.getpeername() 
        return True 
     except socket.error: 
        return False

json = {}
json["type"] = "load"
ip = '127.0.0.1'
port = 8888
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
url = ''
ends = ['s1','s224','s256','s384','s512','s3_224','s3_256','s3_384','s3_512','m5']
url_con = {
    's1':'sha1',
    's224':'sha224',
    's256':'sha256',
    's384':'sha384',
    's512':'sha512',
    's3_224':'sha3_224',
    's3_256':'sha3_256',
    's3_384':'sha3_384',
    's3_512':'sha3_512',
    'm5':'md5',
}

def c():
    s.close()
def setting():
    setting = f"""## TOR+ Setting ##
    ip = {ip}
    port = {port}
        """
    eval(codebox(msg='Setting', title='Setting', text=setting))


def load(url):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print(url)
        url_end = url.split('.')[-2]
        if (url_end not in ends) or (url.split('.')[-1] != 'csec'):
            return "Please enter a valid URL."
        print(url)
        passkey = hashlib.sha256(str(r(0,100000)).encode('utf-8')).hexdigest()[:16]
        print(passkey)
        json["passkey"] = passkey
        json["urlend"] = url_end
        if not is_socket_connected(s):
            try:
             s.connect((ip,port))
            except socket.error:
                return 'Error102'
        print((ip,port))
        secure_url = getattr(hashlib,url_con[url_end])(url.encode('utf-8')).hexdigest()
        print(secure_url)
        json["url"] = secure_url
        jsonstr = js.dumps(json)
        print(jsonstr)
        s.send(bytes(jsonstr,'utf-8'))
        data = s.recv(1024*1024*5)
        print(data)
        # data = bytes.decode(data,chardet.detect(data)['encoding'])
        print(data)
        cipher = AES.new(passkey.encode('utf-8'), AES.MODE_ECB)
        decrypted_data = cipher.decrypt(data)
        print(decrypted_data)
        decrypted_data = unpad(decrypted_data,16).decode('utf-8')
        print(decrypted_data)
        data = get(decrypted_data)
        s.close()
        if data.status_code == 200:
            return eval(data.text)
        else:
            return 'Error404/403/No Internet Connection'
    except Exception as e:
        print(f"An error occurred: {e}")
        return e