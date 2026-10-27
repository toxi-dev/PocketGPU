# Hardware and source research

## Physical hardware

- Donor system: ASUS N55SL; motherboard marking: **60-N10MB1300**.
- Graphics daughterboard: **MGM_N12E_2P REV 2.1**.
- GPU package marking: **NVIDIA N12E-GE2-A1**.
- Motherboard slot silkscreen: **MXM CON1**; proprietary MXM-style socket.
- Test equipment: UNI-T UT39C multimeter, CH341A SPI programmer.

## ASUS N55SL Repair Guide (December 8, 2011)

- **Page 1:** block diagram labels an **MGM Nvidia N12E-GE** module connected to Sandy Bridge CPU over **PCIe x16**.
- **Page 2:** motherboard system power-flow diagram; illustrates multiple switched/regulated supplies.
- **Page 3:** power-on sequence involving system rails and power-good signals.
- **Page 5:** board map labels **MXM CON1**.

This repair guide is not a full schematic, boardview, or pinout and does not establish the pin numbering or individual power contacts of the proprietary connector. Differences between actual board revisions are possible. The copyrighted PDF is kept out of this repository.

## Firmware

- The original motherboard SPI flash was read twice with CH341A, producing matching dumps.
- BIOS string observed: **N55SL.204**.
- Two NVIDIA option ROM candidates were found with PCI IDs **10DE:0DCE** and **10DE:1247**; neither is verified as the correct VBIOS for the physical module.
- Proprietary firmware dumps are not distributed here.
