from subprocess import call
import sys

server = str(sys.argv[1])
path = str(sys.argv[2])
code = str(sys.argv[3])

call(["./conf",server,path,code])

