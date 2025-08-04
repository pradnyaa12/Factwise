# Project Planner Tool

A simple Python-based command-line tool to manage users, teams, and project boards. All data is stored locally in JSON files using a minimal persistence layer.

## Features

- Create users and save them to `users.json`
- Create teams and assign users to teams (`teams.json`)
- Create boards for specific teams (`boards.json`)
- Clean modular architecture using abstract base classes and implementations

## Requirements

- Python 3.7+

No external packages required.

##  How to Run

1. Open a terminal in the project directory.
2. Run the script:

```bash
python main.py
