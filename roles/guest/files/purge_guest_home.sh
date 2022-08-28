#!/bin/bash
# 
# Purge guest HOME directory and copy default XFCE configuration files
#

rm -rf /home/guest/*
rm -rf /home/guest/Desktop
rm -rf /home/guest/.config
rm -Rf /home/guest/.*
mkdir -p /home/guest/.config/
cp -r /opt/xfce4 /home/guest/.config/
cp -r /opt/autostart /home/guest/.config/
chown -R guest:guest /home/guest/.config
