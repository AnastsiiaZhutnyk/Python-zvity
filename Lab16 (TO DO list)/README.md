Лабораторна робота №16: Advanced TODO List
___
Мета роботи:
Метою цієї лабораторної роботи є розробка комплексної системи управління завданнями на Python. Ця система дозволить користувачам створювати, керувати та відстежувати завдання ефективно. Система управління завданнями складається з двох основних компонентів: класу Task та класу Schedule, кожен з яких має різноманітні атрибути та методи для полегшення організації, пріоритизації, планування та відстеження виконання завдань. 
___
Опис завдання:
```Python
Create Task Class
Create a Python class named Task with the following attributes:
title
description
due_date (use datetime.date )
Example of class usage:
Task 2: Add Method to Task Class
Add a method named is_due_today() to the Task class that checks if the task is due today and returns a boolean.
Example of class usage:
 
from datetime import date
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
from datetime import date
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today())
task.is_due_today()  # Expected output: True if today is the due
date
Task 3: Create Schedule Class
Create a class named Schedule that manages multiple tasks. It should have the following methods:
add_task(task: Task)
      remove_task(task_title: str)
     get_task(task_title: str) -> Task
Example of class usage:
  schedule = Schedule()
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task)
schedule.get_task("Buy groceries")  # Expected output: Task
object
Task 4: List Overdue Tasks
Add a method named list_overdue_tasks() to the Schedule class that returns a list of tasks that are overdue.
Example of class usage:
   from datetime import date, timedelta
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today() - timedelta(days=1))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date.today() + timedelta(days=2))
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_overdue_tasks()  # Expected output: [task1]
Task 5: List Tasks Due Today
Add a method named list_tasks_due_today() to the Schedule class that returns a list of tasks that are due today.
Example of class usage:
   from datetime import date
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today())

 task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date.today())
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_tasks_due_today()  # Expected output: [task1,
task2]
Task 6: Sort Tasks by Due Date
Add a method named sort_tasks_by_due_date() to the Schedule class that returns a list of tasks sorted by their due dates.
Example of class usage:
   from datetime import date, timedelta
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today() + timedelta(days=2))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date.today() + timedelta(days=1))
schedule.add_task(task1)
schedule.add_task(task2)
schedule.sort_tasks_by_due_date()  # Expected output: [task2,
task1]
Task 7: Update Task
Add a method named update_task(task_title: str, **kwargs) to the Schedule class that updates the attributes of a task.
Example of class usage:
   schedule = Schedule()
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task)
schedule.update_task("Buy groceries", description="Milk, Bread,
Eggs, Cheese", due_date=date(2024, 5, 26))
schedule.get_task("Buy groceries")  # Expected output: Task
object with updated attributes

Task 8: Task Status
Add a status attribute to the class which can be 'Pending', 'In Progress', or
  'Completed'. Modify Task and Example of class usage:
to handle task status updates.
 task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Pending")
schedule = Schedule()
schedule.add_task(task)
task.status = "In Progress"
schedule.update_task("Buy groceries", status="Completed")
schedule.get_task("Buy groceries").status  # Expected output:
"Completed"
Task 9: Weekly Schedule
Create a method weekly_schedule(start_date: date) in the Schedule class that returns a list of tasks for the week starting from the provided date.
Example of class usage:
   from datetime import date, timedelta
schedule = Schedule()
task1 = Task(title="Task 1", description="First task",
due_date=date(2024, 5, 21))
task2 = Task(title="Task 2", description="Second task",
due_date=date(2024, 5, 23))
schedule.add_task(task1)
schedule.add_task(task2)
start_date = date(2024, 5, 20)
schedule.weekly_schedule(start_date)  # Expected output: [task1,
task2]
Task 10: Monthly Schedule
Create a method monthly_schedule(year: int, month: int) in the Schedule class that returns a list of tasks for the specified month.
  Example of class usage:
Task
 Schedule

 from datetime import date
schedule = Schedule()
task1 = Task(title="Task 1", description="First task",
due_date=date(2024, 5, 21))
task2 = Task(title="Task 2", description="Second task",
due_date=date(2024, 6, 1))
schedule.add_task(task1)
schedule.add_task(task2)
schedule.monthly_schedule(2024, 5)  # Expected output: [task1]
Task 11: Task Priority
Add a priority attribute to the Task class which can be 'Low', 'Medium', or 'High'. Modify Task and Schedule to handle task priority.
Example of class usage:
Task 12: List Tasks by Priority
Add a method list_tasks_by_priority(priority: str) to the Schedule class that returns a list of tasks with the specified priority.
Example of class usage:
    task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), priority="High")
schedule = Schedule()
schedule.add_task(task)
task.priority  # Expected output: "High"
   task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), priority="High")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), priority="Low")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_tasks_by_priority("High")  # Expected output:
[task1]

Task 13: Save Schedule to File
Add a method save_to_file(filename: str) to the Schedule class that saves the schedule to a file.
Example of class usage:
Task 14: Load Schedule from File
Add a method load_from_file(filename: str) to the Schedule class that loads the schedule from a file.
   schedule = Schedule()
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task)
schedule.save_to_file("schedule.txt")
  Example of class usage:
Task 15: Task Notes
Add a notes attribute to the the task. Modify Task and
Example of class usage:
class that can store additional information about to handle task notes.
 schedule = Schedule()
schedule.load_from_file("schedule.txt")
 Task
  Schedule
 task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), notes="Use the discount
coupon")
schedule = Schedule()
schedule.add_task(task)
task.notes  # Expected output: "Use the discount coupon"
Task 16: List Tasks with Notes
Add a method list_tasks_with_notes() to the Schedule class that returns a list of tasks that have notes.
  
Example of class usage:
 task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), notes="Use the discount
coupon")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_tasks_with_notes()  # Expected output: [task1]
Task 17: Mark Task as Completed
Add a method mark_as_completed(task_title: str) to the Schedule class that marks the specified task as completed.
Example of class usage:
   task = Task(title="Buy groceries", description="Milk, Bread, Eggs
", due_date=date(2024, 5, 25))
schedule = Schedule()
schedule.add_task(task)
schedule.mark_as_completed("Buy groceries")
task.status  # Expected output: "Completed"
Task 18: List Completed Tasks
Add a method list_completed_tasks() to the Schedule class that returns a list of completed tasks.
Example of class usage:
   task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)

 schedule.add_task(task2)
schedule.list_completed_tasks()  # Expected output: [task1]
Task 19: Find Task by Keyword
Add a method find_task_by_keyword(keyword: str) to the Schedule class that returns a list of tasks that contain the specified keyword in their title or description.
Example of class usage:
   task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.find_task_by_keyword("assignment")  # Expected output:
[task2]
Task 20: Task Deadline Notification
Add a method check_deadlines() to the Schedule class that returns a list of tasks that are due in the next 24 hours.
Example of class usage:
   from datetime import datetime, timedelta
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=datetime.now().date() + timedelta(days=1))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=datetime.now().date() + timedelta(days=2))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.check_deadlines()  # Expected output: [task1]
Task 21: List All Tasks

  Add a method list_all_tasks() to the Schedule class that returns a list of all tasks.
Example of class usage:
 task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_all_tasks()  # Expected output: [task1, task2]
Task 22: Task Duration
Add a duration attribute to the class which specifies the expected time to complete the task in hours. Modify and Schedule to handle task duration.
Example of class usage:
Task 23: List Tasks by Duration
Add a method
int) to the class that returns a list of tasks whose duration falls within
the specified range.
Example of class usage:
 Task
  Task
 task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), duration=2)
schedule = Schedule()
schedule.add_task(task)
task.duration  # Expected output: 2
 list_tasks_by_duration(min_duration: int, max_duration:
  Schedule
 task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), duration=2)
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), duration=4)
schedule = Schedule()
schedule.add_task(task1)

 schedule.add_task(task2)
schedule.list_tasks_by_duration(1, 3)  # Expected output: [task1]
Task 24: Task History
Add a method task_history() to the Schedule class that returns a history of tasks added, removed, and updated in the schedule.
Example of class usage:
   schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task1)
schedule.remove_task("Buy groceries")
schedule.task_history()  # Expected output: [("added", task1),
("removed", task1)]
Task 25: Clear Completed Tasks
Add a method clear_completed_tasks() to the Schedule class that removes all completed tasks from the schedule.
Example of class usage:
   task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.clear_completed_tasks()
schedule.list_all_tasks()  # Expected output: [task2]
Task 26: Task Recurrence
Add a recurrence attribute to the   class that specifies if the task is recurring (daily, weekly, monthly). Modify   and Schedule to handle task recurrence.
Task
 Example of class usage:
Task

 task = Task(title="Water plants", description="Water the plants
in the garden", due_date=date(2024, 5, 25), recurrence="weekly")
schedule = Schedule()
schedule.add_task(task)
task.recurrence  # Expected output: "weekly"
Task 27: List Recurring Tasks
Add a method list_recurring_tasks() to the Schedule class that returns a list of recurring tasks.
Example of class usage:
   task1 = Task(title="Water plants", description="Water the plants
in the garden", due_date=date(2024, 5, 25), recurrence="weekly")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_recurring_tasks()  # Expected output: [task1]
Task 28: Task Reminders
Add a method set_reminder(task_title: str, reminder_date: date) to the Schedule class that sets a reminder for a specific task.
Example of class usage:
   task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule = Schedule()
schedule.add_task(task)
schedule.set_reminder("Buy groceries", date(2024, 5, 24))
 Task 29: Task Completion Percentage
Add a method completion_percentage() to the Schedule class that returns the percentage of completed tasks.
  
Example of class usage:
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.completion_percentage()  # Expected output: 50.0
Task 30: Task Dependency
Add a dependencies attribute to the Task class that specifies other tasks that need to be completed before the task can start. Modify Task and Schedule to handle task dependencies.
Example of class usage:
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Prepare breakfast", description="Use
groceries to prepare breakfast", due_date=date(2024, 5, 26),
dependencies=[task1])
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
task2.dependencies  # Expected output: [task1]

```
___
Виконання роботи:
```Python
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

```
___
Результати:
```Python
Task added: Buy groceries
All tasks: ['Buy groceries']
[<__main__.Task object at 0x103052cc0>]
Task added: Submit assignment
Task updated: Buy groceries
All tasks: ['Buy groceries', 'Submit assignment']
[<__main__.Task object at 0x103052cc0>, <__main__.Task object at 0x103052de0>]
Task marked as completed: Buy groceries
Completed tasks: ['Buy groceries']
[<__main__.Task object at 0x103052cc0>]
Task added: Water plants
Task history: [('added', 'Buy groceries'), ('added', 'Submit assignment'), ('updated', 'Buy groceries'), ('updated', 'Buy groceries'), ('added', 'Water plants')]
[('added', <__main__.Task object at 0x103052cc0>), ('added', <__main__.Task object at 0x103052de0>), ('updated', <__main__.Task object at 0x103052cc0>), ('updated', <__main__.Task object at 0x103052cc0>), ('added', <__main__.Task object at 0x103037b60>)]
Tasks with notes: []
[]
Tasks with priority Medium: ['Buy groceries', 'Submit assignment', 'Water plants']
[<__main__.Task object at 0x103052cc0>, <__main__.Task object at 0x103052de0>, <__main__.Task object at 0x103037b60>]



```
___
Висновки:Розробка системи управління завданнями на Python виявилася корисним практичним завданням, яке дозволило мені поглибити знання в об'єктно-орієнтованому програмуванні та управлінні даними. Створення класу Task з різноманітними атрибутами та методами надало можливість детально структурувати інформацію про кожне завдання. Додатково, створення класу Schedule дозволило ефективно керувати списком завдань, надаючи можливості для додавання, видалення, оновлення та сортування завдань.