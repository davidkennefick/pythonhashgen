#!/usr/bin/env python
"""
This is designed to provide hashes for files.
in order for the sha3 hashes to work you will nead to install the following modules.
https://github.com/ajakubek/python-sha3
Hashes are
MD5
SHA1
SHA256
SHA512
SHA3256
SHA3512

Author: David Kennefick, @davidkennefick
Purpose: For a forensic lab in my masters course.
"""
import hashlib
import sys
import getopt
import sha3
from sha3 import sha3_256, sha3_512

try: 
    hash_gen = sys.argv[1]
except:
    print "*** You need to supply a filename argument ***"

def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

def SHA1_hash_file(filename):
   # make a hash object
   h = hashlib.sha1()
   # open file for reading in binary mode
   with open(filename,'rb') as file:
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)
   # return the hex representation of digest
   return h.hexdigest()
   
def SHA256_hash_file(filename):
   # make a hash object
   h = hashlib.sha256()
   # open file for reading in binary mode
   with open(filename,'rb') as file:
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)
   # return the hex representation of digest
   return h.hexdigest()

def SHA512_hash_file(filename):
   # make a hash object
   h = hashlib.sha512()
   # open file for reading in binary mode
   with open(filename,'rb') as file:
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)
   # return the hex representation of digest
   return h.hexdigest()

def SHA3_256_hash_file(filename):
   # make a hash object
   h = sha3.sha3_256()
   # open file for reading in binary mode
   with open(filename,'rb') as file:
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)
   # return the hex representation of digest
   return h.hexdigest()


def SHA3_512_hash_file(filename):
   # make a hash object
   h = sha3.sha3_512()
   # open file for reading in binary mode
   with open(filename,'rb') as file:
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)
   # return the hex representation of digest
   return h.hexdigest()

if hash_gen:
    print('The MD5 checksum is', md5Checksum(hash_gen))
    print('The SHA1 checksum is', SHA1_hash_file(hash_gen))
    print('The SHA256 checksum is', SHA256_hash_file(hash_gen))
    print('The SHA512 checksum is', SHA512_hash_file(hash_gen))
    print('The SHA3_256 checksum is', SHA3_256_hash_file(hash_gen))
    print('The SHA3_512 checksum is', SHA3_512_hash_file(hash_gen))