import streamlit as st

st.set_page_config(
    page_title="To Do List",
    page_icon=":clipboard:",
)

st.title("📝 To Do List App")

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

def add_task(task: str):
    """Add a new task to the list."""

    if task:
        st.session_state.tasks.append({"task": task, "completed": False})
        st.toast(f"Task '{task}' added!", icon="📝")

def remove_task(index: int):
    """Remove a task from the list."""

    if 0 <= index < len(st.session_state.tasks):
        removed_task = st.session_state.tasks.pop(index)
        st.toast(f"Task '{removed_task['task']}' removed!", icon="🗑️")

def toggle_task(index: int):
    """Toggle the completion status of a task."""

    if 0 <= index < len(st.session_state.tasks):
        st.session_state.tasks[index]["completed"] = not st.session_state.tasks[index]["completed"]
        status = "completed" if st.session_state.tasks[index]["completed"] else "not completed"
        st.toast(f"Task '{st.session_state.tasks[index]['task']}' is now {status}!", icon="✅" if status == "completed" else "❌")

# Input form for adding a new task

with st.form(key="task_form"):
    task_input = st.text_input("Enter a new task:")
    submit_button = st.form_submit_button(label="Add Task", on_click=add_task, args=(task_input,))

# Display the list of tasks

if st.session_state.tasks:
    st.subheader("Your Tasks")
    col1, col2, col3 = st.columns([3, 1, 1], gap="small")

    for index, task in enumerate(st.session_state.tasks):
        task_status = "✅" if task["completed"] else "❌"
        
        with col1:
            st.write(f"{task_status} {task['task']}")
        
        with col2:
            st.button("Toggle", key=f"toggle_{index}", on_click=toggle_task, args=(index,))
        
        with col3:
            st.button("Remove", key=f"remove_{index}", on_click=remove_task, args=(index,))

else:
    st.write("No tasks added yet. Please add a task to get started.")
