# Pirate-ISLAND-Game

# Overview

This repository contains a Python-based interactive Treasure Island game. The player assumes the role of a pirate navigating an island grid to find hidden treasure while overcoming obstacles such as water tiles and managing thirst levels. A compass provides feedback to assist in the search for treasure.

# File Descriptions

# Main Game File

game.py: Contains the main game loop, handling user interactions, initiating the island grid, pirate positioning, treasure placement, and compass feedback. It manages the gameplay, allowing movements, actions like drinking grog, and handling game termination.

# Supporting Classes

Island.py: Contains the Island class responsible for generating and displaying the island grid. It manages the placement of water tiles and checks for valid player moves.

Pirate.py: Defines the Pirate class representing the player's character. Handles pirate movements, thirst levels, drinking grog, and checking for treasure discovery.

Treasure.py: Implements the Treasure class, spawning the treasure randomly on the island and managing its coordinates.

Compass.py: Provides the Compass class, which gives feedback on the pirate's proximity to the treasure based on distance calculations.

# Gameplay Features

Interactive gameplay with user input for movement (north, south, east, west), drinking grog, and quitting the game.

Dynamic difficulty settings (Arrrd: Easy, Arrrd..rrr: Medium, Very Arrrrd: Hard), affecting the island's size and water density.

Real-time feedback from the compass guiding the player towards the treasure.

Thirst mechanic adds a survival aspect, requiring periodic drinking of grog to continue moving.

# Instructions

Run game.py to start the game.

Follow on-screen prompts to move the pirate, manage thirst, and find the treasure.

Input directions carefully without trailing spaces to ensure valid game responses.

# Author

Vraj Patel (Username: PATVN002)

This project complies with the University's Academic Misconduct Policy.
