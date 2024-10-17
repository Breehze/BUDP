import socket
"""
Header: 
    PROTOCOL_ID | 4byte
    MESSAGE TYPE | 1byte
    SEQ_NUMBER | 4byte   
    PAYLOAD_SIZE | 2byte
    TTL | 4 bytes
"""

def header_packer(protocol:str,message_type:int,seq_number:int,payload_size:int) -> bytes:
    padding = lambda num,byte_size: num.to_bytes(byte_size,byteorder = "big")
    smashed_header = protocol.encode() + padding(message_type,1) + padding(seq_number,4) + padding(payload_size,2)
    return smashed_header

def header_unpacker(header:bytes):
    print(header)
    return header[:4].decode(),int.from_bytes(header[4:5]),int.from_bytes(header[5:9]),int.from_bytes(header[9:11])


def get_my_ip() -> str:
    return socket.gethostbyname(socket.gethostname())


#packed_header = header_packer("BUDP",1,1,1)
#print(header_unpacker(packed_header))
