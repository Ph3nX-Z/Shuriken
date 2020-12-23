
FILE="/etc/shadow"

if ! [[ $(stat -c "%A" $FILE) =~ "r" ]]; then
  apt install python3
  apt install python3-pip
  pip3 install requests
  cp ./Shuriken.py /bin/shuriken
else 
  echo '[-] Run The Script As Root'

fi

exit 0






