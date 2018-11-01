#!/bin/bash

user='pi'
ip_addr='192.168.1.2'
dest_folder='/home/pi/IoT-Lab-SensorTag/'
source_folder='/home/sylvain/DATA/15_IoT/IoT-Lab-SensorTag'

scp "$source_folderapp/app/{backend, app}.py" "$user@$ip_addr:$dest_folder"

ssh "$user@$ip_addr" "python2 -m pip install --user Flask bluepy; python2 $dest_folder/app.py"
