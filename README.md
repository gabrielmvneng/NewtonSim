# Gravity Simulation

A simple Newtonian gravity simulation built with Python and Pygame as a learning project.

## About

The goal of this project was to better understand object-oriented programming, vector math, and basic physics by implementing a simple gravity simulation from scratch.

The simulation currently includes:

- Newtonian gravitational attraction between multiple bodies
- Collision detection between bodies
- Wall collisions
- Modular physics system
- Multiple celestial bodies (Earth, Moon, and Mars)

The simulation does **not** aim to be physically accurate. Most values (masses, radii, and gravitational constant) were intentionally adjusted to create interesting behavior and to simplify experimentation.

## Technologies

- Python 3
- Pygame

## Project Structure

```
.
├── main.py          # Main loop and rendering
├── physics.py       # Physics calculations
├── constants.py     # Simulation constants
└── README.md
```

## Running

Install Pygame:

```bash
pip install pygame
```

Run the simulation:

```bash
python main.py
```

## What I Learned

This project helped me practice:

- Object-oriented programming
- Working with modules
- Vector mathematics using `pygame.math.Vector2`
- Newton's law of gravitation
- Collision detection
- Basic physics simulation
- Git workflow (branches, commits and pull requests)

## License

This project is licensed under the MIT License.
