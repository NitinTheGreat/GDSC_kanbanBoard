from cli import parse_args
from storage import load_data, save_data
from kanban import create_board, list_boards, delete_board, create_task, list_tasks, delete_task, move_task

def main():
    print("Starting main function...")
    args = parse_args()
    data = load_data()

    if args.command == 'board':
        if args.action == 'create':
            create_board(data, args.name)
        elif args.action == 'list':
            list_boards(data)
        elif args.action == 'delete':
            delete_board(data, args.name)
    elif args.command == 'task':
        if args.action == 'create':
            title = input("Enter title: ")
            description = input("Enter description: ")
            assignee = input("Enter assignee: ")
            reporter = input("Enter reporter: ")
            status = input("Enter status (Todo, In Progress, Done): ")
            priority = input("Enter priority (Low, Medium, High): ")
            
            create_task(data, args.board, title, description, assignee, reporter, status, priority)
        elif args.action == 'list':
            list_tasks(data, args.board)
        elif args.action == 'delete':
            delete_task(data, args.board, args.task_id)
        elif args.action == 'move':
            new_status = input("Enter new status (Todo, In Progress, Done): ")
            move_task(data, args.board, args.task_id, new_status)

    save_data(data)

if __name__ == '__main__':
    main()
