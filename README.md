This is a Python based program that displays quotes  on the screen after system-boot. It works only on Linux system and contribution to ext5end it to other systems is welcome.

GUIDE TO INSTALLATION
1. The  main program runs on quotes.py, install the necessary programs based on the imports

2. change the file path in quotes.py to point to the json file having your quotes or to the location of projectFiles.json

Alternatively, you can use the quoteTransfer.py program to transfer your quotes from your text editor to json file

3. Make the program run automatically on system boot. Use terminal to run these commands
    sudo mkdir -p ~/.config/autostart
    cd ~/.config/autostart
    sudo nano quote.desktop #copy the lines of quote.desktop and paste them here
    chmod +x quote.desktop  #make the file executable
    sudo gtk-launch quote   #test it if it works


for more contributions and collaboration
https://x.com/Sour_truths on X
www.linkedin.com/in/charsimon on Linkedin