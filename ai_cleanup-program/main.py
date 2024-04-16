import logging
from ui import MaintenanceUtilityUI
from nlp import process_user_input
from maintenance import organize_files_by_type, find_duplicates, disk_cleanup, registry_cleanup, optimize_startup, defragment_disk

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='maintenance_log.log', filemode='a')

def execute_command(command, path):
    if command == 'organize files':
        organize_files_by_type(path)
    elif command == 'remove duplicates':
        find_duplicates(path)  # Assume this handles the deletion
    elif command == 'disk cleanup':
        disk_cleanup([path], recycle_bin=True)
    elif command == 'registry cleanup':
        registry_cleanup()
    elif command == 'optimize startup':
        optimize_startup()
    elif command == 'defragment disk':
        defragment_disk()
    else:
        logging.error(f"Unknown command: {command}")

def handle_user_input(user_input):
    command, path = process_user_input(user_input)
    execute_command(command, path)

if __name__ == '__main__':
    ui = MaintenanceUtilityUI(handle_user_input)
    ui.run()
