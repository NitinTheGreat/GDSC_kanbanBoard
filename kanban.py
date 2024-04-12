from models import Task
from storage import save_data

# Create a new board
def create_board(data, name):
    if name in data['boards']:
        print(f'Board "{name}" already exists.')
        return

    # Initialize the board with the three statuses
    data['boards'][name] = {
        'todo': [],
        'in_progress': [],
        'done': []
    }
    print(f'Board "{name}" created.')
    save_data(data)

# List existing boards
def list_boards(data):
    print("Boards:")
    for board_name in data['boards']:
        print(f'- {board_name}')

# Delete a board
def delete_board(data, name):
    if name not in data['boards']:
        print(f'Board "{name}" does not exist.')
        return

    del data['boards'][name]
    print(f'Board "{name}" deleted.')
    save_data(data)

# Create a new task in a board
def create_task(data, board_name, title, description, assignee, reporter, status='Todo', priority='Medium'):
    if board_name not in data['boards']:
        print(f'Board "{board_name}" does not exist.')
        return

    task_id = len(data['boards'][board_name][status.lower()]) + 1
    task = Task(task_id, title, description, assignee, reporter, status, priority)
    data['boards'][board_name][status.lower()].append(task)
    print(f'Task "{title}" created in board "{board_name}".')
    save_data(data)

# List tasks in a board
def list_tasks(data, board_name):
    if board_name not in data['boards']:
        print(f'Board "{board_name}" does not exist.')
        return

    board = data['boards'][board_name]

    print(f'Tasks in board "{board_name}":')
    for status in ['todo', 'in_progress', 'done']:
        print(f'\n{status.capitalize()}:')
        tasks = board[status]
        for task in tasks:
            print(f'- Task ID: {task.task_id}, Title: {task.title}, Priority: {task.priority}, Assignee: {task.assignee}, Reporter: {task.reporter}')

# Delete a task in a board
def delete_task(data, board_name, task_id):
    if board_name not in data['boards']:
        print(f'Board "{board_name}" does not exist.')
        return

    board = data['boards'][board_name]
    task_deleted = False

    # Search and delete the task from each status list
    for status in ['todo', 'in_progress', 'done']:
        tasks = board[status]
        for task in tasks:
            if task.task_id == int(task_id):
                tasks.remove(task)
                print(f'Task ID {task_id} deleted from board "{board_name}".')
                task_deleted = True
                break
        if task_deleted:
            break

    if not task_deleted:
        print(f'Task ID {task_id} not found in board "{board_name}".')
    else:
        save_data(data)

# Move a task to a new status
def move_task(data, board_name, task_id, new_status):
    if board_name not in data['boards']:
        print(f'Board "{board_name}" does not exist.')
        return

    board = data['boards'][board_name]
    task_moved = False

    # Move task from its current status to new status
    for status in ['todo', 'in_progress', 'done']:
        tasks = board[status]
        for task in tasks:
            if task.task_id == int(task_id):
                tasks.remove(task)
                
                # Add task to the new status list
                task.status = new_status
                board[new_status.lower()].append(task)
                
                print(f'Task ID {task_id} moved to {new_status} in board "{board_name}".')
                task_moved = True
                break
        if task_moved:
            break

    if not task_moved:
        print(f'Task ID {task_id} not found in board "{board_name}".')
    else:
        save_data(data)
