# Simplefetch _(1.1)_ [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Language: Python](https://img.shields.io/badge/Language-Python-yellow.svg)](https://www.python.org/)

Simplefetch — is a utility for providing the user with all the information about the system. This project was inspired by [neofetch](https://github.com/dylanaraps/neofetch). 

If you find any bugs in the project then create an issue in this repository!

# Installation and deletion

Installing the necessary packages:

**Debian/Ubuntu**
```shell
sudo apt-get install python3 python3-pip mesa-utils
```

**Fedora**
```shell
sudo dnf install python3 python3-pip glx-utils
```

**Arch Linux**
```shell
sudo pacman -S python3 python3-pip mesa-utils
```

**OpenSUSE**
```shell
sudo zypper addrepo -cfp 90 'https://ftp.gwdg.de/pub/linux/misc/packman/suse/openSUSE_Tumbleweed/' packman
sudo zypper refresh
sudo zypper dup --from packman --allow-vendor-change
sudo zypper install python3 python3-pip mesa-utils
```

---

To install Simplefetch itself, you need to enter the following commands:
```shell
git clone https://github.com/nonetype-123/simplefetch/
cd simplefetch
chmod +x setup.sh
./setup.sh # --uninstall for deletion
```

# ! IMPORTANT !

Works only with bash. Zsh and other shells do not work. This problem will be fixed in the future!
