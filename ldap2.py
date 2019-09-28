from ldap3 import Server, Connection, ALL
from ldap3 import MODIFY_ADD, MODIFY_REPLACE, MODIFY_DELETE
import sys
import base64


with open("data.conf") as f:
  lineList = f.readlines()
words = lineList[0].split("|")
#for i in words:
#    print i

ldapserver = words[0]
ldapdn = words[1]
ldappass = words[2].strip()

tempdata = ldappass[12:-15]

data = base64.b64decode(tempdata.decode())

#print ldapserver, ldapdn, ldappass

#action = str(sys.argv[1])
username = str(sys.argv[1])



server = Server(ldapserver, get_info=ALL)
conn = Connection(server, ldapdn, data, auto_bind=True)

status = conn.modify('cn=' + username + ',ou=university,DC=wec,DC=com', {'lockoutTime': [(MODIFY_REPLACE, ['0'])]})

#print status

if status ==True:
    print "Status"
    print "Success"
else:
    print "Status"
    print "Failed"
