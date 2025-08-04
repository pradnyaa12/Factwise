import os
import json
from abc import ABC
from base.project_board_base import ProjectBoardBase
from models.project_board_model import ProjectBoard


class ProjectBoardImpl(ProjectBoardBase, ABC):
    def __init__(self, boards_db=None, teams_db=None):
        if boards_db is not None:
            # Convert ProjectBoard objects to dicts if needed
            self.boards = [board.to_dict() if isinstance(board, ProjectBoard) else board for board in boards_db.values()]
        else:
            self.boards = self._load_boards()

        self.teams_db = teams_db

    def _load_boards(self):
        if not os.path.exists("db/boards.json"):
            return []
        with open("db/boards.json", "r") as file:
            return json.load(file)

    def _save_boards(self):
        with open("db/boards.json", "w") as file:
            json.dump(self.boards, file, indent=4)

    def create_board(self, board: ProjectBoard):
        self.boards.append(board.to_dict())
        self._save_boards()

    def add_task(self, board_id, task):
        for board in self.boards:
            if board["board_id"] == board_id:
                board["tasks"].append(task)
                self._save_boards()
                break

    def update_task_status(self, board_id, task_name, new_status):
        for board in self.boards:
            if board["board_id"] == board_id:
                for task in board["tasks"]:
                    if task["task_name"] == task_name:
                        task["status"] = new_status
                        self._save_boards()
                        return

    def export_board(self, board_id):
        for board in self.boards:
            if board["board_id"] == board_id:
                path = f"out/{board_id}.json"
                os.makedirs("out", exist_ok=True)
                with open(path, "w") as file:
                    json.dump(board, file, indent=4)
                return path
