import socket
import os
import os, sys, platform


# PULLING CHANGES
print("\n\n\nSYNCHRONISING DATABASE...\n\n\n")
os.system('git pull origin master')


# GETTING THE IP ADDRESS OF NATIVE MACHINE (LAN COMPATIBLE)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
native_ip = str(s.getsockname()[0])

platform_os = platform.system()

if platform_os == "Linux":
    print(f"Starting Server ---> KIDEY-CORE @ {native_ip}:8000\n\n\n")
    os.system(f'python3 manage.py runserver {native_ip}:8000')
else:
    try:
        os.system(f'python manage.py runserver {native_ip}:8000')
    except Exception:
        print("\n'python' is probably not recognised as a command... \nERROR DETAILS:\n\n")
        print(Exception)


# AFTER KEYBOARD INTERRUPT
try:
    pass
finally:
    print("\n\n")
    
    print("PUSHING DATABASE CHANGES")



    print("STOPPING SERVER...\n\n")