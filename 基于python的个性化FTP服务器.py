#!/usr/bin/python

#   Location: /home/daiqiang/桌面
#   Date: 2018.04.25 10:45
#   Version: 1.0.1
#   Desktop environment : Budgie Desktop Running on Ubuntu 17.10
#   OS：Ubuntu 17.10 Artful Aardvark
#   Copyright (c) 2018 by DaiQiang. All Rights Reserved.

import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import socket

def main():
    os.system("title 基于python的个性化FTP服务器")
    os.system("color 2e")
    path = input("input your path:")
    if  path == 'default':
        path = '/media/daiqiang/DATA'
    if  path == 'default windows':
        path = 'D:/'
    myname = socket.getfqdn(socket.gethostname())
    ip=socket.gethostbyname(myname)
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    # authorizer.add_user('daiqiang', '12345', '.', perm='elradfmwM')
    authorizer.add_anonymous(path)

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    address = (ip, 2121) # Your IP address
    server = FTPServer(address, handler)

    # set a limit for connections
    #server.max_cons = 256
    #server.max_cons_per_ip = 5
    server.serve_forever() # start ftp server

if __name__ == '__main__':
    main()
