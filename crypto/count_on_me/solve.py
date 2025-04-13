from pwn import *
from Crypto.Util.Padding import unpad


# This script is from http://sebven.com/ctf/2021/08/23/corCTF2021-babypad.html
# Too lazy to do it myself :DDDD

def AES_CTR_POA(ENC, padding_oracle):
    """ Perform AES-CTR Padding Oracle Attack on given ciphertext and oracle function. """

    # Initliase decryption string
    DEC = b''

    # For every 16-byte block
    while len(ENC) > 16:
        BLOCK = b''
        for l in range(1,16+1):
            padbyt = l

          	# Collect all valid bytes
            valid_byts = []

            for k in range(256):

            	# Alter a single byte of ciphertext 
                fuzz = ENC[:-l] + bytes([k]) + bytes([ENC[len(ENC)-(l-1):][i] ^ BLOCK[i] ^ padbyt for i in range(len(BLOCK))])

                assert len(fuzz) == len(ENC)

                # Pass to the oracle and recvieve unpadding success {0,1}
                derr = padding_oracle(fuzz)

                # If valid, the decrypted byte must be the padding value
                if derr:
                    valid_byts += [k]

            # Multiple hits, take the new one
            if len(valid_byts) > 1:
                if ENC[-l] in valid_byts:
                    valid_byts.remove(ENC[-l])

            # Still multiple hits, error
            if len(valid_byts) != 1:
                print(valid_byts,l)
                return 'ERROR'

            # Recover plaintext byte and prepend to BLOCK
            pt_byt = valid_byts[0] ^ padbyt ^ ENC[-l]
            BLOCK = bytes([pt_byt]) + BLOCK
            print(BLOCK+DEC)

        # Prepend BLOCK to DEC string
        DEC = BLOCK + DEC

        # Remove block from ciphertext
        ENC = ENC[:-16]

    # Return
    return DEC


# Imports
from pwn import *

# Remote connection
# r = process(["python3", "./app.py"])
r = remote("chall3.midnightflag.fr", 12040)
# context.log_level = "DEBUG"

ENCFLAG = r.recvline()
ENCFLAG = bytes.fromhex(ENCFLAG.split(b'\n')[0].split(b'=')[1].decode())

def request_decrypt(ciphertext):
    r.sendlineafter(b"enc=", ciphertext.hex().encode())
    response = r.recvline().decode().strip()
    if "Look's good" in response:
        return 1
    else:
        return 0 

# FLAG!
print(AES_CTR_POA(ENCFLAG, request_decrypt))




# d = r.recvline()
# d = bytes.fromhex(d.split(b'\n')[0].split(b'=')[1].decode())
# iv = d[:16]
# ct = d[16:]
# pt = b""

# block_size = 16
# flag = b''

# for block_start in range(0, len(ct), block_size):
#     current_block = ct[block_start:block_start+block_size]
#     recovered = bytearray(block_size)
    
#     for byte_pos in range(block_size - 1, -1, -1):  # from last byte to first
#         for guess in range(256):
#             # Craft a modified IV to test the padding
#             modified_iv = bytearray(iv)
            
#             # Apply XOR to control padding validation
#             for k in range(byte_pos + 1, block_size):
#                 modified_iv[k] ^= recovered[k] ^ (block_size - byte_pos)
            
#             modified_iv[byte_pos] ^= guess ^ (block_size - byte_pos)

#             # Send the modified ciphertext
#             test_ct = bytes(modified_iv) + current_block
#             r.sendlineafter("enc=", test_ct.hex())
#             response = r.recvline().decode().strip()
            
#             if "Look's good" in response:
#                 recovered[byte_pos] = guess
#                 print(f"Block {block_start//16}: {bytes(recovered)}")
#                 break
    
#     flag += bytes(recovered)

# # The flag might have padding, so we unpad it
# try:
#     flag = unpad(flag, block_size)
# except:
#     pass

# print(flag)
