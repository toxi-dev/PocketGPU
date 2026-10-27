# ToxiTech PocketGPU — Phase 2: GPU connector reverse engineering
Updated 2026-10-24

## Current physical hardware observations
- Removable GPU PCB: `MGM_N12E_2P`, revision `2.1` (as observed from user photographs).
- GPU package: `N12E-GE2-A1`; eight graphics-memory packages appear to be fitted, Samsung DDR3 markings visible on some.
- Donor motherboard BIOS: Winbond W25Q32BV family, 4 MiB, independently read twice via CH341 and byte-for-byte compared (`cmp` success shown by owner).
- Firmware build string seen in image: `N55SL.204`. This is evidence of the firmware build, NOT definitive physical identification of the donor board.
- NVIDIA option ROM candidates extracted and checksum validated:
  * 10DE:0DCE / 70.06.2D.00.A6 / 65,536 bytes (NVIDIA legacy driver lists this device as GeForce GT 555M).
  * 10DE:1247 / 70.26.32.00.07 / 59,904 bytes (NVIDIA lists generic 1247 as GT 555M; certain ASUS 1043 subsystem IDs as GT 635M).
- Do NOT flash either VBIOS or assume a candidate is the correct actual device until module hardware/subsystem ID is established.

## Documentation leads (NOT yet checked against donor PCB)
1. EXACT graphics-module boardview listing: `MGM_N12E_2P_2.1.fz` (36.1 KB, access may require registration)
   https://vinafix.com/threads/mgm-n12e-2p.20611/post-31940
2. ASUS N55SF Rev 2.1 motherboard boardview listing (download access requires sign-in)
   https://eletronicabr.com/en/files/file/30711-boardview-asus-n55sf-rev-rev-21-schematic/
3. ASUS N55SL repair guide listing (power-flow, startup-sequence and test-point material; not necessarily connector full schematic)
   https://www.electronica-pt.com/esquema/notebooks/asus/asus-n55sl-20111208-86630/
4. ASUS N55SL official firmware page: BIOS 204 listed
   https://www.asus.com/uk/supportonly/n55sl/helpdesk_bios/
5. NVIDIA GPU PCI ID tables
   https://download.nvidia.com/XFree86/Linux-x86_64/387.12/README/supportedchips.html
6. OpenBoardView, a potential viewer for .fz files:
   https://github.com/OpenBoardView/OpenBoardView
   Caveat: Some ASUS .fz boardviews require an external decryption key. Do not assume the viewer will open the file directly.

## Next actions — DO NOT DESOLDER SOCKET
1. Photograph motherboard top and bottom, particularly original GPU socket and nearby power components; also photograph exact PCB revision marking.
2. Photograph both edges of module to establish contact arrangement, notch/physical orientation and contact count. Photograph socket part numbers if visible.
3. With motherboard fully disconnected from ALL power sources (adapter, main battery, CMOS battery), use continuity mode to map **ground contacts only**. Avoid electrical measurements on live/energized board until rails identified.
4. Populate `connector/pinout_template.csv` with each contact ID, photograph reference, and confidence. Never assign connector pin numbers arbitrarily; use physical numbering validated against datasheet/boardview.
5. Cross-check both GPU module and matching donor motherboard boardview/schematic before routing PCIe, refclock, reset, enable, and power rails.

## Critical hardware unknowns
- Actual motherBOARD silkscreen/revision and GPU slot pin count / mating connector part number.
- All GPU board connector power rails, maximum load and sequencing.
- PCIe lane count, differential-pair mapping, 100 MHz clock, PERST#, any control/SMBus lines.
- Whether GPU can enumerate with generic host firmware absent OEM ACPI power control.
- Appropriate thermal interface/cooling during first test.

## Safety
No 12V / 19V or other external voltage to UNKNOWN contacts. No external power before verifying pinout and ground continuity. Preserve donor slot and donor firmware dump. Avoid connecting voltage across multimeter continuity setting.
