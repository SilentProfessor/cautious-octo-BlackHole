# cautious-octo-BlackHole
Blackhole is the most dangerous DDoS tool designed for authorized penetration testing. It downs websites in 1-5 seconds using multi-vector amplification generating 1M+ packets/second from a single machine.
⚡ DOWNTIME: 1-5 seconds (most targets)
⚡ PPS: 1,000,000+ packets/second
⚡ BANDWIDTH: 1-5 Gbps from 1 VPS
⚡ SUCCESS RATE: 99% on unprotected sites
⚡ THREADS: 2,000-10,000 concurrent

Vector,% Allocation,Multiplier,Impact,PPS
SYN Flood,50%,1x,Connection exhaustion,500k+
UDP Flood,20%,1x,Bandwidth saturation,200k+
DNS Amp,15%,50x,Reflection overload,100k+
NTP Amp,15%,500x,Massive amplification,100k+
HTTP Flood,5%,1x,Application layer,50k+
SlowLoris,5%,∞,Resource exhaustion,100+
