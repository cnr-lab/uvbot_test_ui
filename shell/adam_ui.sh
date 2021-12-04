#!/bin/bash

# sudo slcand -o -c -s2 /dev/ttyACM0 can0
sudo slcand -o -c -s6 /dev/ttyACM* can0
sleep 5
sudo ifconfig can0 up

cd .. && python3 script/main_test.py