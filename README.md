# deb_attack
Binding payloads in any deb package 
usage: deb_auto.py [-h] [-v] [-d deb package name] [-p payload_file_name]

This tool building deb Auto Package Builder and give only payload (python
bash)

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -d deb package name, --deb deb package name
                        debian Package path to inject malicious payload
  -p payload_file_name, --payload payload_file_name
                        give me metasploit generated payload path to inject
                        package in payload

python3 deb_auto.py -d example.deb -p payload_file_path_name
