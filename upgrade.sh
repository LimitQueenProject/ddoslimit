#!\usr\bin\bash
cd ..
pkg update && pkg upgrade
pkg install git
rm -rf ddoslimit
git clone https://github.com/LimitQueenProject/ddoslimit
echo ""
echo ""
echo "ketik cd"
echo ""
