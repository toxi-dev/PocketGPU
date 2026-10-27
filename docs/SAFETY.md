# PocketGPU board-handling and electrical safety

- Remove AC adapter, laptop/main battery and any removable CMOS/backup battery before continuity testing or desoldering.
- Do not hot-plug the SPI chip while the CH341 programmer has USB power.
- Verify both flash **VCC and signal voltage**, not just adapter silkscreen labels. The W25Q32BV is nominally a 3.3 V SPI device; some CH341 programmer variants have unsafe signal levels.
- Do not desolder the GPU connector until its orientation and accessible PCB traces are fully documented.
- Do not guess connector supply voltage. No 12 V, 19 V, 3.3 V or 5 V rail is proven by a picture.
- Avoid probing powered fine-pitch contacts with loose multimeter tips; use stable breakout points, insulated probes and current-limited power sources after identifying safe rails.
- Never inject power until the rail map, expected sequencing, and short-circuit checks are established.
- Use proper ESD handling and heatsink/fan for later powered GPU tests.
- Back up the original SPI firmware; no writing/flashing required in this phase.
