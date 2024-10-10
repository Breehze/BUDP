import socket
import asyncio
import re

class InvalidDestData(Exception):
    pass


def con_conf() -> tuple[str,int]:
    con_info_in = str(input())    
    ip_check = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    if not re.match(ip_check,con_info_in):
        raise InvalidDestData
    split_me_daddy = con_info_in.split(":")
    return (split_me_daddy[0],int(split_me_daddy[1]))    
        

async def handshake():
    pass

async def recv_channel(soc : socket.socket,ip : str,port : int) -> None:
    soc.bind((ip,port))
    soc.setblocking(False)
    while True:
        data =  await asyncio.get_event_loop().sock_recv(soc,1024) 
        print(data)


async def send_channel(soc : socket.socket,ip:str,port : int) -> None:
    cur_event_loop = asyncio.get_event_loop()
    while True:
        BUDP_in = await cur_event_loop.run_in_executor(None,input,"BUDP_in: ")
        soc.sendto(BUDP_in.encode(),(ip,port))
        await(asyncio.sleep(0.1))



async def main():
    dest_ip,dest_port = con_conf()
    print(dest_ip,dest_port)
    handshake_soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #############################
    #
    # Handshake --> peer ip
    #
    #############################
    soc_recv = socket.socket(socket.AF_INET,socket.SOCK_DGRAM )  
    soc_send = socket.socket(socket.AF_INET,socket.SOCK_DGRAM )
    await asyncio.gather(recv_channel(soc_recv,"147.175.160.21",9053),send_channel(soc_send,dest_ip,dest_port))
    



asyncio.run(main())
