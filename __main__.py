import os
from ctypes import CDLL

base = os.path.dirname(os.path.abspath(__file__))
lib = CDLL(os.path.join(base, 'lib.so'))
print(lib.add(5, 7))
