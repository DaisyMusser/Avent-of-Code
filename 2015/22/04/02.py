
import hashlib
import sys

myInput = "iwrupvqb"

for i in range(0, 99999999):
    toHash = myInput + str(i)
    result = hashlib.md5(toHash.encode())
    output = result.hexdigest() 
    if (output[:5] == "000000"):
        print(i)
        sys.exit(0)
print("failure")

