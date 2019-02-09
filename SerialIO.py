#!/usr/bin/env python3
#Code mainly written by Maxime T. aka amaisjeg ;)
#https://github.com/omaisjeg
from threading import Thread
from queue import Queue
from time import sleep
import serial

ser = serial.Serial(port='/dev/ttyS0',baudrate = 57600,timeout=0.01)


def threadenvoie(threadname, q):
    counter = 0
    ser.write(counter.to_bytes(3,byteorder='big'))
    while 1:
        counter = 1 +  q.get()
        print('envoie',counter)
        print(counter.to_bytes(3,byteorder='big'))
        ser.write(counter.to_bytes(3,byteorder='big'))
        sleep(.05)


def threadrecoie(threadname, q):
    sleep(.5)
    while 1:
        sleep(.05)
        read_serial= ser.read(size=3)
        print(read_serial)
        read_serial = int.from_bytes(read_serial,byteorder='big')
        print('recoie',read_serial)
        q.put(read_serial)



varshare = Queue()


env = Thread( target=threadenvoie, args=("Envoie", varshare ) )
rec = Thread( target=threadrecoie, args=("Reçoie", varshare) )

env.start()
rec.start()
env.join()
rec.join()
