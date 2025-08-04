from abc import ABC, abstractmethod

class TeamBase(ABC):
    @abstractmethod
    def create_team(self, team_name: str, created_by_user_id: str) -> dict:
        pass

 
    @abstractmethod
    def add_user_to_team(self, team_id: str, user_id: str) -> None:
        pass
