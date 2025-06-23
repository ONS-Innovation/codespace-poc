from streamlit.testing.v1 import AppTest

at = AppTest.from_file("../src/app.py").run()


class TestApp:

    def test_session_state_initialization(self):
        assert "tasks" in at.session_state, "Session state 'tasks' was not initialized."
        assert isinstance(
            at.session_state.tasks, list
        ), "'tasks' should be a list in session state."
        assert len(at.session_state.tasks) == 0, "'tasks' should be empty initially."

    def test_add_task(self):
        at.text_input(key="task_input").input("New Task").run()
        at.button[0].click().run()

        task_added = False
        for test in at.session_state.tasks:
            if "New Task" in test["task"]:
                task_added = True
                break

        assert task_added, "Task was not added to the session state."

    def test_remove_task(self):
        at.text_input(key="task_input").input("Task to Remove").run()
        at.button[0].click().run()

        at.button(key="remove_0").click().run()

        task_removed = True
        for test in at.session_state.tasks:
            if "Task to Remove" in test["task"]:
                task_removed = False
                break

        assert task_removed, "Task was not removed from the session state."

    def test_toggle_task_completion(self):
        at.text_input(key="task_input").input("Toggle Task").run()
        at.button[0].click().run()

        # Task should now be in the session state
        task = at.session_state.tasks[0]

        assert task["task"] == "Toggle Task", "Task was not added correctly."

        # Toggle the task completion
        at.button(key="toggle_0").click().run()

        task = at.session_state.tasks[0]
        assert task["completed"] is True, "Task completion was not toggled correctly."
