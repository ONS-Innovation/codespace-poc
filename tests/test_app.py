from streamlit.testing.v1 import AppTest

at = AppTest.from_file("../src/app.py").run()

# Test adding a task

at.text_input(key="task_input").input("Test Task").run()
at.button[0].click().run()

task_added = False
for test in at.session_state.tasks:
    if "Test Task" in test["task"]:
        task_added = True
        break

assert task_added, "Task was not added to the session state."

# Test removing a task

at.button(key="remove_0").click().run()

task_removed = True
for test in at.session_state.tasks:
    if "Test Task" in test["task"]:
        task_removed = False
        break

assert task_removed, "Task was not removed from the session state."

# Test toggling task completion

at.text_input(key="task_input").input("Toggle Task").run()
at.button[0].click().run()

# Task should now be in the session state
task = at.session_state.tasks[0]

assert task["task"] == "Toggle Task", "Task was not added correctly."

# Toggle the task completion

at.button(key="toggle_0").click().run()

task = at.session_state.tasks[0]
assert task["completed"] is True, "Task completion was not toggled correctly."
