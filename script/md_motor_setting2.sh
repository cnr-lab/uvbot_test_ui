#!/bin/bash

# sudo slcand -o -c -s2 /dev/ttyACM0 can0
sudo slcand -o -c -s6 /dev/ttyACM* can0
sleep 5
sudo ifconfig can0 up
sleep 5

cansend can0 00b7b801#11.00.00.00.00.00.00.00 #통신 제어
sleep 5
cansend can0 00b7b801#18.01.00.00.00.00.00.00 # 모터 브레이크
sleep 5
cansend can0 00b7b801#47.01.00.00.00.00.00.00 # 모터 방향
sleep 5
cansend can0 00b7b801#10.01.00.00.00.00.00.00 # 모터방향 
sleep 5
cansend can0 00b7b801#12.00.00.00.00.00.00.00 # 모터방향
sleep 5
cansend can0 00b7b801#d3.2d.00.00.00.00.00.00 # 최대 전류설
sleep 5
cansend can0 00b7b801#89.aa.04.00.00.00.00.00 # 보레이터 

sudo ifconfig can0 down
sudo slcand -o -c -s6 /dev/ttyACM* can0
sleep 5
sudo ifconfig can0 up
sleep 5
