from datetime import date, datetime, timedelta

class Task:
    def __init__(self, title: str, description: str, due_date: date, priority: str = "Medium", notes: str = "", duration: int = 0, recurrence: str = "", status: str = "Pending", dependencies: list = []):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.notes = notes
        self.duration = duration
        self.recurrence = recurrence
        self.status = status
        self.dependencies = dependencies

    def is_due_today(self) -> bool:
        return self.due_date == date.today()

class Schedule:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task_title: str):
        for task in self.tasks:
            if task.title == task_title:
                self.tasks.remove(task)
                break

    def get_task(self, task_title: str) -> Task:
        for task in self.tasks:
            if task.title == task_title:
                return task
        return None

    def list_overdue_tasks(self) -> list:
        result = [i for i in self.tasks if i.due_date < date.today()]
        return result

    def list_tasks_due_today(self) -> list:
        result = [i for i in self.tasks if i.is_due_today()]
        return result

    def sort_tasks_by_due_date(self) -> list:
        result = sorted(self.tasks, key=lambda task: task.due_date)
        return result

    def update_task(self, task_title: str, **kwargs):
        task = self.get_task(task_title)
        if task:
            for key, value in kwargs.items():
                setattr(task, key, value)

    def weekly_schedule(self, start_date: date) -> list:
        end_date = start_date + timedelta(days=7)
        result = [i for i in self.tasks if start_date <= i.due_date < end_date]
        return result

    def monthly_schedule(self, year: int, month: int) -> list:
        first_day = date(year, month, 1)
        last_day = date(year, month + 1, 1) - timedelta(days=1)
        result = [i for i in self.tasks if first_day <= i.due_date <= last_day]
        return result
      
    def list_tasks_by_priority(self, priority: str) -> list:
        result = [i for i in self.tasks if i.priority == priority]
        return result

    def save_to_file(self, filename: str):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.title},{task.description},{task.due_date},{task.priority},{task.notes},{task.duration},{task.recurrence},{task.status},{';'.join([dep.title for dep in task.dependencies])}\n")

    def load_from_file(self, filename: str):
        self.tasks = []
        with open(filename, "r") as file:
            for line in file:
                task_data = line.strip().split(",")
                title = task_data[0]
                description = task_data[1]
                due_date = datetime.strptime(task_data[2], "%Y-%m-%d").date()
                priority = task_data[3]
                notes = task_data[4]
                duration = int(task_data[5])
                recurrence = task_data[6]
                status = task_data[7]
                dependencies = [self.get_task(dep_title) for dep_title in task_data[8].split(";") if dep_title]
                task = Task(title, description, due_date, priority, notes, duration, recurrence, status, dependencies)
                self.add_task(task)

    def list_tasks_with_notes(self) -> list:
        result = [i for i in self.tasks if i.notes]
        return result

    def mark_as_completed(self, task_title: str):
        task = self.get_task(task_title)
        if task:
            task.status = "Completed"

    def list_completed_tasks(self) -> list:
        result = [i for i in self.tasks if i.status == "Completed"]
        return result

    def find_task_by_keyword(self, keyword: str) -> list:
        result = [i for i in self.tasks if keyword.lower() in i.title.lower() or keyword.lower() in i.description.lower()]
        return result


    def check_deadlines(self) -> list:
        result = [i for i in self.tasks if i.due_date == date.today() + timedelta(days=1)]
        return result

    def list_all_tasks(self) -> list:
        result = self.tasks
        return result

    def list_tasks_by_duration(self, min_duration: int, max_duration: int) -> list:
        result = [i for i in self.tasks if min_duration <= i.duration <= max_duration]
        return result

    def task_history(self) -> list:
        history = []
        for task in self.tasks:
            if task.status == "Completed":
                history.append(("completed", task))
            elif task.status == "Pending":
                history.append(("added", task))
            else:
                history.append(("updated", task))
        return history

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if task.status != "Completed"]

    def list_recurring_tasks(self) -> list:
        result = [i for i in self.tasks if i.recurrence]
        return result

    def set_reminder(self, task_title: str, reminder_date: date):
        task = self.get_task(task_title)
        if task:
            task.reminder_date = reminder_date

    def completion_percentage(self) -> float:
        if not self.tasks:
            return 0.0
        result = (len(self.list_completed_tasks()) / len(self.tasks)) * 100
        return result



#Приклади виклику функцій з очікуваним виводом
data = " Apple, Banana , orange "
cleaned = clean_data(data)
print(cleaned)  

emails = "mail us test@example.com and invalid-email.com.djwd with example@test.co"
valid_emails = filter_emails(emails)
print(valid_emails)  

words = "apple pear banana kiwi"
filtered_words = extract_keywords(words, 4)
print(filtered_words)  

texts = " Hello! , Yes? , No. , "
processed_texts = process_text(texts)
print(processed_texts)  

numbers = "10, 20,30"
normalized_numbers = normalize_data(numbers)
print(normalized_numbers)  

data = "hello*world*again"
concatenated = concatenate_strings(data, '*')
print(concatenated) 

numbers = "1, 2, test, 3, 4"
total_sum = sum_numeric_strings(numbers)
print(total_sum)  

numbers = "10 test30 40"
filtered = filter_numbers(numbers, 25)
print(filtered) 

numbers = "1, 2, 3, 4"
squared_numbers = map_to_squares(numbers)
print(squared_numbers) 

words = "apple,banana,carrot"
reversed_words = reverse_strings(words)
print(reversed_words)  

task1 = Task("Buy groceries", "Milk, Eggs, Bread", date(2024, 6, 20), priority="High")
task2 = Task("Doctor appointment", "Regular check-up", date(2024, 6, 21), priority="Medium")
task3 = Task("Submit report", "End of month financial report", date(2024, 6, 30), priority="Low", duration=120)


schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.add_task(task3)


all_tasks = schedule.list_all_tasks()
print([task.title for task in all_tasks]) 

tasks_due_today = schedule.list_tasks_due_today()
print([task.title for task in tasks_due_today]) 

overdue_tasks = schedule.list_overdue_tasks()
print([task.title for task in overdue_tasks])  

schedule.update_task("Doctor appointment", notes="Bring insurance card")
print(schedule.get_task("Doctor appointment").notes)  

schedule.mark_as_completed("Buy groceries")
print(schedule.get_task("Buy groceries").status) 

completed_tasks = schedule.list_completed_tasks()
print([task.title for task in completed_tasks])  

high_priority_tasks = schedule.list_tasks_by_priority("High")
print([task.title for task in high_priority_tasks])  
schedule.save_to_file("tasks.txt")

new_schedule = Schedule()
new_schedule.load_from_file("tasks.txt")
loaded_tasks = new_schedule.list_all_tasks()
print([task.title for task in loaded_tasks])  

completion_percent = schedule.completion_percentage()
print(completion_percent) 

tasks_by_duration = schedule.list_tasks_by_duration(60, 180)
print([task.title for task in tasks_by_duration]) 

deadlines_tomorrow = schedule.check_deadlines()
print([task.title for task in deadlines_tomorrow])  

schedule.clear_completed_tasks()
print([task.title for task in schedule.list_all_tasks()])

schedule.set_reminder("Submit report", date(2024, 6, 29))
print(schedule.get_task("Submit report").reminder_date)  