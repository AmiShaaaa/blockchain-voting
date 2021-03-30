from block import Block


initial_block = Block("0", ["0,0"])
second_block = Block(initial_block.block_hash, ["0,1"])
third_block = Block(second_block.block_hash, ["0,2"])
forth_block = Block(third_block.block_hash, ["1,3"])
fifth_block = Block(forth_block.block_hash, ["2,2"])
sixth_block = Block(fifth_block.block_hash, ["3,2"])
seveth_block = Block(sixth_block.block_hash, ["4,2"])
eigth_block = Block(seveth_block.block_hash, ["5,2"])
nineth_block = Block(eigth_block.block_hash, ["5,3"])
tenth_block = Block(nineth_block.block_hash, ["5,4"])
eleven_block = Block(tenth_block.block_hash, ["5,6"])
twelve_block = Block(eleven_block.block_hash, ["5,7"])
thirteen_block = Block(twelve_block.block_hash, ["6,7"])
fourteen_block = Block(thirteen_block.block_hash, ["6,8"])

print(initial_block.transactions)

print(initial_block.block_hash)
print(second_block.transactions)

print(second_block.block_hash)
print(third_block.transactions)

print(third_block.block_hash)
print(forth_block.transactions)

print(forth_block.block_hash)
print(fifth_block.transactions)

print(fifth_block.block_hash)
print(sixth_block.transactions)

print(sixth_block.block_hash)
print(seveth_block.transactions)

print(seveth_block.block_hash)
print(eigth_block.transactions)

print(eigth_block.block_hash)
print(nineth_block.transactions)

print(nineth_block.block_hash)
print(tenth_block.transactions)

print(tenth_block.block_hash)
print(eleven_block.transactions)

print(eleven_block.block_hash)
print(twelve_block.transactions)

print(twelve_block.block_hash)
print(thirteen_block.transactions)

print(thirteen_block.block_hash)
print(fourteen_block.transactions)

var1 = 123
var2 = 456
str1 = str(var1)
str2 = str(var2)
str3 = str1 + "," + str2
print(str3)
