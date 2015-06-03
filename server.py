#!/usr/bin/env python
#Using http://ilab.cs.byu.edu/python/threadingmodule.html as a template to implement threading

import socket
import sys
import os.path
import threading

#Server class will initate on execution of the program, opening a socket to listen and creating client threads to service
class Server:
  def __init__(self):
    self.host = ''
    self.port = 40000
    self.server = None
    self.threads = []

  def open_socket(self):
    self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    self.server.bind((self.host,self.port))
    self.server.listen(1)

  def run(self):
    self.open_socket()
    while True:
      client = Client(self.server.accept())
      client.start()
      self.threads.append(client)
    self.server.close()

#Clients will send requests looking for a file on the file system
class Client(threading.Thread):
  def __init__(self,(client,address)):
    threading.Thread.__init__(self)
    self.client = client
    self.address = address

  def run(self):
    while True:
      data = self.client.recv(1024)

      #Retrieve requested filename
      name = data.splitlines()
      print name
      name = name[0].split()
      filename = name[1]
      print filename

      #fetch file contents
      name = filename[1:len(filename)]
      #favicon.ico was an anamoly that I didn't know how to actually remove
      #there would be a second get request for this file so I simply stopped it
      if name == 'favicon.ico':
        #self.client.close()
        break
      #if the file is successfully found on the file system then its contents will be read and sent back to the client
      if os.path.isfile(name):
        #200
        f = open(name, 'r')
        fil = f.read()
        f.close()
        print fil

        #Create HTML page to return
        html = '\n<!doctype html>\n'
        html += '<html>\n'
        html += '<head>\n'
        html += '<meta charset="utf-8">\n'
        html += '<title>File Content</title>\n'
        html += '</head>\n'
        html += '<body><p>' + fil + '</p></body>\n'
        html += '</html>\n'

        #Create the appropriate header
        temp = str(self.client.getsockname())
        Host = '127.0.0.1:' + str(temp[1])
        Rsp = 'HTTP/1.1 200 OK\n'
        Rsp += 'Connection: keep-alive\n'
        Rsp += 'Host: ' + Host + '\n'
        Rsp += 'Content-Type: text/html; charset=utf-8\n'
        Rsp += 'Content-length: ' + str(len(html))+'\n'
        #Send file contents to the client
        self.client.send(Rsp)
        self.client.send(html)
        self.client.close()
      #if the file was not found the client will encounter a 404 File not found
      else:  
        #404
        #webpage being crafted
        html = '\n<!doctype html>\n'
        html += '<html>\n'
        html += '<head>\n'
        html += '<meta charset="utf-8">\n'
        html += '<title>404 File Not Found</title>\n'
        html += '</head>\n'
        html += '<body><p> 404 File Not Found </p></body>\n'
        html += '</html>\n'
 
        #tcp response header
        temp = str(self.client.getsockname())
        Host = '127.0.0.1:' + str(temp[1])
        NF = 'HTTP/1.1 404 Not Found\n'
        NF += 'Connection: keep-alive\n'
        NF += 'Host: ' + Host + '\n'
        NF += 'Content-Type: text/html; charset=utf-8\n'
        NF += 'Content-length: ' + str(len(html)) + '\n'

        #send the header then the page
        self.client.send(NF)
        self.client.send(html)
        self.client.close()

if __name__ == "__main__":
  s = Server()
  s.run()
        

