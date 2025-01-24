import os
import subprocess

while True:
    # Display a menu to the user
    print("\nPlease select the information you want to see:")
    print("1. Date and time")
    print("2. OS version")
    print("3. Hostname")
    print("4. IP address")
    print("5. MAC address")
    print("6. System uptime")
    print("7. Disk space")
    print("8. Installed software")
    print("9. Memory details")
    print("10. Exit")
    choice = input("Enter your choice: ")

    # Get the selected information
    if choice == '1':
        print("\nDate and time:", subprocess.getoutput("date /t && time /t"))
    elif choice == '2':
        os_version = subprocess.getoutput("systeminfo | findstr /B /C:\"OS Name\"")
        print("\nOS version:", os_version.split(":")[1].strip())
    elif choice == '3':
        print("\nHostname:", subprocess.getoutput("hostname"))
    elif choice == '4':
        ip_address = subprocess.getoutput("ipconfig | findstr /i 'ipv4'")
        print("\nIP address:", ip_address.split(":")[1].strip())
    elif choice == '5':
        mac_address = subprocess.getoutput("getmac | findstr /v 'Transport'")
        print("\nMAC address:", mac_address.strip().split(' ')[0])
    elif choice == '6':
        uptime = subprocess.getoutput("net stats srv | findstr 'Statistics since'")
        print("\nSystem uptime since:", uptime.split('since')[1].strip())
    elif choice == '7':
        print("\nDisk space:", subprocess.getoutput("wmic logicaldisk get size,freespace,caption"))
    elif choice == '8':
        print("\nInstalled software:")
        print(subprocess.getoutput("wmic product get name"))
    elif choice == '9':
        mem = subprocess.getoutput("wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Value")
        mem_list = {line.split('=')[0]: int(line.split('=')[1]) for line in mem.splitlines() if line.strip()}
        mem_total = mem_list["TotalVisibleMemorySize"]
        mem_free = mem_list["FreePhysicalMemory"]
        mem_used = mem_total - mem_free
        print("\nMemory details:")
        print(f"Memory Usage: {mem_used * 1024} bytes used out of {mem_total * 1024} bytes")
    elif choice == '10':
        print("Exiting script...")
        break
    else:
        print("\nInvalid choice")
