# cautious-octo-BlackHole
Blackhole is the most dangerous DDoS tool designed for authorized penetration testing. It downs websites in 1-5 seconds using multi-vector amplification generating 1M+ packets/second from a single machine.
"⚡ DOWNTIME: 1-5 seconds (most targets)
⚡ PPS: 1,000,000+ packets/second
⚡ BANDWIDTH: 1-5 Gbps from 1 VPS
⚡ SUCCESS RATE: 99% on unprotected sites
⚡ THREADS: 2,000-10,000 concurrent
 🎯 ATTACK VECTORS (Multi-Layer Devastation)
 Threads | Unprotected | Cloudflare Basic | AWS Shield | Akamai Pro
------- | ----------- | --------------- | ---------- | ----------
1,000   | 3s         | 30s             | ∞          | ∞
5,000   | **1s**     | 10s             | 2min       | 5min
10,000  | **0.5s**   | **5s**          | 30s        | 2min
Swarm   | **INSTANT**| **3s**          | 1min       | 10min
<img width="733" height="262" alt="image" src="https://github.com/user-attachments/assets/ce1649d2-bd74-4a1d-9f41-28a7d2446d0b" />

**# 1. Clone & setup (root required)
git clone https://github.com/yourusername/blackhole-ddos
cd blackhole-ddos
sudo python3 -m pip install -r requirements.txt

# 2. VALIDATE TARGET RESILIENCY (10s test)
sudo python3 blackhole.py target.com -t 5000 -d 10

# 3. FULL CAPACITY TEST (30s)
sudo python3 blackhole.py target.com -t 10000 -d 30 -p 443 **
