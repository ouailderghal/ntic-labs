#!/bin/bash
#
# Download packages for laboratory machines  
#
# Author : Ouail Derghal <ouail.derghal@univ-constantine2.dz>
# GitLab : https://gitlab.com/ouailderghal1
#
# The following list of packages will be downloaded :
#   - Eclipse for Java Developers
#   - Microsoft Visual Studio Code
#   - Cisco Packet Tracer
# 
# Make sure that you point the WORKDIR variable to the path of the project on your machine.
# If you are having any trouble when downloading packages, update URL constants to active and working links.
# Downloaded packages can be found in your project folder, under packages directory.
# 

WORKDIR=$HOME/Projects/lmc
DOWNLOAD_DIR=$WORKDIR/packages

ECLIPSE_URL="https://ftp.osuosl.org/pub/eclipse/technology/epp/downloads/release/2022-06/R/eclipse-java-2022-06-R-linux-gtk-x86_64.tar.gz"
ECLIPSE_FILENAME="$WORKDIR/roles/java_lab/files/eclipse.tar.gz"

VSCODE_URL="https://az764295.vo.msecnd.net/stable/da76f93349a72022ca4670c1b84860304616aaa2/code_1.70.0-1659589288_amd64.deb"
VSCODE_FILENAME="$WORKDIR/roles/web_lab/files/vscode.deb"

PACKETTRACER_URL="https://ia802208.us.archive.org/20/items/pt81_20220222/CiscoPacketTracer_811_Ubuntu_64bit.deb"
PACKETTRACER_FILENAME="$WORKDIR/roles/networking_lab/files/packettracer.deb"

# Download Eclipse for Java Developers
[ ! -f $ECLIPSE_FILENAME ] && curl $ECLIPSE_URL -o $ECLIPSE_FILENAME || \
    echo "[INFO] Eclipse for Java Developers has already been downloaded."

# Download Microsoft Visual Studio Code
[ ! -f $VSCODE_FILENAME ] && curl $VSCODE_URL -o $VSCODE_FILENAME || \
    echo "[INFO] Visual Studio Code has already been downloaded."

# Download Cisco Packet Tracer
[ ! -f $PACKETTRACER_FILENAME ] && curl $PACKETTRACER_URL -o $PACKETTRACER_FILENAME || \
    echo "[INFO] Cisco Packet Tracer has already been downloaded."

