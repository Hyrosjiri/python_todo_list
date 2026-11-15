from utils import clear_screen, wait_enter, print_title
from todo import ToDoList


def main():
    todo = ToDoList("tasks.json")

    while True:
        clear_screen()
        print_title("SEZNAM ÚKOLŮ")

        # Automatické zobrazení úkolů
        todo.show_todo_list()

        command = input(
            "\n[A] - Přidat \t[R] - Odebrat \t[Q] - Ukončit\n> "
        ).strip().lower()

        match command:
            case "a":
                task = input("Zadej nový úkol:\n> ")
                todo.add_task(task)

            case "r":
                try:
                    task_number = int(input("Zadej číslo úkolu:\n> "))
                    todo.remove_task(task_number)

                except ValueError:
                    print("[CHYBA] Zadej platné číslo.")

            case "q":
                break

            case _:
                print("[CHYBA] Neplatná volba.")

        wait_enter()
        
        
# Spuštění hlavního programu        
if __name__ == "__main__":
    main()