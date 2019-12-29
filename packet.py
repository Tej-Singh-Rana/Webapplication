#!/usr/bin/python3

import  cgi
import cgitb

print("Content-Type: text/html")
print("")

webdata=cgi.FieldStorage()

x1=webdata.getvalue('x')
x2=webdata.getvalue('y')

print(x1)
print(type(x1))
print(x2)
print(type(x2))


sum=int(x1)+int(x2)
print(sum)


