# Asteroids (Boot.dev Project)

A Python implementation of a classic **Asteroids-style game**, built using **Pygame** as part of the Boot.dev curriculum.  

This project focuses on **game loops, time-based simulation, state logging, and object-oriented design**, rather than advanced graphics or physics. The goal was to to understand the **systems-level foundations** that real-time games (and simulations) rely on.

---

## Learning Goals

This project was designed to solidify:

- Multi-file Python project structure
- Object-oriented design using inheritance and composition
- Real-time game loops
- Frame-rate independence using delta time (`dt`)
- State inspection and logging for debugging and testing
- Practical use of virtual environments and dependency management

---

## Key Concepts Implemented

### Game Loop
The core loop follows the classic real-time pattern:

1. Process input events
2. Update game state
3. Render the frame

This loop runs continuously until the player exits the game.

---

### Time Normalization (Delta Time)
To ensure consistent behavior across machines with different performance characteristics, the game uses **delta time (`dt`)**:

- Movement and updates are scaled by elapsed time, not frame count
- The game is capped at **60 FPS**
- This decouples simulation speed from rendering speed

This is a foundational concept for smooth motion, physics simulation, and (eventually) networking.

---

### Logging & Observability
The project includes a lightweight **state logging system** that records snapshots of the game world to a `JSON Lines` file:

- Logs are captured approximately once per second
- Sprite positions, velocities, and screen size are recorded
- Logs enable automated validation via the Boot.dev CLI
- Logs are intentionally excluded from version control

This mirrors real-world debugging and testing techniques used in games and simulations.

---

### Object-Oriented Design
A base `CircleShape` class extends `pygame.sprite.Sprite` and provides shared properties:

- Position
- Velocity
- Radius
- Standard `update(dt)` and `draw(screen)` interfaces

Game objects inherit from this base class, allowing behavior to evolve cleanly as the project grows.

---

## Project Structure

```

asteroids/
├── main.py            # Game entry point and main loop
├── constants.py       # Screen dimensions and shared constants
├── logger.py          # Game state and event logging
├── circleshape.py     # Base class for circular game entities
├── pyproject.toml     # Project metadata and dependencies
├── .venv/             # Virtual environment (not committed)
└── .gitignore

````

---

## Requirements

- Python **3.13**
- [`uv`](https://github.com/astral-sh/uv) for environment and dependency management
- Pygame **2.6.1**

---

## Setup & Run

```bash
uv python pin 3.13
uv venv
source .venv/bin/activate
uv add pygame==2.6.1
uv run main.py
````

Close the game window or press `Ctrl+C` in the terminal to exit.

---

## Extending the Project

Some ideas for future improvements:

* Add scoring and UI overlays
* Implement player lives and respawning
* Add asteroid explosions and visual effects
* Introduce acceleration-based movement
* Wrap objects around screen edges
* Add power-ups (shields, speed boosts, bombs)
* Experiment with non-circular hitboxes
* Improve collision handling and physics realism

---

## Notes

This project intentionally prioritizes **clarity and learning over polish**.
It serves as a foundation for deeper exploration into:

* Game architecture
* Simulation correctness
* Time-based systems
* Debugging real-time programs

---

## Why This Project Matters

This project provided hands-on experience with **real-time systems**, not just Python syntax.

Key skills learned:
- Implementing a **time-based game loop**
- Using **delta time (dt)** to decouple simulation logic from frame rate
- Applying **object-oriented design** with extensible base classes
- Building **observability into a system** via structured state logging
- Managing environments and dependencies with modern Python tooling

---

## Acknowledgements

Built as part of the **Boot.dev** curriculum.
