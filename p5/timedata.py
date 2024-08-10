from datetime import datetime
import time
import builtins
from p5.settings import *

def year():
    return datetime.now().year

def month():
    return datetime.now().month

def day():
    return datetime.now().day

def hour():
    return datetime.now().hour

def minute():
    return datetime.now().minute

def second():
    return datetime.now().second

    
def milli_sec():
    return int(round(time.time() * 1000))

def millis():
    return milli_sec() - builtins.MILLIS
    pass
