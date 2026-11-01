#!/usr/bin/env python3
"""Awesome Budget Residential Proxies Under $1 Dollar Matrix 2026."""
import argparse

PROXIES = {
    "packetstream": {"name": "PacketStream", "rate_per_gb": 1.00, "min_order": 50, "never_expire": True},
    "pawns": {"name": "Pawns.app", "rate_per_gb": 1.20, "min_order": 10, "never_expire": True},
    "nineproxy": {"name": "9Proxy", "rate_per_gb": 0.04, "min_order": 20, "never_expire": True}, # per-IP rate
    "webshare": {"name": "Webshare", "rate_per_gb": 0.80, "min_order": 5, "never_expire": False}
}

def calculate():
    print("=" * 70)
    print("Awesome Budget Residential Proxy Directory 2026 (Under $1.50/GB)")
    print("=" * 70)
    print(f"{'Provider':<15} {'Effective Rate':<18} {'Min Order':<15} {'Expiry Policy'}")
    print("-" * 70)
    for key, data in PROXIES.items():
        print(f"{data['name']:<15} ${data['rate_per_gb']:.2f}/GB{'':<10} ${data['min_order']:.2f}{'':<10} {'Never Expires' if data['never_expire'] else 'Monthly Cycle'}")
    print("=" * 70)

if __name__ == "__main__":
    calculate()
