import os

# Define constants for file paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FOLDER = os.path.join(BASE_DIR, "db")

USERS_JSON_PATH = os.path.join(DB_FOLDER, "users.json")
TEAMS_JSON_PATH = os.path.join(DB_FOLDER, "teams.json")
BOARDS_JSON_PATH = os.path.join(DB_FOLDER, "boards.json")
