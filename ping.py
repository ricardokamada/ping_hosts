
# -*- coding: utf-8 -*-

import subprocess
import os
import time
from colorama import init, Fore
import datetime 
# Inicializa o colorama
init()

#Dicionário de IPs e hosts
ips_hosts = {
    "172.16.0.220" : "SBS",
    "172.16.0.201" : "AD_201",
    "172.16.0.202" : "AD_202",
    "172.16.0.239" : "BENNER",
    "172.16.2.126" : "JHON",
    "172.16.1.113" : "LIMA",
    "CPD-ANA" : "ANA",
    "172.16.6.27" : "BLOCO F - ANIMAIS"
}

while True:
    for ip, host in ips_hosts.items():
        try:
            result = subprocess.run(["ping", "-n", "1", "-w", "1000", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            #print(result.stdout)
            if "Resposta" in result.stdout: # se a palavra "Resposta" estiver na saída do ping, então o host está ativo
                print(f"{host} ({ip}) {Fore.GREEN}ESTA ATIVO {Fore.RESET}", datetime.datetime.now().strftime("%d-%m-%Y (%H:%M:%S)" ))
            else:
                print(f"{host} ({ip}) {Fore.RED} ESTA INATIVO{Fore.RESET}")
        except Exception as e:
            print(f"Erro: {e}")
                

    time.sleep(2)
    print(' --------- wait ---------')
    
    
