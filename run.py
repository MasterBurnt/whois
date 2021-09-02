#!/bin/python3
#MasterBurnt 
#t.me/TheBurnt
import socket
import os

#Colors
c1 = '\033[0m'  #white
c2 = '\033[92m' #green
c3 = '\033[96m' #cyan
c4 = '\033[91m' #red
c5 = '\033[93m' #yellow 
c6 = '\033[94m' #blue
os.system('clear')
def banner():
    print(f"""
        
        {c1} _ _ _  _
        {c2}| | | || |_  ___
        {c3}| | | ||   || . |
        {c4}|_____||_|_||___| 
{c6}             ???????
           {c5}??:::::::??
         {c1}??:::::::::::? {c6}  iiii
        {c3}?:::::????:::::?{c1} i::::i
        {c2}?::::?    ?::::? {c3} iiii
        {c4}?::::?     ?::::?            
        {c6}??????     ?::::?{c4}iiiiiii     ssssssssss
                  {c5}?::::? {c2}i:::::i   ss::::::::::s
                 {c1}?::::?   {c6}i::::i ss:::::::::::::s
                {c2}?::::?    {c3}i::::i s::::::ssss:::::s
               {c4}?::::?     {c4}i::::i  s:::::s  ssssss
              {c1}?::::?      {c2}i::::i    s::::::s
              {c5}?::::?      {c6}i::::i       s::::::s
              {c2}??::??      {c5}i::::i ssssss   s:::::s
               {c6}????      {c1}i::::::is:::::ssss::::::s
                         {c3}i::::::is::::::::::::::s
               {c2}???       {c2}i::::::i s:::::::::::ss
              {c1}??:??      {c5}iiiiiiii  sssssssssss
               {c6}???       {c4}Mᵃˢᵗᵉʳ Bᵘʳⁿᵗ 
        
""")  
banner()
#Final Output
out = str()

#Domain Name
domain = input(c6+f"[+] {c2}Enter Domain Address {c1}[{c5}Google.com{c1}] : {c3}").lower().replace("http://","").replace("https://","").replace("www.","")

#Partial check of domain correctness
domain_find = domain.find('.')
if domain_find == -1 or domain == '' or domain == '127.0.0.1':
    print(c4+f'[-] {c2}Please enter the{c4} domain address {c2}correctly!')
    exit(0)
    
#Guided    
elif domain[-3:] in ["com", "net", "org"]:
    whois_server = "whois.internic.net" 
else:
    whois_server =  "whois.iana.org"
    
#Connect
try :
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((whois_server,43))
    s.send((domain+"\r\n").encode())
except socket.error:
    print(c4+f'[-]{c2} Check your{c4} connection{c2} to the{c4} Internet')
    exit(1)
#Filter & Show
msg = s.recv(1000000)
msg = msg.decode()
if domain[-3:] == "org" or domain[-3:] == "com" or domain[-3:] == "net":
    out = msg[:-2263]
else:
    out = msg[136:-181]
if out == "":
    print(c4+f"[Warning] :{c1} Failed! Check that the domain address is correct\nAlso Check your connection to the Internet!  ")
    exit(0)
else:
    print(c1+out) 
    #Build History Folder
    try:
        os.mkdir('history')
    except:
        pass
    #Save
    os.chdir('history')
    file = open(domain[0:domain_find]+".txt", "wt")
    file.write(out)
    file.write("\n\n\t  Developer : MasterBurnt\n\n\t ContactMe : t.me/TheBurnt")
    file.close()


