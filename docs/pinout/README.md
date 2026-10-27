# Provisional ASUS N55SL graphics connector map

> **NOT A MANUFACTURING PINOUT.** These labels refer to a user-annotated photographic reference for visible solder-side test positions. They are **not** official MXM connector contact numbers. The correspondence of these pads/vias to actual connector contacts remains to be verified.

## Reported unpowered continuity observations

| Reference pads | Observed reading or beep | Status |
|---|---|---|
| A01, B01, C01, D01 | Continuity beep to positive terminal of the two middle pink-top motherboard capacitors | Candidate `POWER_NET_A`, voltage unknown |
| A02, B02, C02, D02 | Same continuity | Candidate `POWER_NET_A`, voltage unknown |
| A03, B03, C03, D03 | No beep to tested ground or `POWER_NET_A` | Unknown, not automatically a PCIe signal |
| A04, B04, C04, D04 | No beep to tested ground or `POWER_NET_A` | Unknown |
| A05, B05, C05, D05 | Ground continuity reported | GND candidate |
| A06, B06, C06, D06 | Ground continuity reported | GND candidate |
| G01–G08 | Ground continuity reported | GND candidate |

The two middle pink capacitors' positive terminals beep to one another. An upper-left pink capacitor shares their measured net. A bottom capacitor was reported to have continuity to the battery connector, rather than to those three capacitors. No beep was detected to the unpowered external input path; switching circuitry may interrupt the path, but this is not confirmed.

A beep is evidence only of low measured impedance under a particular meter setting. It **does not prove** the operating voltage, the exact topology, or that two points are directly connected by copper rather than components.

## Open questions

1. Map our photographic identifiers onto the **real socket contacts**.
2. Verify `POWER_NET_A` and its normal operating voltage, maximum current and switching behavior.
3. Identify all additional supply, ground and sideband contacts.
4. Trace PCIe lane pairs, clock, reset, and related signals.
5. Independently verify geometry and all nets prior to PCB fabrication.

**Do not inject power using this map.**
