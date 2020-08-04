# coding=utf-8
import socket
import pymongo
import requests
import ftplib
from tqdm import tqdm
import sys
from concurrent.futures import ThreadPoolExecutor
import logging
logging.captureWarnings(True)


def redis(ip):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 6379))
        s.send(bytes("INFO\r\n", 'UTF-8'))
        result = s.recv(1024).decode()
        if "redis_version" in result:
            print(ip + ":6379 redis未授权")
        s.close()
    except Exception as e:
        pass
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 7001))
        s.send(bytes("INFO\r\n", 'UTF-8'))
        result = s.recv(1024).decode()
        if "redis_version" in result:
            print(ip + ":7001 redis未授权")
        s.close()
    except Exception as e:
        pass
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 7002))
        s.send(bytes("INFO\r\n", 'UTF-8'))
        result = s.recv(1024).decode()
        if "redis_version" in result:
            print(ip + ":7002 redis未授权")
        s.close()
    except Exception as e:
        pass
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 7000))
        s.send(bytes("INFO\r\n", 'UTF-8'))
        result = s.recv(1024).decode()
        if "redis_version" in result:
            print(ip + ":7000 redis未授权")
        s.close()
    except Exception as e:
        pass
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 32768))
        s.send(bytes("INFO\r\n", 'UTF-8'))
        result = s.recv(1024).decode()
        if "redis_version" in result:
            print(ip + ":32768 redis未授权")
        s.close()
    except Exception as e:
        pass
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 7777))
        s.send(bytes("INFO\r\n", 'UTF-8'))
        result = s.recv(1024).decode()
        if "redis_version" in result:
            print(ip + ":7777 redis未授权")
        s.close()
    except Exception as e:
        pass
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 6969))
        s.send(bytes("INFO\r\n", 'UTF-8'))
        result = s.recv(1024).decode()
        if "redis_version" in result:
            print(ip + ":6969 redis未授权")
        s.close()
    except Exception as e:
        pass
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 6699))
        s.send(bytes("INFO\r\n", 'UTF-8'))
        result = s.recv(1024).decode()
        if "redis_version" in result:
            print(ip + ":6699 redis未授权")
        s.close()
    except Exception as e:
        pass
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 10000))
        s.send(bytes("INFO\r\n", 'UTF-8'))
        result = s.recv(1024).decode()
        if "redis_version" in result:
            print(ip + ":10000 redis未授权")
        s.close()
    except Exception as e:
        pass
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 6779))
        s.send(bytes("INFO\r\n", 'UTF-8'))
        result = s.recv(1024).decode()
        if "redis_version" in result:
            print(ip + ":6779 redis未授权")
        s.close()
    except Exception as e:
        pass
    finally:
        bar.update(1)

def mongodb(ip):
    try:
        conn = pymongo.MongoClient(ip, 27017, socketTimeoutMS=4000)
        dbname = conn.list_database_names()
        print(ip + ":27017 mongodb未授权")
        conn.close()
    except Exception as e:
        pass
    try:
        conn = pymongo.MongoClient(ip, 28017, socketTimeoutMS=4000)
        dbname = conn.list_database_names()
        print(ip + ":28017 mongodb未授权")
        conn.close()
    except Exception as e:
        pass
    finally:
        bar.update(1)

def memcached(ip):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 11211))
        s.send(bytes('stats\r\n', 'UTF-8'))
        if 'version' in s.recv(1024).decode():
            print(ip + ":11211 memcached未授权")
        s.close()
    except Exception as e:
        pass
    finally:
        bar.update(1)

def elasticsearch(ip):
    try:
        url = 'http://' + ip + ':9200/_cat'
        r = requests.get(url, timeout=5)
        if '/_cat/master' in r.content.decode():
            print(ip + ":9200 elasticsearch未授权")
    except Exception as e:
        pass
    finally:
        bar.update(1)

def zookeeper(ip):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 2181))
        s.send(bytes('envi', 'UTF-8'))
        data = s.recv(1024).decode()
        s.close()
        if 'Environment' in data:
            print(ip + ":2181 zookeeper未授权")
    except:
        pass
    finally:
        bar.update(1)

def ftp(ip):
    try:
        ftp = ftplib.FTP.connect(ip,21,timeout=5)
        ftp.login('anonymous', 'Aa@12345678')
        print(ip + ":21 FTP未授权")
    except Exception as e:
        pass
    finally:
        bar.update(1)

def CouchDB(ip):
    try:
        url = 'http://' + ip + ':5984'+'/_utils/'
        r = requests.get(url, timeout=5)
        if 'couchdb-logo' in r.content.decode():
            print(ip + ":5984 CouchDB未授权")
    except Exception as e:
        pass
    try:
        url = 'https://' + ip +'/_utils/'
        r = requests.get(url, timeout=5,verify = False)
        if 'couchdb-logo' in r.content.decode():
            print(ip + ":443 CouchDB未授权")
    except Exception as e:
        pass
    try:
        url = 'http://' + ip + ':5986'+'/_utils/'
        r = requests.get(url, timeout=5)
        if 'couchdb-logo' in r.content.decode():
            print(ip + ":5986 CouchDB未授权")
    except Exception as e:
        pass
    try:
        url = 'http://' + ip +'/_utils/'
        r = requests.get(url, timeout=5)
        if 'couchdb-logo' in r.content.decode():
            print(ip + ":80 CouchDB未授权")
    except Exception as e:
        pass
    finally:
        bar.update(1)

def docker(ip):
    try:
        url = 'http://' + ip + ':2375'+'/version'
        r = requests.get(url, timeout=5)
        if 'ApiVersion' in r.content.decode():
            print(ip + ":2375 docker api未授权")
    except Exception as e:
        pass
    finally:
        bar.update(1)

def Hadoop(ip):
    try:
        url = 'http://' + ip + ':50070'+'/dfshealth.html'
        r = requests.get(url, timeout=5)
        if 'hadoop.css' in r.content.decode():
            print(ip + ":50070 Hadoop未授权")
    except Exception as e:
        pass
    try:
        url = 'http://' + ip + ':50090'+'/dfshealth.html'
        r = requests.get(url, timeout=5)
        if 'hadoop.css' in r.content.decode():
            print(ip + ":50090 Hadoop未授权")
    except Exception as e:
        pass
    try:
        url = 'http://' + ip + ':9870'+'/dfshealth.html'
        r = requests.get(url, timeout=5)
        if 'hadoop.css' in r.content.decode():
            print(ip + ":9870 Hadoop未授权")
    except Exception as e:
        pass
    try:
        url = 'http://' + ip + ':50075'+'/dfshealth.html'
        r = requests.get(url, timeout=5)
        if 'hadoop.css' in r.content.decode():
            print(ip + ":50075 Hadoop未授权")
    except Exception as e:
        pass
    try:
        url = 'http://' + ip + ':50030'+'/dfshealth.html'
        r = requests.get(url, timeout=5)
        if 'hadoop.css' in r.content.decode():
            print(ip + ":50030 Hadoop未授权")
    except Exception as e:
        pass
    finally:
        bar.update(1)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage:python3 unauthorized-check.py url.txt")
    file = sys.argv[1]
    with open(file, "r", encoding='UTF-8') as f:
        line = [i for i in f.readlines()]
    bar = tqdm(total=len(line)*9)
    with ThreadPoolExecutor(600) as pool:
        for target in line:
            target=target.strip()
            pool.submit(redis, target)
            pool.submit(Hadoop, target)
            pool.submit(docker, target)
            pool.submit(CouchDB, target)
            pool.submit(ftp, target)
            pool.submit(zookeeper, target)
            pool.submit(elasticsearch, target)
            pool.submit(memcached, target)
            pool.submit(mongodb, target)
