from abc import ABC, abstractmethod

class UserBase(ABC):
    @abstractmethod
    def create_user(self, username: str, email: str) -> dict:
        pass



    @abstractmethod
    def get_user(self, user_id: str) -> dict:
        pass
