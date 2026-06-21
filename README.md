# Gravitational Lensing Simulation & Reconstruction

This repository contains a comprehensive study and simulation of **Gravitational Lensing**, ranging from classical optics analogies to relativistic light deflection and source reconstruction from lensed images.

The project was developed as part of the Krittika Summer Projects (KSP) 7.0 Selection Assignment.

## Project Overview

Gravitational lensing occurs when a massive object (the lens) bends the light from a distant source, creating distortions, multiple images, or even an Einstein Ring. This project implements the physics of these phenomena using numerical methods and provides tools for both forward simulation and inverse reconstruction.

### Key Features

*   **Classical Optics Analogy:** Modeling a thin convex lens and ray tracing.
*   **Numerical Modeling:** Solving the exact lens equation using the **Newton-Raphson method**.
*   **Forward Simulation:** Simulating point and extended sources (galaxy models) lensed by a point mass.
*   **Einstein Ring Formation:** Demonstrating the effect of perfect source-lens-observer alignment.
*   **Source Reconstruction:**
    *   Inverse mapping of discrete lensed points.
    *   **Bitmap De-lensing:** Reconstructing the original source from a real astronomical image (Hubble LRG 3-757) using OpenCV.

## Visualizations

### 1. Error Analysis of Small-Angle Approximation
We analyzed the validity of the small-angle approximation in gravitational lensing by comparing it to the exact numerical solution.

![Error Analysis](plots/error_analysis.png)

### 2. Extended Source Lensing
Simulating how a circular galaxy is distorted into arcs when lensed.

![Extended Source](plots/extended_source.png)

### 3. Einstein Ring
When the source is perfectly aligned with the lens, it forms a complete ring of light.

![Einstein Ring](plots/einstein_ring.png)

### 4. Bitmap Reconstruction (Bonus)
Using the inverse lens equation to "un-bend" the light from a Hubble bitmap image of a lensed galaxy.

![Reconstruction](plots/reconstruction.png)

## Technical Skills Highlighted

*   **Physics Modeling:** Implementation of General Relativity-based light deflection equations.
*   **Numerical Methods:** Newton-Raphson iteration for transcendental equations.
*   **Data Analysis:** Handling and processing astronomical coordinate data (Pandas).
*   **Computer Vision:** Image processing and inverse mapping using NumPy and OpenCV.
*   **Scientific Visualization:** Professional-grade plotting with Matplotlib.

## Repository Structure

*   `KSP_Coding_Assignment.ipynb`: Complete project walkthrough with code and explanations.
*   `q1.py` to `q7.py`: Standalone scripts for each part of the assignment.
*   `lensed_points.csv`: Dataset for source reconstruction.
*   `hubble-lrg3757.bmp`: Real-world lensed galaxy image used for the bonus part.

## Setup

To run the simulations, install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the scripts individually or explore the Jupyter Notebook.
