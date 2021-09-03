import hash
import ubinascii
def new(k, m):
    SHA1 = hash.sha1
    SHA1_BLOCK_SIZE = 64
    KEY_BLOCK = k + (b'\0' * (SHA1_BLOCK_SIZE - len(k)))
    KEY_INNER = bytes((x ^ 0x36) for x in KEY_BLOCK)
    KEY_OUTER = bytes((x ^ 0x5C) for x in KEY_BLOCK)
    inner_message = KEY_INNER + m
    outer_message = KEY_OUTER + ubinascii.unhexlify(SHA1(inner_message))
    return SHA1(outer_message)
