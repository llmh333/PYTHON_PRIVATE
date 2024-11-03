import re
s = input()

email = r'^[a-zA-Z0-9.+%/]+@[a-zA-Z0-9]+.[a-zA-Z0-9.+%/]'

if re.match(email,s): print("Valid")
else: print("Invalid")
