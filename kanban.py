from models import Board, Task
from storage import load_data, save_data

# Add functions for creating, listing, and deleting boards and tasks
def create_board(data, name):
    board = {"board_id": len(data["boards"]), "name": name, "tasks": []}
    data["boards"].append(board)
    print(f'Board "{name}" created.')

def list_boards(data):
    for board in data["boards"]:
        print(f'{board["board_id"]}: {board["name"]}')

def delete_board(data, name):
    for board in data["boards"]:
        if board["name"] == name:
            data["boards"].remove(board)
            print(f'Board "{name}" deleted.')
            return
    print(f'Board "{name}" not found.')

def create_task(data, board_name, title, description, assignee, reporter, status, priority):
    # Find the board
    board = next((b for b in data["boards"] if b["name"] == board_name), None)
    if board is None:
        print(f'Board "{board_name}" not found.')
        return
    
    # Create a new task
    task_id = len(board["tasks"])
    task = {
        "task_id": task_id,
        "title": title,
        "description": description,
        "assignee": assignee,
        "reporter": reporter,
        "status": status,
        "priority": priority
    }
    board["tasks"].append(task)
    print(f'Task "{title}" created with ID {task_id}.')

def list_tasks(data, board_name):
    # Find the board
    board = next((b for b in data["boards"] if b["name"] == board_name), None)
    if board is None:
        print(f'Board "{board_name}" not found.')
        return
    
    # List tasks
    for task in board["tasks"]:
        print(f'{task["task_id"]}: {task["title"]} (status: {task["status"]}, priority: {task["priority"]})')

def delete_task(data, board_name, task_id):
    # Find the board
    board = next((b for b in data["boards"] if b["name"] == board_name), None)
    if board is None:
        print(f'Board "{board_name}" not found.')
        return
    
    # Find and delete the task
    task_id = int(task_id)
    for task in board["tasks"]:
        if task["task_id"] == task_id:
            board["tasks"].remove(task)
            print(f'Task "{task_id}" deleted.')
            return
    print(f'Task "{task_id}" not found.')

def move_task(data, board_name, task_id, new_status):
    # Find the board
    board = next((b for b in data["boards"] if b["name"] == board_name), None)
    if board is None:
        print(f'Board "{board_name}" not found.')
        return
    
    # Find the task
    task_id = int(task_id)
    for task in board["tasks"]:
        if task["task_id"] == task_id:
            task["status"] = new_status
            print(f'Task "{task_id}" moved to status "{new_status}".')
            return
    print(f'Task "{task_id}" not found.')
