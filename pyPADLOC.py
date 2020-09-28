"""
PyPADLOC, pyPADLOC, a tool for planning how the PADLOC units
          will interact with the WEC controller.

Contact: Bryan Murray, brmurray@mailbox.org

Versions:
    09/28/2020 - First commit (BRM)

"""

#from importlib import reload  

import serial
import datetime
import calendar

def introduce():
    print("""
          pyPADLOC, a tool for planning how the PADLOC units
          will interact with the WEC controller.
          
          For now, it is meant to be used through IPython or another
          interactive Python shell
          """)
    
def parse(input):
    '''Parse the string received from MASTER PADLOC unit'''
    
    # $WERST = master requests status from WEC
    if input==r'$WERST':
        print("Got status request")
        print("reply = $WETST {WecStatus 20 characters}\r\n")
        
    
     # $WECMD = master passed a command from pier -> SHORE -> MASTER -> WEC
    elif input==r'$WECMD':
        print("Got command from pier (via SHORE to MASTER")
        print("reply = none")
        
    
     # $WERST = master requests status from WEC
    elif input==r'$WERTM':
        print("Got time request")
        dt = datetime.datetime.utcnow()
        #posix = calendar.timegm(dt.timetuple())
        
        reply = dt.strftime("%Y%m%d%H%M%S") + "{WecStatus 20 characters}\r\n"
        print(r"reply = " + reply)
        
    elif input==r'$LCDAT':
        print('Got loadcell datagram')
        
    else:
        print("Error: unrecognized input")
        
        
def getStatusMsg():
    '''Request status from higher level controller'''
    
def startSerial():
    """Open serial port and start listening"""
    ser=serial.Serial('COM9')
    print("COM Port=" + ser.name)
    return ser
    
def listen(ser):
    parse(ser.readline()) # read up a to /n (EOL), send to parse()