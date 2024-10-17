import socket
import asyncio
import re
import exceptions
import utils

print(utils.get_my_ip())
"""
Handshake:
1. Hit target with conn request
2. Target responds with:
                        OKOK - Data transmission can now proceed
                        REFU - Refuse incoming connection
                        BUSY - Target is already connected to someone
3. If OKOK exchange secondary ports  ~2bytes

Header: 
    PROTOCOL | 1byte
    MESSAGE TYPE | 1byte
    SEQ_NUMBER | 4byte   
    PAYLOAD_SIZE | 2byte
"""

async def con_conf() -> tuple[str,int]:
    con_info_in = str(input())    
    ip_check = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    if not re.match(ip_check,con_info_in):
        raise exceptions.InvalidDestData
    split_me_daddy = con_info_in.split(":")
    return (split_me_daddy[0],int(split_me_daddy[1]))    
        

async def handshake():
    
    pass 

async def recv_channel(soc : socket.socket,ip : str,port : int) -> None:
    soc.bind((ip,port))
    soc.setblocking(False)
    while True:
        data =  await asyncio.get_event_loop().sock_recv(soc,1024) 
        print(f"\n{data.decode()}")


async def send_channel(soc : socket.socket,ip:str,port : int) -> None:
    cur_event_loop = asyncio.get_event_loop()
    while True:
        BUDP_in = await cur_event_loop.run_in_executor(None,input,"BUDP_in: ")
        soc.sendto(BUDP_in.encode(),(ip,port))
        await(asyncio.sleep(0.1))



async def main():
    dest_ip,dest_port = await con_conf()
    handshake_soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #############################
    #
    # Handsh
    #
    #############################
    soc_recv = socket.socket(socket.AF_INET,socket.SOCK_DGRAM )  
    soc_send = socket.socket(socket.AF_INET,socket.SOCK_DGRAM )
    await asyncio.gather(recv_channel(soc_recv,utils.get_my_ip(),9053),send_channel(soc_send,dest_ip,dest_port))
    
asyncio.run(main())
