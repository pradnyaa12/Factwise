from abc import ABC, abstractmethod

class ProjectBoardBase(ABC):

    @abstractmethod
    def create_board(self, team_id: str, name: str) -> dict:
        pass

 
    @abstractmethod
    def add_task(self, board_id: str, title: str, description: str, assigned_to: str) -> dict:
        pass

    @abstractmethod
    def update_task_status(self, board_id: str, task_id: str, new_status: str) -> dict:
        
        pass

    @abstractmethod
    def export_board(self, board_id: str) -> str:
        pass
