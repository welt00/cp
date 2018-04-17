#!/usr/bin/env python3.5

from ctypes import cdll
import os

p = os.getcwd()+'/libfunc.so'
f = cdll.LoadLibrary(p)
print (f.func(99))
