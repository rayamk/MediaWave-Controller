import os

def get_tv_status(ip):
    response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    return "Active" if response == 0 else "Offline"

