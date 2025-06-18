#!/bin/bash

sudo mkdir /usr/local/simplefetch
sudo cp simplefetch.py /usr/local/simplefetch
pip install -r requirements.txt
echo "alias simplefetch='python /usr/local/simplefetch/simplefetch.py'" >> ~/.bashrc
source ~/.bashrc
clear
