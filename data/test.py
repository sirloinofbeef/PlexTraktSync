import os
import sys

print("hello world")
os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)