from abc import ABC, abstractmethod

class UserBase(ABC):
    @abstractmethod
    def to_dict(self):
        pass


class User(UserBase):
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email
        }

