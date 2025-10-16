# path: oblique_shot_speed_with_graph.py
"""
Oblique projectile motion calculator.
This program:
- Receives the projectile angle and initial velocity from the user.
- Calculates maximum altitude, range, and flight time.
- Finds the object's speed at any given moment.
- Displays the trajectory graphically.
"""

import math
import matplotlib.pyplot as plt

GRAVITY = 9.81  #Gravitational acceleration(m/s²)

# --- Mathematical Part ---

def to_radians(angle_deg: float) -> float:
    #Converts degrees to radians.
    return angle_deg * math.pi / 180.0

def projectile_info(angle_deg: float, v0: float):
    #Calculates basic orbital information from angle and initial velocity.
    theta = to_radians(angle_deg)
    v0x = v0 * math.cos(theta)   #Horizontal velocity component
    v0y = v0 * math.sin(theta)   #Vertical velocity component

    #Flight duration (until touchdown)
    t_flight = 2 * v0y / GRAVITY
    #maximum height
    max_height = (v0y ** 2) / (2 * GRAVITY)
    #Total horizontal distance (range)
    range_ = v0x * t_flight

    return v0x, v0y, t_flight, max_height, range_

def position_at_time(v0x: float, v0y: float, t: float):
    #Returns the position of the object at a given time.
    x = v0x * t
    y = v0y * t - 0.5 * GRAVITY * t**2
    return x, y

def speed_at_time(v0x: float, v0y: float, t: float):
    #Returns the velocity components and magnitude at a given time.
    vy = v0y - GRAVITY * t               #Vertical speed decreases with time
    v = math.sqrt(v0x ** 2 + vy ** 2)    #Total speed magnitude(v = √(vx² + vy²))
    return v0x, vy, v

# --- Main Program flow ---

def main():
    print("=== Oblique Projectile Motion Calculator ===")

    #The part where we receive the opening and initial inputs from the user
    angle = float(input("Enter launch angle (degrees): "))
    v0 = float(input("Enter initial speed (m/s): "))

    #The part that calculates orbital information
    v0x, v0y, t_flight, h_max, range_ = projectile_info(angle, v0)

    #The part that prints the results to the screen
    print(f"\nMaximum height: {h_max:.2f} m")
    print(f"Horizontal range: {range_:.2f} m")
    print(f"Total flight time: {t_flight:.2f} s")

    #The part where data is taken from the user to find out the speed at any given moment
    t = float(input("\nYou want to know the speed at what second? "))

    if t > t_flight:
        print("! The object has already hit the ground.")
        return

    #The part that allows us to calculate the velocity component at the desired moment
    vx, vy, v = speed_at_time(v0x, v0y, t)
    x, y = position_at_time(v0x, v0y, t)

    #The part that prints the results to the terminal
    print(f"\nAt t = {t:.2f} s:")
    print(f"  ➤ Horizontal velocity: {vx:.2f} m/s")
    print(f"  ➤ Vertical velocity: {vy:.2f} m/s")
    print(f"  ➤ Total speed: {v:.2f} m/s")
    print(f"  ➤ Position: ({x:.2f}, {y:.2f}) m")

    #The part that draws the orbit graph
    times = [i * t_flight / 100 for i in range(101)]  #100 steps from 0 to flight time
    xs = [v0x * ti for ti in times]
    ys = [v0y * ti - 0.5 * GRAVITY * ti**2 for ti in times]

    plt.figure(figsize=(8, 5))
    plt.plot(xs, ys, label="Trajectory")               #orbital curve
    plt.scatter(x, y, color="red", zorder=5, label=f"t = {t:.2f}s")  #chosen moment
    plt.title("Oblique Projectile Motion")
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()