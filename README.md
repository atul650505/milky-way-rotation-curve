# Mapping the Milky Way's Rotation Curve from the 21 cm Line of Neutral Hydrogen

## Overview
This repository contains a Python data pipeline and the accompanying LaTeX project files for mapping the kinematics of the Milky Way Galaxy. The project analyzes 21 cm emission data from the HI4PI all-sky survey to derive the rotation curve of the inner Milky Way and estimate its enclosed dynamical mass. 

**Author:** Atul K Suresh  
**Institution:** Ramnarain Ruia Autonomous College / ASTRO-NOT

## Methodology & Physical Parameters
The analysis isolates neutral hydrogen (H I) spectral data across Galactic longitudes 15° to 80°. Data cuts and extraction methods were strictly governed by physical considerations:
* **Latitude Limits:** Constrained based on the physical thickness of the Galactic hydrogen disk.
* **Longitude Limits:** Specifically chosen to avoid interference from the Galactic bar and to account for the intrinsic broadening of the gas.
* **Velocity Extraction:** The terminal velocity of the neutral hydrogen along each line of sight was extracted using a fixed brightness threshold.
* **Calibration:** Rather than relying on theoretical bias, the systematic bias of the velocity edge was empirically calibrated using high-longitude sightlines.
* **Kinematics:** The tangent-point method was applied to convert terminal velocities into the final rotation curve. 

## Key Results
* **Rotation Curve:** The measured rotation curve rises from approximately 200 km/s near 2 kpc to a stable plateau close to 235 km/s. Irregularities observed in the curve were interpreted as genuine gas motions rather than noise.
* **Enclosed Mass:** The enclosed dynamical mass within the solar circle was calculated to be (1.10 ± 0.08) × 10¹¹ solar masses.
* **Dark Matter:** The conclusions strictly outline the total gravitating mass, keeping this empirical measurement separate from direct claims regarding dark matter halos.

## Repository Structure
* **Pipeline:** Python scripts for data reduction and spectral analysis (e.g., `make_sample_spectrum.py` for generating velocity profiles).
* **Data Visualizations:** Found in the `figures/` directory, including `sample_spectrum.pdf` and `sample_spectrum.png`.
* **Report Source:** The complete LaTeX source code for the project report, including `main.tex`, `astronot.sty`, and `refs.bib`.
