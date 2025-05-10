import os
import json
import random
import datetime

# File paths for storing data
TASKS_FILE = 'tasks.json'
CONTACTS_FILE = 'contacts.json'
BUDGET_FILE = 'budget.json'
RECIPES_FILE = 'recipes.json'
MOVIES_FILE = 'movies.json'
EVENTS_FILE = 'events.json'
QUIZZES_FILE = 'quizzes.json'
VOTES_FILE = 'votes.json'
DIARY_FILE = 'diary.json'

def load_json(file_path):
#  Load JSON data from a file. If the file does not exist, return an empty dictionary.

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return {}

def save_json(data, file_path):
#    Save JSON data to a file.

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def task_manager():
#    Manage tasks including adding, viewing, completing, deleting, editing, and searching tasks.

    tasks = load_json(TASKS_FILE)

    def add_task():
#        Add a new task with details like name, category, priority, due date, and notes.

        task_name = input("Enter the task name: ")
        category = input("Enter the category (e.g., Work, Personal): ")
        priority = input("Enter the priority (Low, Medium, High): ")
        due_date = input("Enter the due date (YYYY-MM-DD): ")
        notes = input("Enter additional notes: ")
        tasks.append({
            "name": task_name,
            "completed": False,
            "category": category,
            "priority": priority,
            "due_date": due_date,
            "notes": notes
        })
        save_json(tasks, TASKS_FILE)
        print(f"Task '{task_name}' added successfully!")

    def view_tasks(show_all=True):
#        View tasks. Optionally filter to show only pending tasks.
 
        for idx, task in enumerate(tasks, 1):
            if show_all or not task["completed"]:
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['name']} - {status} - {task['category']} - {task['priority']} - Due: {task['due_date']}")
                if task['notes']:
                    print(f"   Notes: {task['notes']}")

    def complete_task():
#        Mark a task as completed.

        view_tasks(show_all=False)
        task_num = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            save_json(tasks, TASKS_FILE)
            print(f"Task '{tasks[task_num]['name']}' marked as completed!")
        else:
            print("Invalid task number.")

    def delete_task():
#        Delete a task by its number.

        view_tasks()
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            task_name = tasks.pop(task_num)['name']
            save_json(tasks, TASKS_FILE)
            print(f"Task '{task_name}' deleted successfully!")
        else:
            print("Invalid task number.")

    def edit_task():
#       Edit the details of an existing task.
 
        view_tasks()
        task_num = int(input("Enter the task number to edit: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]['name'] = input(f"Enter the new name for '{tasks[task_num]['name']}': ")
            tasks[task_num]['category'] = input(f"Enter the new category for '{tasks[task_num]['name']}': ")
            tasks[task_num]['priority'] = input(f"Enter the new priority for '{tasks[task_num]['name']}': ")
            tasks[task_num]['due_date'] = input(f"Enter the new due date for '{tasks[task_num]['name']}': ")
            tasks[task_num]['notes'] = input(f"Enter the new notes for '{tasks[task_num]['name']}': ")
            save_json(tasks, TASKS_FILE)
            print(f"Task details updated!")
        else:
            print("Invalid task number.")

    def search_task():
#        Search for tasks by name.

        search_query = input("Enter the task name to search: ").lower()
        found_tasks = [task for task in tasks if search_query in task['name'].lower()]
        if found_tasks:
            for idx, task in enumerate(found_tasks, 1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['name']} - {status} - {task['category']} - {task['priority']} - Due: {task['due_date']}")
                if task['notes']:
                    print(f"   Notes: {task['notes']}")
        else:
            print("No matching tasks found.")

    def show_task_statistics():
#        Show statistics about tasks, including total tasks, completed tasks, pending tasks, and completion rate.

        total_tasks = len(tasks)
        completed_tasks = len([task for task in tasks if task['completed']])
        pending_tasks = total_tasks - completed_tasks
        print(f"Total tasks: {total_tasks}")
        print(f"Completed tasks: {completed_tasks}")
        print(f"Pending tasks: {pending_tasks}")
        if total_tasks > 0:
            completion_rate = (completed_tasks / total_tasks) * 100
            print(f"Completion rate: {completion_rate:.2f}%")

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Search Task")
        print("7. Show Task Statistics")
        print("8. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            edit_task()
        elif choice == '6':
            search_task()
        elif choice == '7':
            show_task_statistics()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

def contact_manager():
    """
    Manage contacts including adding, viewing, and searching contacts.
    """
    contacts = load_json(CONTACTS_FILE)

    def add_contact():
        """
        Add a new contact with details like name, phone number, and email address.
        """
        name = input("Enter the contact name: ")
        phone = input("Enter the phone number: ")
        email = input("Enter the email address: ")
        contacts.append({"name": name, "phone": phone, "email": email})
        save_json(contacts, CONTACTS_FILE)
        print(f"Contact '{name}' added successfully!")

    def view_contacts():
        """
        View all contacts.
        """
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['name']} - Phone: {contact['phone']} - Email: {contact['email']}")

    def search_contact():
        """
        Search for contacts by name.
        """
        search_query = input("Enter the contact name to search: ").lower()
        found_contacts = [contact for contact in contacts if search_query in contact['name'].lower()]
        if found_contacts:
            for idx, contact in enumerate(found_contacts, 1):
                print(f"{idx}. {contact['name']} - Phone: {contact['phone']} - Email: {contact['email']}")
        else:
            print("No matching contacts found.")

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def budgeting():
    """
    Manage budgeting including setting budgets, recording expenses, and viewing budgets.
    """
    budget = load_json(BUDGET_FILE)

    def set_budget():
        """
        Set a new budget for a category.
        """
        category = input("Enter the budget category: ")
        amount = float(input("Enter the amount: "))
        budget[category] = amount
        save_json(budget, BUDGET_FILE)
        print(f"Budget for '{category}' set to {amount}!")

    def record_expense():
        """
        Record an expense in a category.
        """
        category = input("Enter the expense category: ")
        amount = float(input("Enter the amount spent: "))
        if category in budget:
            budget[category] -= amount
            save_json(budget, BUDGET_FILE)
            print(f"Recorded {amount} expense for '{category}'. Remaining budget: {budget[category]}")
        else:
            print("Category not found. Please set a budget first.")

    def view_budget():
        """
        View the remaining budget for each category.
        """
        for category, amount in budget.items():
            print(f"Category: {category}, Remaining Budget: {amount}")

    while True:
        print("\nBudgeting")
        print("1. Set Budget")
        print("2. Record Expense")
        print("3. View Budget")
        print("4. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == '1':
            set_budget()
        elif choice == '2':
            record_expense()
        elif choice == '3':
            view_budget()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def recipe_manager():
    """
    Manage recipes including adding and viewing recipes.
    """
    recipes = load_json(RECIPES_FILE)

    def add_recipe():
        """
        Add a new recipe with details like name, ingredients, and instructions.
        """
        name = input("Enter the recipe name: ")
        ingredients = input("Enter the ingredients (comma separated): ").split(',')
        instructions = input("Enter the instructions: ")
        recipes[name] = {"ingredients": ingredients, "instructions": instructions}
        save_json(recipes, RECIPES_FILE)
        print(f"Recipe '{name}' added successfully!")

    def view_recipes():
        """
        View all recipes.
        """
        for name, details in recipes.items():
            print(f"Recipe: {name}")
            print(f"Ingredients: {', '.join(details['ingredients'])}")
            print(f"Instructions: {details['instructions']}")

    while True:
        print("\nRecipe Manager")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == '1':
            add_recipe()
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def movie_recommendation():
    """
    Manage movie recommendations including adding movies and recommending based on genre.
    """
    movies = load_json(MOVIES_FILE)

    def add_movie():
        """
        Add a new movie with details like name, genre, and rating.
        """
        name = input("Enter the movie name: ")
        genre = input("Enter the genre: ")
        rating = float(input("Enter the rating (0-10): "))
        movies[name] = {"genre": genre, "rating": rating}
        save_json(movies, MOVIES_FILE)
        print(f"Movie '{name}' added successfully!")

    def recommend_movie():
        """
        Recommend movies based on a preferred genre.
        """
        genre = input("Enter your preferred genre: ")
        recommended_movies = [name for name, details in movies.items() if details['genre'] == genre]
        if recommended_movies:
            print(f"Recommended movies in {genre} genre:")
            for movie in recommended_movies:
                print(f"{movie} - Rating: {movies[movie]['rating']}")
        else:
            print("No movies found in that genre.")

    while True:
        print("\nMovie Recommendation")
        print("1. Add Movie")
        print("2. Recommend Movie")
        print("3. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == '1':
            add_movie()
        elif choice == '2':
            recommend_movie()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def event_scheduler():
    """
    Manage events including adding and viewing events.
    """
    events = load_json(EVENTS_FILE)

    def add_event():
        """
        Add a new event with details like name and date.
        """
        name = input("Enter the event name: ")
        date = input("Enter the event date (YYYY-MM-DD): ")
        events[name] = date
        save_json(events, EVENTS_FILE)
        print(f"Event '{name}' added successfully!")

    def view_events():
        """
        View all events.
        """
        for name, date in events.items():
            print(f"Event: {name} - Date: {date}")

    while True:
        print("\nEvent Scheduler")
        print("1. Add Event")
        print("2. View Events")
        print("3. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == '1':
            add_event()
        elif choice == '2':
            view_events()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def quiz_application():
    """
    Manage quizzes including creating and taking quizzes.
    """
    quizzes = load_json(QUIZZES_FILE)

    def create_quiz():
        """
        Create a new quiz with a title and questions.
        """
        title = input("Enter the quiz title: ")
        questions = []
        while True:
            question = input("Enter a question (or type 'done' to finish): ")
            if question.lower() == 'done':
                break
            options = input("Enter the options (comma separated): ").split(',')
            answer = input("Enter the correct answer: ")
            questions.append({"question": question, "options": options, "answer": answer})
        quizzes[title] = questions
        save_json(quizzes, QUIZZES_FILE)
        print(f"Quiz '{title}' created successfully!")

    def take_quiz():
        """
        Take a quiz by answering questions and calculating the score.
        """
        title = input("Enter the quiz title to take: ")
        if title in quizzes:
            score = 0
            for q in quizzes[title]:
                print(f"Question: {q['question']}")
                for idx, option in enumerate(q['options'], 1):
                    print(f"{idx}. {option}")
                answer = input("Enter your answer: ")
                if answer == q['answer']:
                    score += 1
            print(f"Your score: {score}/{len(quizzes[title])}")
        else:
            print("Quiz not found.")

    while True:
        print("\nQuiz Application")
        print("1. Create Quiz")
        print("2. Take Quiz")
        print("3. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == '1':
            create_quiz()
        elif choice == '2':
            take_quiz()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def voting_system():
    """
    Manage voting including creating polls, voting, and viewing poll results.
    """
    votes = load_json(VOTES_FILE)

    def create_poll():
        """
        Create a new poll with a title and options.
        """
        poll_title = input("Enter the poll title: ")
        options = input("Enter the options (comma separated): ").split(',')
        votes[poll_title] = {option: 0 for option in options}
        save_json(votes, VOTES_FILE)
        print(f"Poll '{poll_title}' created successfully!")

    def vote():
        """
        Vote in an existing poll.
        """
        poll_title = input("Enter the poll title to vote on: ")
        if poll_title in votes:
            print("Options:")
            for idx, option in enumerate(votes[poll_title], 1):
                print(f"{idx}. {option}")
            choice = int(input("Choose an option by number: ")) - 1
            if 0 <= choice < len(votes[poll_title]):
                selected_option = list(votes[poll_title].keys())[choice]
                votes[poll_title][selected_option] += 1
                save_json(votes, VOTES_FILE)
                print("Vote recorded!")
            else:
                print("Invalid choice.")
        else:
            print("Poll not found.")

    def view_polls():
        """
        View all polls and their results.
        """
        for poll_title, options in votes.items():
            print(f"\nPoll: {poll_title}")
            for option, count in options.items():
                print(f"{option}: {count} votes")

    while True:
        print("\nVoting System")
        print("1. Create Poll")
        print("2. Vote")
        print("3. View Polls")
        print("4. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == '1':
            create_poll()
        elif choice == '2':
            vote()
        elif choice == '3':
            view_polls()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def digital_diary():
    """
    Manage diary entries including adding and viewing entries.
    """
    diary = load_json(DIARY_FILE)

    def add_entry():
        """
        Add a new diary entry with a date and content.
        """
        date = input("Enter the date (YYYY-MM-DD): ")
        entry = input("Enter your diary entry: ")
        diary[date] = entry
        save_json(diary, DIARY_FILE)
        print("Diary entry added!")

    def view_entries():
        """
        View all diary entries.
        """
        for date, entry in diary.items():
            print(f"{date}: {entry}")

    while True:
        print("\nDigital Diary")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    """
    Display the main menu and navigate to different modules.
    """
    while True:
        print("\nMain Menu")
        print("1. Task Manager")
        print("2. Contact Manager")
        print("3. Budgeting")
        print("4. Recipe Manager")
        print("5. Movie Recommendation")
        print("6. Event Scheduler")
        print("7. Quiz Application")
        print("8. Voting System")
        print("9. Digital Diary")
        print("10. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            task_manager()
        elif choice == '2':
            contact_manager()
        elif choice == '3':
            budgeting()
        elif choice == '4':
            recipe_manager()
        elif choice == '5':
            movie_recommendation()
        elif choice == '6':
            event_scheduler()
        elif choice == '7':
            quiz_application()
        elif choice == '8':
            voting_system()
        elif choice == '9':
            digital_diary()
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
