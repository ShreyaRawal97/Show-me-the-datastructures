"""
Blockchain
"""

import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def get_utc_time(self):
        return datetime.utcfromtimestamp(float(self.timestamp))

    def calc_hash(self, str):
        sha = hashlib.sha256()
        hash_str = str.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class LinkedList:
    def __init__(self):
        self.tail = None

    def append(self, data):
        if self.tail is None:
            self.tail = Block(str(datetime.now().timestamp()), data, None)
        else:
            tail = self.tail
            block = Block(str(datetime.now().timestamp()), data, tail)
            self.tail = block
        return self.tail

    def print(self):
        tail = self.tail
        while tail != None:
            print("\nTime Stamp: ", tail.get_utc_time())
            print("Data:", tail.data)

            print("SHA256 Hash: ", tail.hash)
            tail = tail.previous_hash
            if tail != None:
                print("Previous Hash Data:", tail.data)
            else:
                print("Previous Hash Data: None")

#Test Case 1
def testCase1():
    print("Test Case 1 - ")
    block1 = LinkedList()
    block1.append("Data")
    block1.append("Structures")
    block1.append("and")
    block1.append("Algorithms")
    block1.print()

"""
Expected output Case 1:
Test Case 1 -

Time Stamp:  2019-07-31 20:08:35.912332
Data: Algorithms
SHA256 Hash:  3c34d938281ebe9c3c41c91c11178d9527cd460911135a01f553bcc9b4fc859d
Previous Hash Data: and

Time Stamp:  2019-07-31 20:08:35.912311
Data: and
SHA256 Hash:  6201111b83a0cb5b0922cb37cc442b9a40e24e3b1ce100a4bb204f4c63fd2ac0
Previous Hash Data: Structures

Time Stamp:  2019-07-31 20:08:35.912298
Data: Structures
SHA256 Hash:  b912533f7f9a318d96607b263a3fdaf282ed09bcf134c7f60834b32f7f9729f9
Previous Hash Data: Data

Time Stamp:  2019-07-31 20:08:35.912243
Data: Data
SHA256 Hash:  cec3a9b89b2e391393d0f68e4bc12a9fa6cf358b3cdf79496dc442d52b8dd528
Previous Hash Data: None
"""

#Test Case 2
def testCase2():
    print("\nTest Case 2 - ")
    block2 = LinkedList()
    block2.append("Summer")
    block2.append("2019")
    block2.print()

"""
Expected output Case 2:
Test Case 2 -

Time Stamp:  2019-07-31 20:08:35.912806
Data: 2019
SHA256 Hash:  023e33504ab909cf87a6f4e4e545090e40bdc0a2153e5b68b19f7fad2b737904
Previous Hash Data: Summer

Time Stamp:  2019-07-31 20:08:35.912786
Data: Summer
SHA256 Hash:  c0de243c407c0e98ed0364e1d0c636d542318867862aac7e8ae2446d4a328dd6
Previous Hash Data: None
"""

#Test Case 3
def testCase3():
    print("\nTest Case 3 - ")
    block3 = LinkedList()
    block3.append("Computer")
    block3.append("Science")
    block3.print()

"""
Expected output Case 3:
Test Case 3 -

Time Stamp:  2019-07-31 20:08:35.912894
Data: Science
SHA256 Hash:  9d948c73e0ad7a5a213a5e7e00b962531ca6b07992a06bd8c2fc2ac5ae23c51b
Previous Hash Data: Computer

Time Stamp:  2019-07-31 20:08:35.912880
Data: Computer
SHA256 Hash:  76ed42d22129dc354362704eb4b54208041b68736f976932aada43bc0035f7c0
Previous Hash Data: None
"""

#Test Case 4 (empty block chain)
def testCase4():
    print("\nTest Case 4 - ")
    block4 = LinkedList()
    block4.print()

"""
Expected output Case 4:
Test Case 4 -
"""

testCase1()
testCase2()
testCase3()
testCase4()
