
apt install python3
apt install python3-pip
pip3 install requests
pip install pyinstaller
pyinstaller --onefile ./Shuriken.py
cp ./dist/Shuriken /bin/shuriken
pyinstaller --onefile ./Katana.py
cp ./dist/Katana /bin/Katana
echo "[+] Installation Complete !"



