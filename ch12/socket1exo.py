import re
import socket
try:
    url = input('Enter url: ')
    url = url.lower()
    hostname = url.split('/')[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('hostname', 80))
    # cmd = 'GET' + 'url' + 'HTTP/1.0\r\n\r\n'.encode()
    mysock.send('GET ' + url + ' HTTP/1.0\n\n')
    print(hostname)
except:
    print('You have entered an improperly formatted or non-exisent URL - ', url)
    exit()


while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
mysock.close()
