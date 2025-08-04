import json
import os


class StorageManager:
    DB_FOLDER = "db"

    @staticmethod
    def _get_path(filename: str) -> str:
        return os.path.join(StorageManager.DB_FOLDER, filename)

    @staticmethod
    def load_data(filename: str) -> list:
        path = StorageManager._get_path(filename)
        if os.path.exists(path): 
            with open(path, "r") as f:
                return json.load(f)
        return []


    # @staticmethod
    # def save_data(filename: str, data: list):
    #     path = StorageManager._get_path(filename)
    #     with open(path, "w") as f:
    #         json.dump(data, f, indent=2)


    @staticmethod
    def save_data(filename: str, data: list):
        os.makedirs(StorageManager.DB_FOLDER, exist_ok=True)  
        path = StorageManager._get_path(filename)
        print(f"[DEBUG] Saving to {path}")
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
