import json
import os
import uuid
from datetime import datetime
from base.user_base import UserBase
from models.user_model import User
from db.store import users_db

DB_PATH = os.path.join("db", "users.json")

users_db = {}

class UserImpl(UserBase):
    def __init__(self, users_db=None):
        if users_db is not None:
            self.users = {k: v.to_dict() if hasattr(v, 'to_dict') else v for k, v in users_db.items()}
        else:
            self._load()

    def _load(self):
        if os.path.exists(DB_PATH) and os.path.getsize(DB_PATH) > 0:
            with open(DB_PATH, "r", encoding="utf-8") as f:
                self.users = json.load(f)
        else:
            self.users = {} 

    def _save(self):
        with open(DB_PATH, "w", encoding="utf-8") as f:
            json.dump(self.users, f, indent=2)

    def create_user(self, user: User) -> dict:
        for existing_user in self.users.values():
            if existing_user["name"] == user.name:
                raise ValueError(f"Username '{user.name}' already exists.")

        user_id = str(uuid.uuid4())
        user.user_id = user_id  
        user_data = user.to_dict()
        user_data["created_at"] = datetime.now().isoformat()

        self.users[user_id] = user_data
        self._save()
        return user_data

    def get_user(self, user_id: str) -> dict:
        return self.users.get(user_id)


__all__ = ['UserImpl', 'users_db']
