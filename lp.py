from subprocess import call
import sys

#action = str(sys.argv[1])
username = str(sys.argv[1])

call(["./ldap2",username])

