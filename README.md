# Projectile Motion Simulator

## Overview  
This program simulates **projectile motion** based on user-defined **initial velocity** and **launch angle**.  
It calculates and displays the **range**, **maximum height**, and **total flight time** of the projectile.  
Additionally, the user can input a specific time to determine the **instantaneous velocity** of the projectile at that moment.  
Finally, the program visualizes the projectile’s trajectory using a **graph**.

## Features  
- Calculates:
  - **Range (Horizontal Distance)**  
  - **Maximum Height**  
  - **Total Flight Time**  
- Computes **velocity at a given time (t)**  
- Displays a **trajectory plot** using `matplotlib`  
- Contains **commented code sections** for better readability and understanding  

## How It Works  
1. The user inputs the **initial velocity (v₀)** and **launch angle (θ)**.  
2. The program applies standard projectile motion equations:  
   - `Range = (v₀^2 * sin(2θ)) / g`  
   - `Height_max = (v₀^2 * sin^2(θ)) / (2 * g)`  
   - `Time_flight = (2 * v₀ * sin(θ)) / g`  
3. The user can input a **time (t)** to calculate the **instantaneous velocity**.  
4. The program plots the projectile’s motion using `matplotlib`.

## Requirements  
- Python 3.x  
- `matplotlib`  
- `math` (standard library)  

Install the required library:  
```bash
pip install matplotlib
```

## Usage  
Run the program in your terminal or IDE:  
```bash
python projectile_motion.py
```
Follow the on-screen instructions to enter:  
- Initial velocity (m/s)  
- Launch angle (degrees)  
- Time (s) to calculate velocity  

## Example Output  
```
Range: 102.5 m  
Maximum Height: 25.6 m  
Total Flight Time: 4.57 s  
Velocity at 2 s: 18.4 m/s  
```
A graph showing the projectile’s trajectory will be displayed.  

## License  
This project is open-source and available for educational and research purposes.  

## Author  
**Created by:** Yavuz Selim Şahin  
**Year:** 2025
