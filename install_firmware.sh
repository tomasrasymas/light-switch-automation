#!/usr/bin/env bash

# install necessary libraries for flashing MicroPython firmware into ESP32
pip install esptool --upgrade
pip install adafruit-ampy --upgrade

# get MicroPython firmware path and serial port of ESP32 board
echo "Path to MicroPython firmware:"
read -e micropython_firmware_path

echo "Port of ESP32 board connected:"
read -e board_port

if [ "$board_port" == '' ]
then
    echo "Using default port /dev/tty.usbserial-0001"
    board_port="/dev/tty.usbserial-0001"
fi

# erase flash and install MicroPython firmware
esptool.py --port $board_port erase_flash
esptool.py --port $board_port --chip esp32 write_flash -z 0x1000 $micropython_firmware_path

echo "Copying light switch firmware to ESP32 board"
ampy --port $board_port put firmware /

echo "All done"
