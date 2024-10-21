# Three-Body Orbit Plot: Earth, Moon, and Satellite

## Overview:
This program plots the three-body orbit of the Earth, Moon, and a satellite orbiting the Earth. The satellite's motion is computed in a rotating reference frame where the origin is located at the center of mass of the Earth-Moon system. The program visualizes the **x** and **y** positions of the satellite over time and shows its orbital pattern relative to the Earth and the Moon.

## Dependencies:
This program uses the following Python libraries:
1. **Matplotlib**: For plotting the orbital paths.
2. **SciPy**: Specifically, `scipy.integrate.odeint` is used to solve the system of differential equations representing the equations of motion.
3. **NumPy**: For numerical operations and array handling.

### How to Install the Required Libraries:
You can install the required libraries using `pip`, the Python package manager. Here’s how to install them on different operating systems:

### For MacOS, Windows, and Linux:
1. Open your terminal (MacOS/Linux) or command prompt (Windows).
2. Run the following commands to install the necessary packages:

## Equations of Motion:
The equations of motion for the satellite are computed in a **rotating reference frame**. The origin of this frame is placed at the **center of mass** of the Earth-Moon system. This reference frame allows us to observe how the satellite's position changes over time, taking into account the gravitational forces from both the Earth and the Moon. There is also the Coriolis and Centrifugal forces that are taken into account to help illustrate the behavior in the rotating reference frame.

In this frame, we calculate the forces and accelerations acting on the satellite, then use **SciPy’s `odeint`** function to numerically integrate these equations of motion over time.

## Plotting:
Once the equations of motion are computed, the program uses **Matplotlib** to plot the satellite's trajectory. The program specifically plots the **x** and **y** positions of the satellite over time to show its orbit around the Earth and the Moon.

### Key Features:
- The Earth and Moon positions are included in the plot to provide reference points.
- The plot displays how the satellite's trajectory evolves over time and how it interacts with the gravitational pulls of both the Earth and Moon.
- The plots and Equations of motion take into account both the Centrifugal and Coriolis force from being in the rotating reference frame.

## Running the Program:
Once you have installed the required packages, you can run the program by executing the Python script. The script will generate a plot showing the orbital pattern of the satellite.

Example usage:

This will open a plot window, displaying the satellite's path as it orbits around the Earth and Moon.

The Satellites path in the x direction with respect to time and the satellites path in the y direction with respect to time.

Enjoy visualizing the complex dynamics of a three-body system!
