import datetime
from project import Project


def load_projects(file_name):
    projects = []
    try:
        with open(file_name, 'r') as file:
            # Skip the header line
            next(file)
            for line in file:
                name, start_date, priority, estimate, completion = line.strip().split('\t')
                start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y').date()
                projects.append(Project(name, start_date, int(priority), float(estimate), int(completion)))
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Starting with an empty project list.")
    return projects


def save_projects(file_name, projects):
    with open(file_name, 'w') as file:
        for project in projects:
            file.write(
                f"{project.name},{project.start_date.strftime('%d/%m/%Y')},{project.priority},{project.estimate},"
                f"{project.completion}\n")


def display_projects(projects):
    incomplete = [project for project in projects if project.completion < 100]
    completed = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete, key=lambda x: x.priority):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed, key=lambda x: x.priority):
        print(f"  {project}")


def filter_projects_by_date(projects):
    try:
        date_string = input("Show projects that start after date (dd/mm/yyyy): ")
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date_after(date)]
        for project in sorted(filtered_projects, key=lambda x: x.start_date):
            print(f"  {project}")
    except ValueError:
        print("Invalid date format. Please use the format dd/mm/yyyy.")


def add_new_project():
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    return Project(name, start_date, priority, estimate, completion)


def update_project(projects):
    display_projects(projects)
    try:
        index = int(input("Project choice: "))
        project = projects[index]
        new_completion = input("New Percentage: ")
        if new_completion:
            project.completion = int(new_completion)
        new_priority = input("New Priority: ")
        if new_priority:
            project.priority = int(new_priority)
    except (IndexError, ValueError):
        print("Invalid input. Please try again.")


def main():
    print("Welcome!")
    file_name = "projects.txt"
    projects = load_projects(file_name)
    print(f"Loaded {len(projects)} projects from {file_name}")

    while True:
        print("\nMenu:")
        print("  (L)oad projects")
        print("  (S)ave projects")
        print("  (D)isplay projects")
        print("  (F)ilter projects by date")
        print("  (A)dd new project")
        print("  (U)pdate project")
        print("  (Q)uit")
        choice = input(">>> ").upper()

        if choice == 'L':
            file_name = input("Enter filename: ")
            projects = load_projects(file_name)
        elif choice == 'S':
            file_name = input("Enter filename: ")
            save_projects(file_name, projects)
            print(f"Projects saved to {file_name}")
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            projects.append(add_new_project())
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            save_option = input(f"Would you like to save to {file_name}? ").lower()
            if save_option.startswith('y'):
                save_projects(file_name, projects)
                print(f"Projects saved to {file_name}")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
