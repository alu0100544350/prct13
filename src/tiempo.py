#!/usr/bin/python
#!encoding: UTF-8
import time
import math

start=time.time()
import modulo
finish=time.time()-start

print"introduzca el nombre del fichero :"
nombre_fichero=raw_input();
f=open(nombre_fichero,"w")
f.write(str(finish))
f.close() 