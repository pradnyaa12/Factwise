from abc import ABC, abstractmethod

class TeamBase(ABC):
    @abstractmethod
    def to_dict(self):
        pass

class Team(TeamBase):
    def __init__(self, team_id, name, members=None):
        self.team_id = team_id
        self.name = name
        self.members = members or [] 

    def to_dict(self):
        return {
            "team_id": self.team_id,
            "name": self.name,
            "members": self.members
        }
