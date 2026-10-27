# Reverse-engineering roadmap

- [x] Identify on-module GPU and major components from photos (preliminary).
- [x] Read 4 MiB SPI flash from donor motherboard using CH341B programmer.
- [x] Obtain two byte-identical firmware dumps (owner confirmed 2026-10-24).
- [x] Extract two structurally valid NVIDIA option ROM candidates.
- [ ] Identify actual donor motherboard PCB model and revision from silkscreen.
- [ ] Locate reliable boardview/schematic for **that exact** revision.
- [ ] Photograph and count proprietary GPU socket contacts.
- [ ] Create a complete, experimentally verified connector pinout.
- [ ] Determine required supplies / load / power sequence with schematics and safe measurements.
- [ ] Identify module PCI device and subsystem IDs; select correct VBIOS/initialization strategy.
- [ ] Design non-destructive adapter/prototype with suitable power, protection and PCIe routing.
- [ ] Current-limited bring-up and `lspci -nn` detection, then driver tests.
- [ ] Thermal design, enclosure and portability refinement.

## Prototype-first scope
First target is enumerating the GPU on a host via PCIe. Standalone physical video outputs, GPU compute acceleration, and USB-C/USB4 eGPU support are **later and distinct milestones**. This is an early Fermi GPU; modern NVIDIA proprietary drivers are not a safe assumption.
