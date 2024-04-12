import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Kanban board CLI')

    # Add subparsers for different commands
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Subparser for board commands
    board_parser = subparsers.add_parser('board', help='Manage boards')
    board_parser.add_argument('action', choices=['create', 'list', 'delete'], help='Action to perform')
    board_parser.add_argument('name', nargs='?', help='Name of the board')

    # Subparser for task commands
    task_parser = subparsers.add_parser('task', help='Manage tasks')
    task_parser.add_argument('action', choices=['create', 'list', 'delete', 'move'], help='Action to perform')
    task_parser.add_argument('board', help='Board name')
    task_parser.add_argument('task_id', nargs='?', help='Task ID for delete/move operations')
    task_parser.add_argument('new_status', nargs='?', help='New status for move operation (if applicable)')

    args = parser.parse_args()
    print(f"Arguments parsed: {args}")
    return args
