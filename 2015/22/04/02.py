
import hashlib
import sys
from tqdm import tqdm

myInput = "iwrupvqb"

for i in tqdm(range(0, 99999999999999999), desc="Searching..."):
    toHash = myInput + str(i)
    result = hashlib.md5(toHash.encode())
    output = result.hexdigest() 
    if (output[:6] == "000000"):
        print(i)
        sys.exit(0)
print("failure")

