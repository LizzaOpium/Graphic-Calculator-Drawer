"""
Project: Ladder Geometry Visualizer
Author: Alexey Popov
Description:
    This program visualizes a 3D-ish projection of the structure made of 
    four 1.8-meter wooden beams standing on the ground 0.2 m apart, with 
    six horizontal platforms every 0.2 m height.

    The purpose of the program:
        • Show the geometry clearly
        • Demonstrate coordinate-based construction
        • Provide clean axes and scaling
        • Be easy to convert into .exe using PyInstaller

Libraries used:
    matplotlib.pyplot — draws the figure
    numpy — used only for generating numeric ranges cleanly

How to compile into .exe:
    pyinstaller --noconsole --onefile plot_ladder.py
"""

import matplotlib.pyplot as plt
import numpy as np


def build_vertical_beams():
    """
    Creates coordinates of the 4 vertical beams.
    The beams:
        • Height = 1.8 m
        • Ground positions: x = 0, 0.2, 0.4, 0.6
    Returns:
        list of vertical line segments
    """
    heights = np.linspace(0, 1.8, 200)
    xs = [0, 0.2, 0.4, 0.6]

    beams = []
    for x in xs:
        beams.append((x * np.ones_like(heights), heights))

    return beams


def build_horizontal_platforms():
    """
    Creates the 6 horizontal platforms.
    Conditions:
        • First: at height 0.2 m
        • Step: 0.2 m
        • Total: 6 platforms
        • They connect ALL 4 beams → run from x = 0 to x = 0.6

    Returns:
        list of line segments (x array, y array)
    """
    platforms = []
    xs = np.array([0, 0.6])
    for k in range(1, 7):  # 6 platforms
        y = 0.2 * k
        platforms.append((xs, y * np.ones(2)))

    return platforms


def plot_structure():
    """
    Main plotting function.
    Builds:
        1. Vertical beams
        2. Horizontal platforms
    Styles:
        • Thick lines for beams
        • Thinner lines for platforms
        • Proper axes scaling
        • Grid for clarity
        • "Equal" aspect ratio for geometry correctness
    """
    beams = build_vertical_beams()
    platforms = build_horizontal_platforms()

    fig, ax = plt.subplots(figsize=(8, 6))

    # Draw vertical beams
    for x, y in beams:
        ax.plot(x, y, linewidth=3)

    # Draw horizontal platforms
    for xs, ys in platforms:
        ax.plot(xs, ys, linewidth=2)

    # Axes configuration
    ax.set_xlim(-0.1, 0.7)
    ax.set_ylim(0, 2.0)

    ax.set_xlabel("x, meters", fontsize=12)
    ax.set_ylabel("height, meters", fontsize=12)
    ax.set_title("Fruit Ladder Structure — Geometric Visualization", fontsize=14)

    # Make axes look clean
    ax.grid(True, linestyle="--", linewidth=0.5)
    ax.set_aspect("equal", adjustable="box")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_structure()
