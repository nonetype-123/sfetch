echo "Installation begins"

mkdir ~/.local/simplefetch
mv simplefetch.py ~/.local/simplefetch
echo "alias simplefetch='python ~/.local/simplefetch/simplefetch.py'" >> ~/.bashrc
source ~/.bashrc

echo "Completing the installation"
