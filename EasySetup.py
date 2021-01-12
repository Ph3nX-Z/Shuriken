import os

os.system('chmod +x install.sh')

os.system('chmod +x uninstall.sh')

var = input('Install or uninstall (I/U) :').upper() 
if var == "I":
	os.system("sudo bash install.sh")
elif var == "U":
	os.system("sudo bash uninstall.sh")
	print("[+] Uninstallation done !")
else:
	print('Not a valid option')
