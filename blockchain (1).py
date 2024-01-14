
import pickle
import mediapipe as mp
import numpy as np
import pandas as pd
import hashlib
import time
import json
model_dict = pickle.load(open('./model.p', 'rb'))

model = model_dict['model']
class Block:
    def __init__(self, index, previous_hash, timestamp, data, model_output, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.model_output = model_output
        self.hash = hash
def Covid():
    ip=''
    op=''
    for i in range (1,6):
        p = []
        print("give", i ,"patient details")
        n=input()
        for i in n.split(","):
            if i=='yes':
                ip=ip+'1'
                p.append(1)
            elif i=='no':
                ip=ip+'0'
                p.append(0)
 
        t = model.predict([p])
    
        if t[0]<0.5:
            op=op+'0'
            print("COVID TEST-NO")
        else:
            op=op+'1'
            print("COVID TEST-YES")
    return ip,op
def calculate_hash(index, previous_hash, timestamp, data, model_output,ip,op):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data) + str(model_output)+ip+op
    if index==0:
        print("Hash is calculated for Gensis Block 'BLOCKCHAIN IS CREATED'")
    else:
        print("Hash is calculated for Block:",index,"and appended to Blockchain")
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    ip,op=Covid()
    
    return Block(0, "0", time.time(), "Genesis Block", "Initial Model Output", calculate_hash(0, "0", time.time(), "Genesis Block", "Initial Model Output",ip,op))

def create_new_block(previous_block, data, model_output):
    index = previous_block.index + 1
    timestamp = time.time()
    ip,op=Covid()
    hash = calculate_hash(index, previous_block.hash, timestamp, data, model_output,ip,op)
    return Block(index, previous_block.hash, timestamp, data, model_output, hash)

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Add blocks to the blockchain with simulated ML model outputs
num_blocks_to_add = 2
for i in range(num_blocks_to_add):
    data = f"Input Data #{i+1}"
    model_output = f"Model Output #{i+1}"
    new_block = create_new_block(previous_block, data, model_output)
    blockchain.append(new_block)
    previous_block = new_block
#Print the blockchain
for block in blockchain:
    print(f"Index: {block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Model Output: {block.model_output}")
    print(f"Hash: {block.hash}")
    print("\n" +"="*50+"\n")