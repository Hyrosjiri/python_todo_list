import json


class ToDoList:  
    # Inicializace objektu a načtení úkolů
    def __init__(self, name_json):
        self.name_json = name_json
        self.todo_list = self.load_json()

    # Načtení ůkolu z JSON souboru
    def load_json(self):
        try:
            with open(self.name_json, "r", encoding="UTF-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []   
    
    # Uložení úkolů do JSON souboru
    def save_json(self):
        with open(self.name_json, "w", encoding="UTF-8") as file:
            json.dump(self.todo_list, file, ensure_ascii=False, indent=4)
    
    # Zobrazení všech úkolů
    def show_todo_list(self):
        if not self.todo_list:
            print("Seznam úkolů je prázdný.")
            return

        for i, task in enumerate(self.todo_list, start=1):
            print(f"{i}. {task}")
    
    # Přidání nového úkolu
    def add_task(self, task):
        task = task.strip()
        
        # Kontrola prázdného vstupu
        if not task:
            print("[CHYBA] Nebyl zadán žádný úkol.")
            return
        
        self.todo_list.append(task)
        self.save_json()
    
    # Odstranění úkolu podle čísla
    def remove_task(self, number_remove):
        if not 0 < number_remove <= len(self.todo_list):
            print("[CHYBA] Číslo úkolu není v seznamu.")
            return
        
        removed_task = self.todo_list.pop(number_remove - 1)
        self.save_json()
        
        print(f"Úkol '{removed_task}' byl odstraněn.")