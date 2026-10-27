# Hardware notes

## GPU module (identifications based on submitted photographs)
- NVIDIA package marking previously observed: `N12E-GE2-A1`.
- PCB silkscreen previously observed: `MGM_N12E_2P`, revision `2.1`.
- ASUS proprietary/removable graphics module: **not assumed to be electrically standard MXM**.
- Eight Samsung memory chip locations were identified across both faces; markings on readable devices reported `K4W2G1646C-HC11`. 2 GiB total is consistent with 8 × 2 Gbit chips **if all eight match**.
- Identified/likely board power ICs include NCP3218 and APL5930 (chip markings pictured earlier), but exact rail functions and pin mapping are not yet traced.
- Module has original local GPU voltage regulator circuitry. **Do not assume its connector takes laptop adapter voltage or desktop PCIe 12 V.**

## Donor laptop motherboard
- Onboard 4 MiB Winbond W25Q32BV-class SPI flash successfully read.
- Firmware reports `N55SL.204`. Physical board identification is pending.
- Motherboard reportedly non-booting. The intact donor GPU socket and PCB traces remain valuable for pinout recovery.

## Required measurements before PCB design
- Physical contact count; keyed/notched side; pin-1 reference based on actual socket datasheet if identifiable.
- GND contacts by multimeter continuity to ground plane.
- Supply nets traced back to inductors/caps/FETs and measured only under an appropriate safe test plan.
- PCIe differential-pair routing from socket to chipset via schematic/boardview plus board inspection.
- PCIe REFCLK, PERST#, CLKREQ#, power enables / power-good, SMBus/DDC as applicable.
- Determine which display outputs are wired via the main board, if needed for a display-capable adapter.
- Cooling and thermal protection for the module.

Do not rely on internet schematics for a nearby model if the PCB silkscreen and connector revisions do not match.
