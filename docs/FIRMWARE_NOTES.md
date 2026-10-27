# BIOS and VBIOS recovery notes — 2026-10-24

## Donor SPI
- Chip marking seen in photos: Winbond `25Q32BVSIG` (W25Q32BV class), 32 Mbit = 4 MiB, nominal 3.3 V SPI NOR.
- Programmer: CH341B-compatible using `flashrom -p ch341a_spi`.
- Programmer was intermittent: one good read followed by failures, then second successful read.
- Owner's terminal confirmed `cmp` success: **both BIOS reads byte-for-byte identical**.
- First BIOS SHA-256: `dc4481d350d069ce7ba050e07b60119cb8478063f041aba66fad4b34579fda82`.
- Dump format identification from earlier extraction: AMI UEFI; build/version string `N55SL.204`. **This does not by itself confirm the physical donor motherboard model.**

## NVIDIA option ROM candidates

| Filename | PCI ID | VBIOS version | Length | SHA-256 |
|---|---|---|---:|---|
| `ASUS_NVIDIA_GF106_10DE-0DCE_v70.06.2D.00.A6.rom` | 10DE:0DCE | 70.06.2D.00.A6 | 65536 B | `8033368516ff6119eca7d993a71d2dd8cd85854233e980a0110a8852759dac91` |
| `ASUS_NVIDIA_GF106B_10DE-1247_v70.26.32.00.07.rom` | 10DE:1247 | 70.26.32.00.07 | 59904 B | `1adebf533e587a4ef53388340271f9a8cbecf01ab77a5ca67b0411afb9eea192` |

Both extracted files have 55 AA ROM signatures, PCIR structs, PCI NVIDIA vendor ID 10DE and a matching byte sum checksum. They were extracted from compressed UEFI content of the uploaded BIOS image. These structural checks **do not demonstrate that either firmware belongs to the physical module**.

### Unknowns
- Precise donor motherboard PCB model/revision.
- GPU's actual enumerated PCI device and subsystem IDs.
- If module firmware is from main BIOS only or other initialization data exists.
- Whether either candidate matches GT 555M board/VRAM configuration.

### Firmware safety
- Keep both original firmware images unchanged and backed up separately.
- Never flash candidate VBIOS into motherboard SPI or an unknown GPU module.
- No flashing is needed for passive connector reverse-engineering.
