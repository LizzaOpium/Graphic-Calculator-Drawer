# Graphic Calculator

## Project Information

**Project:** Ladder Geometry Visualizer / Graphic Calculator
**Author:** Alexey Popov

This application visualizes a vertical ladder-like structure made of wooden beams and horizontal platforms using coordinate-based geometry. The project is implemented in Python and distributed as a standalone Windows executable (.exe).

The program is designed for educational purposes and demonstrates how geometric objects can be constructed and visualized using numerical methods.

---

## Project Description

The program builds a 2D geometric projection of the following structure:

* 4 vertical wooden beams
* Each beam has a height of **1.8 meters**
* The distance between neighboring beams is **0.2 meters**
* 6 horizontal platforms
* Platforms are placed every **0.2 meters** in height
* All platforms connect all four beams

The result is a clear geometric model that resembles a ladder or scaffolding structure.

---

## Purpose of the Project

* Visual demonstration of geometry using coordinates
* Demonstration of numerical model construction
* Practice with plotting and scaling
* Visualization of real-world structures in a mathematical form
* Easy conversion into an executable (.exe) file

---

## Technologies Used

* **Python 3** — main programming language
* **matplotlib.pyplot** — used for drawing the figure
* **numpy** — used for numerical arrays and clean range generation

---

## How the Structure is Built

### Vertical Beams

* Height: 1.8 meters
* X coordinates: `0`, `0.2`, `0.4`, `0.6`
* Each beam is drawn as a vertical line segment

### Horizontal Platforms

* First platform at height `0.2 m`
* Step size: `0.2 m`
* Total: 6 platforms
* Each platform connects all beams from `x = 0` to `x = 0.6`

---

## Axis Settings and Visualization

* Equal scaling on both axes
* Grid enabled
* Correct proportional geometry
* Clear axis labels and title

---

## Running the Program from Python

If you want to run the source code directly:

```bash
pip install matplotlib numpy
python GRAPH.py
```

---

## Executable Version (.exe)

The compiled Windows executable is named:

```
grafik.exe
```

It is located inside the archive:

```
Graphic Calculator
```

and published in this GitHub repository.

The executable version does **not require Python to be installed**.

---

## How to Build the EXE Yourself

To build the executable manually:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile GRAPH.py
```

The final `.exe` file will appear in the `dist` folder.

---

## Educational Value

This project can be used for:

* School geometry projects
* Demonstration of coordinate systems
* Learning numerical modeling
* Introduction to scientific visualization

---

## Author

Alexey Popov
