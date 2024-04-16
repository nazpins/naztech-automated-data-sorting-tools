class MaintenanceUtilityUI:
    def __init__(self, handle_user_input):
        self.handle_user_input = handle_user_input

    def run(self):
        print("Welcome to the AI Maintenance Utility. Type 'exit' to quit.")
        while True:
            user_input = input("> ")
            if user_input.lower() == 'exit':
                break
            command, path = self.handle_user_input(user_input)
            print(f"Command: {command}, Path: {path}")
