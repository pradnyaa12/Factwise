from abc import ABC, abstractmethod

class ProjectBoardBase(ABC):
    @abstractmethod
    def to_dict(self):
        pass

    @abstractmethod
    def update_task_status(self, task_id, status):
        pass
class ProjectBoard(ProjectBoardBase):
    def __init__(self, board_id, name, team_id, tasks):
        self.board_id = board_id
        self.name = name
        self.team_id = team_id
        self.tasks = tasks

    def to_dict(self):
        return {
            "board_id": self.board_id,
            "name": self.name,
            "team_id": self.team_id,
            "tasks": self.tasks
        }


    def update_task_status(self, task_id, status):
        for task in self.tasks:
            if task["task_id"] == task_id:
                task["status"] = status
                break
