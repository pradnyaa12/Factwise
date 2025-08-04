import os
from datetime import datetime


def export_board_view(board: dict) -> str:
    export_dir = "out"
    os.makedirs(export_dir, exist_ok=True)

    filename = f"{board['id']}_export.txt"
    filepath = os.path.join(export_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Board: {board['name']} (ID: {board['id']})\n")
        f.write(f"Created on: {board['creation_time']}\n")
        f.write(f"Team ID: {board['team_id']}\n")
        f.write("\nTasks:\n")
        f.write("-" * 50 + "\n")

        for task in board["tasks"]:
            f.write(f"Task ID: {task['id']}\n")
            f.write(f"Title: {task['title']}\n")
            f.write(f"Description: {task['description']}\n")
            f.write(f"Assigned to: {task['assigned_to']}\n")
            f.write(f"Status: {task['status']}\n")
            f.write(f"Created at: {task['created_at']}\n")
            f.write("-" * 50 + "\n")

    return filepath
