MESAJ="Alpha String"
MESAJ+="\nTelegram: @AlphaResmi"
pkg upgrade
clear
echo -e $MESAJ
echo "Python yüklənir..."
pkg install python -y
clear
echo -e $MESAJ
echo "TeleThon yüklənir..."
pip install telethon
echo "Requests/BS4 yüklənir..."
pip install requests
pip install bs4
clear
echo -e $MESAJ
echo "Fayl yazılır..."
curl "https://raw.githubusercontent.com/Goqerti/AlphaUserBot/main/alpha.py" --output "alpha.py"
clear
echo -e $MESAJ
echo "Qurulum Bitdi! İndi String Ala Bilərsiz."
clear
python alpha.py
