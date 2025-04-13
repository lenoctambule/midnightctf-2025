import requests

URL = 'https://mctf.lamarr.bzh/CFcGFCGgn'
resp = requests.get(URL, verify=False)
pt = ""
with open('stage2', 'w') as f :
    for c in resp.text:
        pt += chr(ord(c) ^ 0x42)
    f.write(pt)