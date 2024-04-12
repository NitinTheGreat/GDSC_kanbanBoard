import argparse

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Kanban board CLI')

    subparsers = parser.add_subparsers(dest='command')

    # Board commands
    board_parser = subparsers.add_parser('board', help='Manage boards')
    board_parser.add_argument('action', choices=['create', 'list', 'delete'], help='Action to perform')
    board_parser.add_argument('name', nargs='?', help='Name of the board')

    # Task commands
    task_parser = subparsers.add_parser('task', help='Manage tasks')
    task_parser.add_argument('action', choices=['create', 'update', 'delete', 'move', 'list'], help='Action to perform')
    task_parser.add_argument('board', help='Name of the board')
    task_parser.add_argument('task_id', nargs='?', help='ID of the task')

    args = parser.parse_args()
    print("Arguments parsed:", args)  # Debugging statement

    return args
