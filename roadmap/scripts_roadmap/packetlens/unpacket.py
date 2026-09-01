import dpkt
from time import sleep
import socket

def desempacotar(dados_lido):
    for timestamp, buf in dados_lido:
        eth = dpkt.ethernet.Ethernet(buf)
        if not isinstance(eth.data, dpkt.ip.IP):
            continue

        ip = eth.data
        #print(f"o IP e: {ip}")
        print("_" * 30) 
        if isinstance(ip.data, dpkt.tcp.TCP):
            mac_src = ":".join(f"{b:02x}" for b in eth.src)
            mac_dst = ":".join(f"{b:02x}" for b in eth.dst)

            tcp = ip.data
            ip_src = socket.inet_ntoa(ip.src)
            ip_dst = socket.inet_ntoa(ip.dst) 
            print(f"""
            o ethernet e: src={mac_src} dst={mac_dst} type={eth.type}
            o ip e: src={ip_src} dst={ip_dst} protocolo={ip.p} ttl={ip.ttl}
            tcp e: porta e {tcp.sport} para {tcp.dport} sua flasg e {tcp.flags}   
            """)
            
