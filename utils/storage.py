import json
import os

class StorageManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump({}, f)

    def read(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def write(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=2)

    def get(self, id: str):
        data = self.read()
        return data.get(id)

    def save(self, id: str, obj: dict):
        data = self.read()
        data[id] = obj
        self.write(data)

    def delete(self, id: str):
        data = self.read()
        if id in data:
            del data[id]
            self.write(data)
