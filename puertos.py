import nmap
import csv

#toma el rango de los puertos
#que seran escaneados

def nmap_funcion(target, begin, end): 
    scanner = nmap.PortScanner()
    for i in range(begin, end+1):
        #Empieza el scaneo de puertos
        res = scanner.scan(target,str(i))
        for host in scanner.all_hosts():
            print('Host : %s (%s)' % (host, scanner[host].hostname()))
            print('State : %s' % scanner[host].state())
            for proto in scanner[host].all_protocols():
                print('Protocol : %s' % proto)

                lport = scanner[host][proto].keys()
                for port in lport:
                    print ('port : %s\tstate : %s' % (port, scanner[host][proto][port]['state']))              
                    if scanner[host][proto][port]['state'] == 'open':
                        port=open('puertos.csv', 'a')
                        porti=scanner.csv()
                        for i in porti:       
                            port.write(i)
                        port.close()
                    
                
                


    

             
             
            
        