import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\\033[1;97m [\x1b[38;5;48m❦\033[1;97m] \x1b[38;5;48mJoin Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/GIE74ZSkmv9AVxSxtYZbCb')
danmo=platform.architecture()[0]
if danmo=="32bit":
    os.system('clear')
    print('\033[1;97m [\x1b[38;5;48m❦\033[1;97m]\x1b[38;5;196mBit Device Not Working')
elif danmo=="64bit":
    __import__("danmo")
