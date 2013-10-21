#!/usr/bin/python

import os       #for using operation system function

#open qemu serial output result
fin = open( './serial.out', 'r' )

#read each line in the file and compare to "Hello"
#if find, it means USART output"Hello" successful
for line in fin.readlines():
    if line.find( "Hello" ):
        print "Find string : \"Hello\" in serial"
    else :
        print "Can't fin string : \"Hello\" "

#file close
fin.close()

#kill qemu
os.system( 'killall qemu-system-arm' )
