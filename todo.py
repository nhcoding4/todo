import os

def main():    
    TOTAL_FUNCS = 4
    tasks: list[str] = []    

    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        choice = user_input_int(menu_prompt(), TOTAL_FUNCS)
        match choice:
            case 0:
                add_task(tasks)
                continue_program()
            case 1:
                delete_task(tasks)
                continue_program()
            case 2:
                list_tasks(tasks)
                continue_program()
            case 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                os._exit(os.EX_OK)                
            case _:
                print("Invalid option")               


def add_task(task_list: list[str]):
    task_list.append(input("\nEnter a task:\n-> "))
    print(f"{task_list[len(task_list)-1]} has been added to the list.")


def list_tasks(task_list: list[str]):
    print("")

    if len(task_list) == 0:
        print("There are no tasks in the list.")
        return
    
    for i, task in enumerate(task_list):
        print(f"{i+1}: {task}")        


def delete_task(task_list: list[str]):
    list_tasks(task_list)

    if len(task_list) == 0:   
        return 

    delete_index: int = user_input_int("Select a task to delete:\n-> ", len(task_list))
    old_task: str = task_list[delete_index]
    del task_list[delete_index]
    
    print(f"Deleted {old_task}.")


def user_input_int(prompt: str, limit: int) -> int:
    invalid_prompt = lambda: print(f"Invalid input. Please enter a value between 1 and {limit}")

    while True:        
        try:
            user_input = int(input(prompt))
            if user_input > 0 and user_input <= limit:
                return user_input - 1

            invalid_prompt()              
        
        except Exception as _:
            invalid_prompt()


def menu_prompt() -> str:
    return "Todo Application:\n\nEnter one of the following options:\n" \
    "1. Add a new task\n2. Delete a task\n3. List tasks\n4. Quit\n-> "


def continue_program():
    input("\nPress Enter to continue")
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()