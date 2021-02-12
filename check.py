import bs4
import requests
import smtplib
import ctypes  # An included library with Python install.   
from sty import fg, bg, ef, rs
import threading


interval = 300

def check_price():
    # Download page
    getPage = requests.get('https://www.emag.bg/video-karti/vendor/emag/sort-pricedesc/c')
    getPage.raise_for_status() #if error it will stop the program

    # Parse text for foods
    menu = bs4.BeautifulSoup(getPage.text, 'html.parser')
    cards = menu.select('.product-title')

    the_one = '3060'
    the_other_one = '3070'
    # the_one = '1050 ti'
    flength = len(the_one)
    available = False

    for card in cards:
        for i in range(len(card.text)):
            chunk = card.text[i:i+flength].lower()
            if chunk == the_one or chunk == the_other_one:
                available = True
                    

    # ------------------- E-mail list ------------------------
    toAddress = ['example1@email.com','example2@email.com']
    # --------------------------------------------------------   
        
    if available == True:
    #     conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
    #     conn.ehlo() # call this to start the connection
    #     conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
    #     conn.login('youremail@gmail.com', 'appkey')
    #     conn.sendmail('youremail@gmail.com', toAddress, 'Subject: Borzaska Alert!\n\nAttention!\n\nYour favourite food is available today!\n\nBon apetite!:\nFood Notifier V1.0')
    #     conn.quit()
    #     print('Sent notificaton e-mails for the following recipients:\n')
    #     for i in range(len(toAddress)):
    #         print(toAddress[i])
    
        print('CARD AVAILABLE!!!')
        ctypes.windll.user32.MessageBoxW(0, "CARD AVAILABLE!!!", "Video Card Checker", 1)
    else:        
        print('Card' + fg.red + ' NOT ' + fg.rs + 'available')
        

    #print to console e-mail addresses where the alert was sent.       

def start_check():
    threading.Timer(interval, start_check).start()
    check_price()
    
start_check()