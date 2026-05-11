# Hardware

## Bill of materials

| Component | Qty | Notes |
|---|---:|---|
| Arduino MEGA 2560 | 1 | Drives both motors via Firmata |
| 28BYJ-48 stepper motor (5 V) | 2 | One per axis (X, Y) |
| ULN2003 driver board | 2 | Bundled with the motors |
| Olympus CX41 microscope | 1 | Any compound microscope with a movable stage works |
| USB microscope camera | 1 | Any OpenCV-compatible camera |
| 3D-printed mounts | 3 | See `stl/` |
| Jumper wires, USB cable | — | |

## 3D-printed parts

Print settings: **PLA · 0.2 mm layers · 30 % infill · no supports** (orient flat faces down).

| File | Purpose |
|---|---|
| `stl/stage.stl` | Main stage extension that interfaces with the microscope's mechanical stage |
| `stl/stage_mount.stl` | Bracket that anchors the X-motor and aligns it with the stage knob |
| `stl/coupling.stl` | Adapter coupling linking the stepper output shaft to the focus/translation knob |

## Wiring

| Axis | IN1 | IN2 | IN3 | IN4 | VCC | GND |
|---|---:|---:|---:|---:|---|---|
| X motor | D4 | D5 | D6 | D7 | Arduino 5 V | Arduino GND |
| Y motor | D8 | D9 | D10 | D11 | Arduino 5 V | Arduino GND |

The two 28BYJ-48 steppers run from the Arduino's on-board 5 V rail. For longer or higher-torque runs, power the ULN2003 boards from an external 5 V supply.

See the breadboard and schematic diagrams in the top-level [README](../README.md).
