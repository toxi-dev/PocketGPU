#!/usr/bin/env python3
"""Read-only integrity check for ToxiTech PocketGPU firmware files."""
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parent.parent
FW = ROOT / 'firmware'
VBIOS = FW / 'vbios'
EXPECTED_BIOS = 'dc4481d350d069ce7ba050e07b60119cb8478063f041aba66fad4b34579fda82'
ROM_SPECS = [
    ('ASUS_NVIDIA_GF106_10DE-0DCE_v70.06.2D.00.A6.rom', 0x0DCE, 65536,
     '8033368516ff6119eca7d993a71d2dd8cd85854233e980a0110a8852759dac91'),
    ('ASUS_NVIDIA_GF106B_10DE-1247_v70.26.32.00.07.rom', 0x1247, 59904,
     '1adebf533e587a4ef53388340271f9a8cbecf01ab77a5ca67b0411afb9eea192'),
]

def sha256(b): return hashlib.sha256(b).hexdigest()

errors = 0
first = second = None
for name in ('asus_bios_1.bin','asus_bios_2.bin'):
    p = FW / name
    if not p.is_file():
        print(f'[MISSING] {p}'); errors += 1; continue
    b = p.read_bytes()
    print(f'[BIOS] {name}: {len(b)} bytes, SHA256={sha256(b)}')
    if len(b) != 4194304 or sha256(b) != EXPECTED_BIOS:
        print('  [FAIL] Different from original 4MiB firmware read'); errors += 1
    if name.endswith('_1.bin'): first=b
    else: second=b
if first is not None and second is not None:
    if first==second: print('[OK] Both BIOS reads are byte-for-byte identical')
    else: print('[FAIL] BIOS reads differ'); errors += 1

for fname, device, expected_size, expected_sha in ROM_SPECS:
    p=VBIOS/fname
    if not p.is_file(): print(f'[MISSING] {p}'); errors+=1; continue
    b=p.read_bytes()
    issues=[]
    if len(b)!=expected_size: issues.append('size mismatch')
    if sha256(b)!=expected_sha: issues.append('SHA-256 mismatch')
    if len(b)<0x1c or b[:2]!=bytes.fromhex('55aa'): issues.append('missing 55 AA signature')
    else:
        pcir=int.from_bytes(b[0x18:0x1a], 'little')
        if pcir+8>len(b) or b[pcir:pcir+4]!=b'PCIR': issues.append('invalid PCIR')
        else:
            vendor=int.from_bytes(b[pcir+4:pcir+6], 'little')
            devid=int.from_bytes(b[pcir+6:pcir+8], 'little')
            if (vendor,devid)!=(0x10de,device): issues.append('PCI vendor/device mismatch')
    if sum(b)%256: issues.append('ROM checksum mismatch')
    print(f'[ROM] {fname}: ' + ('[OK]' if not issues else '[FAIL] ' + ', '.join(issues)))
    errors+=bool(issues)
print('\nReminder: structure/hash validation does NOT prove GPU compatibility, and no writes were performed.')
sys.exit(1 if errors else 0)
