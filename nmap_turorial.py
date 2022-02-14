from matplotlib.pyplot import sca
import nmap
import sys

target=str(sys.argv[1])

ports=[21,22,80,139,443,8080]
scan_=nmap.PortScanner()

print('-'*25)
print(f'Scanning to {target} for {ports}')
print('-'*25)

for i in ports:
    portscan=scan_.scan(target,str(i))
    print("Port",i ,'is ',portscan['scan'][list(portscan['scan'])[0]]['status']['state'])
