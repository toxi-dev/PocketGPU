# ToxiTech PocketGPU v0.1 — KiCad design starter

## What this project actually contains

- An **editable KiCad schematic**, including a provisional 314-contact symbolic inventory (not a confirmed pin count), separate host PCIe x4 planning symbol, and power/reset-control planning symbol.
- An **editable KiCad four-layer PCB** with a **130 × 95 mm *conceptual* outline**, labels, mechanical reserved regions, and two **board-only footprints with ZERO copper pads**.
- A local symbol library, local footprint library and pin-map CSV for recording measured connections.
- No guessed power or PCIe connections, no routings, no copper pours, no fabrication outputs.

## Critical non-production warnings

**DO NOT FABRICATE, ORDER, POPULATE, OR POWER THIS BOARD.** The ASUS GPU connector pin count and numbering, pitch, housing outline, height, locating pegs, orientation and mating connector remain unverified. The envelopes are diagrams, **not solderable footprints**.

- `J_GPU1` numbers 1..314 are **arbitrary inventory row numbers**, not physical ASUS pin numbers. **314 is a working hypothesis only.**
- `J_HOST1` names illustrate the PCIe x4 electrical *functions*; they're not actual PCIe card-edge finger assignments.
- All rail voltages/current ratings, enable and reset levels and sequencing are unknown.
- Mechanical size 130 × 95 mm, clearances and 1.6 mm thickness are editable placeholders, not measured design parameters.
- 4-layer stack is planned, not impedance-calculated. PCIe signals require controlled impedance and verified launch geometry.

## Planned schematic architecture

1. GPU connector mapping (J_GPU1): 314? provisional unconnected pins.
2. Host interface planning (J_HOST1): PCIe lanes 0–3, reference clock, PERST#, optional sideband, host power groups.
3. Power/reset sequencing plan (U_CTRL1): unknown enable, PGOOD, reset and auxiliary rails.
4. Later: exact connector pin map, chosen host connector, PSU topology, PGOOD/reset logic, protections, impedance-stackup details.

## Verification gates to unlock a real revision

- Identify actual connector manufacturer/part number and retrieve mechanical drawing.
- Count *physical contacts* and define unambiguous pin-1 corner/orientation.
- Trace GND and all supply contacts on **unpowered** donor board, measure voltage levels only on a safely repaired/known-good donor (not required for v0.1).
- Trace differential PCIe pairs + reference clock + reset + sideband signals with supporting evidence.
- Determine VBIOS firmware path; two extracted candidates exist but which applies is not confirmed.
- Reconcile netlist, footprint pad numbers and EDA checks, then impedance control & design review.

## How to use

Open `kicad/PocketGPU_v0.1.kicad_pro` in KiCad 8/9; open schematic and PCB separately. The local libraries should be picked up from the included `*-lib-table`. This project was generated from KiCad's documented s-expression syntax, but **KiCad CLI/ERC/DRC could not be run in the build environment**. Inspect and resave before modifying.

Do not auto-update the PCB from schematic yet: the symbols are deliberately `on_board no` and board footprints deliberately board-only because no actual pads exist.
