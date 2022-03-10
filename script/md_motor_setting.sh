#!/bin/bash

# sudo slcand -o -c -s2 /dev/ttyACM0 can0
sudo slcand -o -c -s2 /dev/ttyACM* can0
sleep 5
sudo ifconfig can0 up
sleep 5

cansend can0 00b7b801#11.00.00.00.00.00.00.00
sleep 5
cansend can0 00b7b801#47.01.00.00.00.00.00.00
sleep 5
cansend can0 00b7b801#10.01.00.00.00.00.00.00
sleep 5
cansend can0 00b7b801#12.00.00.00.00.00.00.00
sleep 5
cansend can0 00b7b801#d3.2d.00.00.00.00.00.00
sleep 5
cansend can0 00b7b801#89.aa.04.00.00.00.00.00
sleep 5
cansend can0 00b7b801#9C.00.04.00.00.00.00.00
sleep 5
cansend can0 00b7b801#7B.00.04.00.00.00.00.00
sleep 5
cansend can0 00b7b801#AA.00.04.00.00.00.00.00
sleep 5
cansend can0 00b7b801#15.0A.00.00.00.00.00.00
sleep 5
cansend can0 00b7b801#41.0A.00.00.00.00.00.00
sleep 5

sudo ifconfig can0 down
sudo slcand -o -c -s6 /dev/ttyACM* can0
sleep 5
sudo ifconfig can0 up
sleep 5
