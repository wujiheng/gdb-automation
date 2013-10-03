#!/usr/bin/python

import os

fin = open( './serial.out', 'r' )
for line in fin.readlines():
    if line.find( "Hello" ):
        print "Find string : \"Hello\" in serial"
    else :
        print "Can't fin string : \"Hello\" "
fin.close()

os.system( 'killall qemu-system-arm' )
