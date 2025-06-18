#!/bin/bash

INSTALL_DIR="/usr/local/simplefetch"
BIN_LINK="/usr/local/bin/simplefetch"
RC_ENTRY="alias simplefetch='python3 ${INSTALL_DIR}/simplefetch.py'"

if [ "$1" == "--uninstall" ]; then
    echo "Deleting Simplefetch..."
    sudo rm -rf "$INSTALL_DIR"
    sudo rm -f "$BIN_LINK"
    sed -i '/alias simplefetch=/d' ~/.bashrc
    echo "Done!"
    exit 0
fi

echo "Installing Simplefetch..."

sudo mkdir -p "$INSTALL_DIR"

sudo cp simplefetch.py "$INSTALL_DIR/"
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
fi

sudo ln -sf "${INSTALL_DIR}/simplefetch.py" "$BIN_LINK"

if ! grep -q "$RC_ENTRY" ~/.bashrc; then
    echo "$RC_ENTRY" >> ~/.bashrc
fi

source ~/.bashrc
echo "Done!"
