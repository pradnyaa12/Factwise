import json
from base.team_base import TeamBase
from db.constants import TEAMS_JSON_PATH
from models.team_model import Team

class TeamImpl(TeamBase):
    def __init__(self, teams_db=None, users_db=None):
        if teams_db is not None:
            self.teams = teams_db
        else:
            self.teams = self.load_data(TEAMS_JSON_PATH)
        self.users_db = users_db
    @staticmethod
    def load_data(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    @staticmethod
    def save_data(file_path, data):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def create_team(self, team_data: Team):
        self.teams[team_data.team_id] = team_data


    def list_teams(self):
        return self.teams

    def add_user_to_team(self, team_id: str, user_id: str):
        for team in self.teams:
            if team["id"] == team_id:
                if "members" not in team:
                    team["members"] = []
                if user_id not in team["members"]:
                    team["members"].append(user_id)
                    self._save_teams()
                    return True
        return False
