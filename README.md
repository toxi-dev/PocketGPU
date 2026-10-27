#PocketGPU

### Giving an old NVIDIA laptop GPU a second life.

**ToxiTech PocketGPU** is an experimental open-hardware project exploring whether a proprietary ASUS laptop graphics module can be repurposed as a standalone PCIe graphics card.

The project involves reverse-engineering the original motherboard, identifying the GPU connector pinout, studying power distribution, recovering firmware information, and designing a custom PCB adapter.

> **Project status:** Early research and hardware reverse-engineering. No functional external GPU adapter has been completed.

## Hardware

| Component | Details |
|---|---|
| Donor laptop | ASUS N55SL |
| Graphics module | MGM_N12E_2P REV 2.1 |
| GPU | NVIDIA N12E-GE2-A1 |
| Interface | PCI Express x16, according to ASUS documentation |
| Connector | Proprietary ASUS MXM-style module connector |
| Donor motherboard | ASUS 60-N10MB1300 |
| PCB design software | KiCad |
| Measurement tools | Digital multimeter, CH341A SPI programmer |

## Project Goals

- Reverse-engineer the graphics module connector.
- Identify power, ground, PCIe, and control signals.
- Understand the GPU's power requirements.
- Investigate the original firmware and initialization requirements.
- Design a custom adapter PCB.
- Develop and validate a safe power-delivery solution.
- Attempt to initialize the GPU using a standard PCIe host.

## Reverse Engineering Progress

### Connector mapping

The current pin labels are provisional reference identifiers created for this project. They are **not official ASUS or MXM pin numbers**.

| Reference pads | Current findings |
|---|---|
| A01–D01 | Continuity to Power Net A |
| A02–D02 | Continuity to Power Net A |
| A03–D03 | No continuity detected to tested power net or ground |
| A04–D04 | No continuity detected to tested power net or ground |
| A05–D05 | Ground |
| A06–D06 | Ground |
| G01–G08 | Ground |

### Power research

Continuity testing indicates that several motherboard capacitors and eight connector reference pads share a common electrical network.

The network has provisionally been named `POWER_NET_A`.

**The operating voltage is not yet known.**

The original laptop motherboard also contains separate battery-associated circuitry.

### Firmware research

Two matching motherboard BIOS dumps have been obtained using a CH341A SPI programmer.

NVIDIA option ROM candidates have been identified for further investigation.

Proprietary firmware dumps are not distributed in this repository.

## Documentation

The project documents measurements, component identification, circuit tracing, reference photographs, and PCB design progress.

All electrical findings should distinguish between:

- Measured and confirmed connections.
- Preliminary observations.
- Hypotheses requiring additional testing.
- Unknown or unverified connections.

## Safety

This is an experimental hardware project.

**Do not apply power to the graphics module based on the preliminary connector map.**

Incorrect supply voltages, missing power sequencing, or incorrect connector wiring could permanently damage the graphics module, motherboard, or connected host.

PCB files created during early research are conceptual and must not be treated as manufacturing-ready.

## Roadmap

- [x] Identify the donor graphics module.
- [x] Recover the motherboard BIOS.
- [x] Locate the original GPU connector.
- [x] Begin mapping connector ground connections.
- [x] Identify a candidate power network.
- [ ] Confirm all power rails and operating voltages.
- [ ] Determine the official connector contact mapping.
- [ ] Identify PCIe lanes and reference clock.
- [ ] Identify reset and other control signals.
- [ ] Investigate firmware initialization.
- [ ] Complete an electrically verified KiCad schematic.
- [ ] Design and review the adapter PCB.
- [ ] Prototype and test the hardware.

## Credits

Created by **ToxiTech**.

GitHub: [@toxi-dev](https://github.com/toxi-dev)

---

**ToxiTech PocketGPU — Reusing hardware, one connection at a time.**
