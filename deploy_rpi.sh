#!/bin/bash

user='pi'
ip_addr='192.168.1.2'
dest_folder='/home/pi/IoT-Lab-SensorTag/'
source_folder='/home/sylvain/DATA/15_IoT/IoT-Lab-SensorTag'

scp "$source_folderapp/app/backend.py" "$user@$ip_addr:$dest_folder"
scp "$source_folderapp/app/app.py" "$user@$ip_addr:$dest_folder"

ssh "$user@$ip_addr" "python2 -m pip install --user Flask bluepy"
ssh "$user@$ip_addr" "python2 $dest_folder/app.py"
