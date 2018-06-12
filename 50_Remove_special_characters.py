import re
s = "H@e#$l+l/*o"
print(re.sub("[^a-zA-Z0-9_\s]", "", s))
s = "$¥W¢πO}R|%L&@ D"
print(re.sub("[^a-zA-Z0-9_\s]", "", s))
