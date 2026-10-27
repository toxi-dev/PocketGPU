# ToxiTech PocketGPU — first KiCad project

**Status:** concept + pinout research, not electronics manufacturing.

Open: `kicad/PocketGPU_v0.1.kicad_pro`
Schematic: `kicad/PocketGPU_v0.1.kicad_sch`
PCB: `kicad/PocketGPU_v0.1.kicad_pcb`
Libs: `kicad/PocketGPU.kicad_sym`, `kicad/PocketGPU.pretty/`, `kicad/{sym,fp}-lib-table`
Inventory: `connector/GPU_contact_inventory_314_ASSUMED.csv`

Hardware clues: ASUS 60-N10MB1300 donor, N55SL.204 firmware, MGM_N12E_2P Rev2.1 graphics module, suspected but **unverified** 314-position proprietary MXM-style connector.

**The footprints are graphical envelopes, NOT electrical solder footprints; do not fabricate or supply power.**

Background: original BIOS backed up twice and verified byte-for-byte; NVIDIA VBIOS candidates previously extracted. The package doesn't duplicate the user's firmware dumps.

Read: `docs/PHASE3_KICAD_STARTER.md`
