import socket
import os
import os, sys, platform
import datetime

origin = 'https://github.com/B6Infinity/kidey_DEV'

# PULLING CHANGES
print("\n\n\n\033[95m\033[1m\033[4mSYNCHRONISING DATABASE...\033[0m\n\n\n")
os.system('git pull https://github.com/B6Infinity/kidey_DEV master')


# GETTING THE IP ADDRESS OF NATIVE MACHINE (LAN COMPATIBLE)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
native_ip = str(s.getsockname()[0])

platform_os = platform.system()

print(f"\033[95m\033[1m\033[4mStarting Server ---> KIDEY-CORE @ {native_ip}:8000\033[0m")
print('\n\n\n')
if platform_os == "Linux":
    os.system(f'python3 manage.py runserver {native_ip}:8000')
else:
    try:
        os.system(f'python manage.py runserver {native_ip}:8000')
    except Exception:
        print("\n\033[93m'python'\033[0m \033[91mis probably not recognised as a command...\033[0m \n\033[94m\033[1mERROR DETAILS:\033[0m\n\n")
        print(Exception)


# AFTER KEYBOARD INTERRUPT
try:
    pass
finally:
    print("\n\n")
    
    print("\033[95m\033[1m\033[4mPUSHING DATABASE CHANGES\033[0m")

    os.system('git add db.sqlite3')
    os.system(f'git commit -m "Changed db.sqlite3 from {native_ip} at {datetime.datetime.now().date()}--{datetime.datetime.now().time()}"')
    os.system('git push https://github.com/B6Infinity/kidey_DEV master')

    
    


    print("\033[95m\033[1m\033[4mSTOPPING SERVER...\033[0m\n\n")
