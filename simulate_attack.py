import requests
import time
import random
import sys

BASE_URL = "http://localhost:8000/api/simulate"

def simulate_port_scan():
    print("[*] Simulating Port Scan...")
    for i in range(6):
        payload = {
            "type": "port_scan",
            "src_ip": "192.168.1.100",
            "dst_port": 80 + i
        }
        requests.post(BASE_URL, json=payload)
        time.sleep(0.1)
    print("    -> Sent 6 port scan events")

def simulate_brute_force():
    print("[*] Simulating Brute Force Attack...")
    payload = {
        "type": "failed_login",
        "user": "admin"
    }
    # Send 4 failed logins to trigger brute force alert (threshold is 3)
    for _ in range(4):
        requests.post(BASE_URL, json=payload)
        time.sleep(0.5)
    print("    -> Sent 4 failed login events")

def simulate_suspicious_process():
    print("[*] Simulating Suspicious Process (High CPU)...")
    payload = {
        "type": "high_cpu_process",
        "pid": random.randint(1000, 9999),
        "name": "crypto_miner.exe",
        "cpu_percent": 95.5
    }
    requests.post(BASE_URL, json=payload)
    print("    -> Sent suspicious process event")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python simulate_attack.py [port_scan|brute_force|suspicious_process|all]")
        sys.exit(1)

    attack = sys.argv[1]
    
    if attack == "port_scan":
        simulate_port_scan()
    elif attack == "brute_force":
        simulate_brute_force()
    elif attack == "suspicious_process":
        simulate_suspicious_process()
    elif attack == "all":
        simulate_port_scan()
        time.sleep(2)
        simulate_brute_force()
        time.sleep(2)
        simulate_suspicious_process()
    else:
        print("Invalid attack type.")
