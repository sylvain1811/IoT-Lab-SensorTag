import sys, os
from bluepy import btle
from time import sleep

MACAddr20 = "B0:B4:48:C9:B1:05" # 20
MACAddr21 = "B0:B4:48:C9:D3:05" # 21
sensor20 = btle.Peripheral(MACAddr20)
sensor21 = btle.Peripheral(MACAddr21)

# set sensor to remote mode 
sensor21.writeCharacteristic(0x50, bytes("\x01"), withResponse=True)
# activate buzzer
for i in range(10):
    sensor21.writeCharacteristic(0x4e, bytes("\x04"), withResponse=True)
    sleep(0.4)
    sensor21.writeCharacteristic(0x4e, bytes("\x00"), withResponse=True)

# wake up the IR sensor (write the value 1 at handle 0x24) -> GATT
sensor20.writeCharacteristic(0x24, bytes("\x01"), withResponse=True)
sleep(1)  # warm up

# read temperature data from sensor
t_data = sensor20.readCharacteristic(0x21)  # handle 0x21
msb = ord(t_data[1])
lsb = ord(t_data[0])

# formula from TMP007 temperature sensor , explained at http://nessy.info/?p=959
# first part: (msb * (2**8) + lsb)  is to concatenate MSB LSB
# then 2**-2 shifts by 2 to the right (formula given by datasheet of TMP007)
# and finally divide by 32 (also part of the TMP007 temperature formula)
c = round(((msb * (2 ** 8) + lsb) * (2 ** (-2))) / 32, 2)

# display temperature value
print "temperature = " + str(c)

# turn off sensor
sensor20.writeCharacteristic(0x24, bytes("\x00"), withResponse=True)
sensor21.writeCharacteristic(0x24, bytes("\x00"), withResponse=True)
