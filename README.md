# Pharmacist Robot — ECSE 211 Final Project (Winter 2026)

An autonomous LEGO EV3 robot built for **ECSE 211: Design Principles and Methods II** at McGill University. The robot picks up a "medication" block, navigates a hospital-floor-plan course by following lines and detecting color-coded intersections, and delivers the block to a target bed/room, using onboard ultrasonic, color, gyroscope, and touch sensors.

Built by a small team (Hassan and Sonia, credited in commit history) using feature branches per subsystem — line following, color/intersection detection, gyroscope-based turning, drive system, and the pickup/delivery claw — before integrating into `main`.

## Subsystems

**Drive system** (`test/drive_system`, integrated into `main.py`)
Two-motor differential drive (`leftWheel`/`rightWheel` on ports B/A) with helper functions for forward/backward movement, in-place spins, and left/right turns via relative encoder positioning.

**Claw / pickup mechanism** (`test/claw_mechanism`)
A two-motor arm + gripper (ports C/D) that raises/lowers and opens/closes to pick up and set down a block, sequenced through `bring_cube_up()` / `bring_cube_down()`.

**Color & intersection detection** (`experiment/color_identification`, `test/color_sensor_calibration`)
An `EV3ColorSensor` reads RGB, normalizes it, and classifies it against pre-calibrated cluster centers and standard deviations for six colors (red, green, blue, yellow, orange, white) plus line/intersection detection — calibration data collected and stored per-color as CSV/Excel samples, with matching done via a 2-standard-deviation threshold per channel (`Color.is_match()` / `find_distance()`).

**Line following** (`experiment/line_follower`, `test/line_follower`)
A wiggle-based line follower that reads the color sensor to detect the line and adjusts motor speed to stay on it, with a planned path/intersection-based navigation strategy for the hospital floor plan (documented in `Line Follower Path Map + Logic and Info.png` / `Line Follower Code Discussion.txt`) — pick up meds, orient to the door, follow the path through turns and realignments, locate the target bed, deliver, and return.

**Gyroscope-based turning** (`test/gyro_sensor`)
Turning and orientation logic backed by empirical gyro data — recorded readings for 90°/180° turns, straight-line drift, and idle noise, analyzed with NumPy (`gyro_sensor_data_crunching.py`) to derive mean/standard-deviation baselines used to make turns and heading corrections more reliable.

## Project Structure

```
├── Documentation/
│   ├── Gantt_Chart/            # Project timeline/planning docs
│   └── Testing Procedures/     # Sensor test procedure write-ups
├── src/
│   ├── main.py                 # Integrated entry point (drive + claw on main branch)
│   └── utils/                  # EV3 hardware interface layer (brick.py, rmi.py, sound.py, filters.py, telemetry.py, remote.py)
└── testing/
    └── claw.py                 # Claw mechanism test script
```

Branch-specific work (not yet merged to `main`) additionally includes:
```
src/color.py                    # Color classification (experiment/color_identification)
src/data/calibration_data_*.csv # Per-color RGB calibration samples
src/testing/line-follower.py    # Line-following logic (experiment/line_follower)
src/data_analysis/*.csv, .py    # Gyro sensor calibration data + analysis (test/gyro_sensor)
```

## Tech Stack

- **Python**, running on the **LEGO EV3 brick** (via `ev3dev`-style RPyC brick interface in `utils/brick.py`, `utils/rmi.py`)
- **NumPy** for sensor calibration data analysis
- Sensors: EV3 color sensor, ultrasonic sensor, touch sensor, gyroscope
- Git feature branching per subsystem (`experiment/*` for exploratory work, `test/*` for isolated hardware testing)

## Status

`main` currently integrates the drive system and claw mechanism with a manual test routine (`testMovement()`). Color/intersection detection, line following, and gyro-calibrated turning are developed and validated on their own branches with real calibration data, but not yet merged into a single autonomous run — integrating all subsystems into one navigation loop is the remaining work.

## Team & Course Context

Built as a final design project for ECSE 211 at McGill, covering the full design cycle — requirements, iterative subsystem testing with real sensor data, and integration — for an autonomous robot completing a real-world-inspired delivery task.
