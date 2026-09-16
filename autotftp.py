#!/bin/env python3

# This is an automatic backup script #

import paramiko
import time
from datetime import datetime

# Config #
username = "student" # SSH Username
password = "cisco" #SSH password
tftp = "192.168.0.0" #TFTP ip
device_list_file = "devices.txt"
log_file = "backup_log.txt"

# Function

def backup_device(ip):
    try:
        # Create SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(ip, username=username, password=password, timeout=10)
        
        print(f"Connected to {ip}")
        
        # Start interactive shell
        remote_con = ssh.invoke_shell()
        time.sleep(1) 
        
        remote_con.send("enable\n")
        time.sleep(1)
        remote_con.send(password + "\n")
        time.sleep(1)
        
        # Set terminal Length to avoid 0 
        remote_con.send("terminal length 0\n")
        time.sleep(1)
        
        #Backup commands
        filename = f"{ip}_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.cfg"
        cmd = f"copy running-config tftp:\n"
        remote_con.send(cmd)    
        time.sleep(2)
        remote_con.send(f"{tftp_server}\n")
        time.sleep(2)
        remote_con.send(f"{filename}\n")
        time.sleep(5)  # Wait for the command to complete
        
        #Read Output
        output = remote_con.recv(65535).decode('utf-8')
        ssh.close
        
        if "Ok" in output or "copied" in output or "Copy complete" in output:
            log_message = f"{datetime.now()} - SUCCESS - {ip} - {filename}\n"
        else:
            log_message = f"{datetime.now()} - FAILED - {ip} - {filename}\n"
        print(log_message.strip())
        with open(log_file, "a") as log:
            log.write(log_message)
            
    except Exception as e:
        error_msg = f"{datetime.now()} - ERROR - {ip} - {str(e)}\n"
        print(error_msg.strip())
        with open(log_file, "a") as log:
            log.write(error_msg)
            
           
            # Main Script #
if __name__ == "__main__":
    with open(device_list_file, "r") as f:
        devices = [line.strip() for line in f if line.strip()]
    
    print(f"Starting backup for {len(devices)} devices...\n")
    for device in devices:
        backup_device(device)
    
    print("\nBackup process completed.Check backup_log.txt for details.")
    
    
    