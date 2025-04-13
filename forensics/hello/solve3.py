import base64 as b

encoded = 'ADoHdRg9URIYKjAHF0MDGhJIZmwgIFIVLBgyUgITUhU3AwpqHg=='
decoded = b.b64decode(encoded)
key = b"MyS3cr3t"
out = ""
for i in range(len(decoded)) :
    out += chr(key[i % len(key)] ^ decoded[i])
print(out)