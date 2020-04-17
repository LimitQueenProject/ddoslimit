#!\usr\bin\bash

pkg update && pkg upgrade
pkg install python
pkg install python2
pkg install git
pkg install bash
pkg install curl
pkg install apache2
pkg install openssh
pkg install python-pip
pip2 install requests
pip2 install mechanize
pip2 install bs4
pip install requests
pip install mechanize
pip install bs4

echo "done"
