#!/usr/bin/env python
import sys
from tc3625 import *


dev = TC3625_Serial()

if 1:
    dev.print_cmds()
    
if 0:
    dev.print_help_all()

if 0:    
    dev.print_help('control type',rw=False)

dev.open()


if 1:
    cmds = dev.serial_cmds.keys()
    cmds.sort()
    for k in cmds:
        if dev.serial_cmds[k]['read'] != None:
            print '%s:'%(k,),
            sys.stdout.flush()
            val = dev.read(k)
            print val

if 0:
    n = 100
    print 'read alarm deadband:', dev.read('alarm deadband')
    
    val = dev.write('alarm deadband', n)
    print 'write alarm deadband:', val
    
    print 'read alarm deadband:', dev.read('alarm deadband')
    
    


dev.close()



# val = to_twoscomp(-1)
# print val


# val = from_twoscomp('1')
# print val

# val = from_twoscomp('ffffffff')
# print val
