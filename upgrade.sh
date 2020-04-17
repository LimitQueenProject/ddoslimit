#!\usr\bin\bash
cd ..
pkg update && pkg upgrade
pkg install git
rm -rf ddoslimit
git clone https://github.com/LimitQueenProject/ddoslimit

echo "\33[36;1mupgrade selesai"
