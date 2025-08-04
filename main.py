import uuid
from impl.team_impl import TeamImpl
from impl.user_impl import UserImpl
from impl.project_board_impl import ProjectBoardImpl
from storage_manager import StorageManager
from models.user_model import User
from models.team_model import Team
from models.project_board_model import ProjectBoard

def main():
    print("Welcome to the Project Planner!")

    # Load data
    users = StorageManager.load_data("users.json")
    teams = StorageManager.load_data("teams.json")
    boards = StorageManager.load_data("boards.json")

    users_db = {}
    teams_db = {}
    boards_db = {}


    for entry in users:
        if isinstance(entry, dict) and all(k in entry for k in ("user_id", "name", "email")):
            user = User(entry["user_id"], entry["name"], entry["email"])
            users_db[user.user_id] = user
        else:
            print("Invalid user entry skipped:", entry)

    # Parse teams
    for team in teams:
        if isinstance(team, dict):
            try:
                teams_db[team["team_id"]] = Team(team_id=team["team_id"], name=team["name"], members=team.get("members", []))
            except Exception as e:
                print(f"Invalid team entry: {team} | Error: {e}")
        else:
            print(f"Invalid team entry: {team}")

    # Parse boards
    for board in boards:
        if isinstance(board, dict):
            try:
                boards_db[board["board_id"]] = ProjectBoard(
                    board_id=board["board_id"],
                    name=board["name"],
                    team_id=board["team_id"],
                    tasks=board.get("tasks", {})
                )
            except Exception as e:
                print(f"Invalid board entry: {board} | Error: {e}")
        else:
            print(f"Invalid board entry: {board}")

    # Initialize implementations
    user_impl = UserImpl(users_db)
    team_impl = TeamImpl(teams_db)
    board_impl = ProjectBoardImpl(boards_db, teams_db)

    # create a user
    user_id = str(uuid.uuid4())
    user_name = "test3"
    user_email = "test3@example.com"
    new_user = User(user_id=user_id, name=user_name, email=user_email)
    user_impl.create_user(new_user)
    users_db[new_user.user_id] = new_user 
    print(f"User '{new_user.name}' created with ID {new_user.user_id}")

    # create a team
    team_id = str(uuid.uuid4())
    new_team = Team(team_id=team_id, name="DevOps Team", members=[user_id])
    team_impl.create_team(new_team)
    print(f"Team '{new_team.name}' created with ID {new_team.team_id}")


    # Create board
    board_id = str(uuid.uuid4())
    board_name = "backend Board"
    new_board = ProjectBoard(board_id=board_id, name=board_name, team_id=team_id, tasks={})
    board_impl.create_board(new_board)
    boards_db[new_board.board_id] = new_board   # ← this is crucial
    print(f"Board '{new_board.name}' created with ID {new_board.board_id}")



    # When saving users
    print("Saving users:")
    print([user.to_dict() for user in users_db.values()])
    StorageManager.save_data("users.json", [user.to_dict() for user in users_db.values()])

    
    # When saving boards
    print("Saving boards:")
    print([board.to_dict() for board in boards_db.values()])
    StorageManager.save_data("boards.json", [board.to_dict() for board in boards_db.values()])


    # When saving teams
    print("Saving teams:")
    print([team.to_dict() for team in teams_db.values()])
    StorageManager.save_data("teams.json", [team.to_dict() for team in teams_db.values()])
    print("Data successfully saved.")

if __name__ == "__main__":
    main()
