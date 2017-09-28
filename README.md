scrabble_solver
===============

Command-line tool to generate and score possible Scrabble words from a given rack.

## Description

I made this in an afternoon for fun and as an exercise in writing clean, readable code. If any of it would be useful, feel free to clone the repo and play around with it.

## Install
Install manually with

    git clone git://github.com/nathan-hunt/scrabble_solver.git

## Usage:

    python scrabble.py [RACK]

where the rack is a group of seven letters (or really as many as you want).

The output is every possible Scrabble-legal word and its score, ordered by score from highest to lowest.

