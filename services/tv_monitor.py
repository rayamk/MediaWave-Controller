import socket
from services.logger import get_logger

logger = get_logger("TVMonitor")

def is_tv_online(ip, port=80):
    try:
        # TV ပွင့်မပွင့် Socket နဲ့ စမ်းကြည့်ခြင်း
        socket.setdefaulttimeout(3)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False

def start_monitor(tv_ip):
    status = is_tv_online(tv_ip)
    if status:
        logger.info(f"TV at {tv_ip} is ONLINE.")
    else:
        logger.info(f"TV at {tv_ip} is OFFLINE.")
    return status


