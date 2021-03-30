import hashlib
import base64

class Block:
    def __init__(self, previous, transaction):
        self.transactions = transaction
        self.previous = previous
        string_to_hash = "".join(transaction) + previous
        self.block_hash = base64.encode(string_to_hash.encrypt())


first_block = Block("0", ["0,0,0,0,0,0"])
vote1 = 0
vote2 = 0
vote3 = 0
vote4 = 0
vote5 = 0
vote6 = 0
run = 1
prev_block = first_block

vote = int(input())
if vote == 1:
    vote1 += 1
elif vote == 2:
    vote2 = vote2 + 1
elif vote == 3:
    vote3 = vote3 + 1
elif vote == 4:
    vote4 = vote4 + 1
elif vote == 5:
    vote5 = vote5 + 1
elif vote == 6:
    vote6 = vote6 + 1
str1 = str(vote1)
str2 = str(vote2)
str3 = str(vote3)
str4 = str(vote4)
str5 = str(vote5)
str6 = str(vote6)

final_str = str1 + "," + str2 + "," + str3 + "," + str4 + "," + str5 + "," + str6

new_block = Block(prev_block.block_hash, [final_str])

print(prev_block.block_hash)
print(new_block.transactions)
print(new_block.block_hash)
prev_block = new_block


while run > 0:

    vote = int(input())
    if vote == 1:
        vote1 += 1
    elif vote == 2:
        vote2 = vote2 + 1
    elif vote == 3:
        vote3 = vote3 + 1
    elif vote == 4:
        vote4 = vote4 + 1
    elif vote == 5:
        vote5 = vote5 + 1
    elif vote == 6:
        vote6 = vote6 + 1
    str1 = str(vote1)
    str2 = str(vote2)
    str3 = str(vote3)
    str4 = str(vote4)
    str5 = str(vote5)
    str6 = str(vote6)

    final_str = str1 + "," + str2 + "," + str3 + "," + str4 + "," + str5 + "," + str6

    new_block = Block(prev_block.block_hash, [final_str])

    print(prev_block.block_hash)
    print(new_block.transactions)
    print(new_block.block_hash)
    prev_block = new_block



