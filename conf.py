import sys
import base64
import random
import string

letters= string.ascii_letters + string.digits
part1 = ''.join(random.sample(letters,12))
part2 = ''.join(random.sample(letters,15))


#action = str(sys.argv[1])
server = str(sys.argv[1])
path = str(sys.argv[2])
code = str(sys.argv[3])

value1 = server[7:]
value2 = path[5:]
value3 = code[5:]

data = base64.b64encode(value3.encode())

newdata = part1 + data + part2

finalvalue = value1 + "|" + value2 + "|" + newdata
#print "Status"
#print finalvalue

f = open("data.conf", "w")
f.write(finalvalue)
f.close()

print "Status"
print "Settings Updated"
