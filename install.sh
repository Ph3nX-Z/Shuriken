
apt install python3
apt install python3-pip
pip3 install flask
pip3 install requests
pip install pyinstaller
pyinstaller --onefile ./Shuriken.py
cp ./dist/Shuriken /bin/shuriken
echo "[*] Installed Shuriken"
pyinstaller --onefile ./Katana.py
cp ./dist/Katana /bin/Katana
echo "[*] Installed Katana"
pyinstaller --onefile ./FuzzMe.py
cp ./dist/FuzzMe /bin/FuzzMe
echo "[*] Installed FuzzMe"
echo "[+] Installation Complete !"



