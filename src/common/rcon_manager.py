from rcon.battleye import Client

client =  Client('127.0.0.1', 25575, passwd='123456')

def is_broadcast_msg_valid(msg: str):
    return msg.isalnum()

def broadcast(msg: str):
    if (not is_broadcast_msg_valid(msg)): raise Exception("Invalid broadcast string");
    client.run("Broadcast", msg)
